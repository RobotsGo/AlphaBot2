#!/bin/bash

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
  
# Written by spoonie (Rick Spooner) for RobotsGo

menu_option_one() {
echo ""

echo "Set your desired Hostname"
read Hostname

echo " "

echo "SET WIFI country code - See https://en.wikipedia.org/wiki/ISO_3166-1"
echo "Remeber your country code as it will needed later for hostap setup"
read CCrpi

echo " "

echo "Removing uneeded packages..."
sudo apt-get remove -y realvnc-vnc-server
sudo apt-get remove -y chromium-browser
sudo apt-get remove -y chromium-browser-l10n
sudo apt-get remove -y chromium-codecs-ffmpeg-extra

echo " "

echo "Checking system updates..."
sudo apt-get update 
sudo apt-get -y full-upgrade

echo " "

echo "Enable SSH..."
sudo systemctl enable ssh
sudo systemctl start ssh

echo " "

echo "Installing AbphaBot2 RobotsGo required Dependencies..."
sudo apt-get install -y make gcc python3 python3-pip python3-gpiozero xrdp xboxdrv libusb-dev libevent-dev libjpeg8-dev libbsd-dev libraspberrypi-dev libgpiod-dev
sudo pip3 install rpi_ws281x adafruit-circuitpython-servokit psutil pynput netifaces

echo " "
 
echo "Add XboxOne controller bluetooh config..."
echo 'options bluetooth disable_ertm=Y' | sudo tee -a /etc/modprobe.d/bluetooth.conf

echo " "

echo "Compile sixpair for PS3 controller..."
mkdir ~/sixpair
cd ~/sixpair
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb

echo " "

echo "Clone RobotsGo AlphaBot2 repo..."
cd ~
git clone https://github.com/RobotsGo/AlphaBot2.git

echo " "

echo "Setting scripts to executable..."
chmod +x ~/AlphaBot2/AlphaBot2-Control/start.sh
chmod +x ~/AlphaBot2/AlphaBot2-Control/startStreamer.sh
chmod +x ~/AlphaBot2/AlphaBot2-Control/startGameHatClient.sh

echo " "

echo "Clone and build ustreamer with omx support"
cd ~
git clone --depth=1 https://github.com/pikvm/ustreamer
cd ~/ustreamer
make WITH_OMX=1
sudo make install

echo " "

echo "Adding needed entries to config.txt"
echo "gpu_mem_256" | sudo tee -a /boot/config.txt
echo "dtparam=spi=on" | sudo tee -a /boot/config.txt
echo "dtparam=i2c_arm=on" | sudo tee -a /boot/config.txt
echo "start_x=1" | sudo tee -a /boot/config.txt
sudo sed -i 's/dtparam=audio=on/#dtparam=audio=on/g' /boot/config.txt

echo " "

echo "Setting Hostname"
sudo hostnamectl set-hostname $Hostname
echo "127.0.0.1 "$Hostname | sudo tee -a /etc/hosts

echo " "

echo "Setting wifi wpa Country Code"
echo "country="$CCrpi | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
sudo iw reg set $CCrpi

echo " "

echo "Unblocking wifi"
sudo rfkill unblock wifi

echo "Updating EEPROM if required"
sudo rpi-eeprom-update -a

echo "Please restart for changes to take effect."
exit
}

menu_option_two() {
echo "Installing client required Dependencies"
sudo pip3 install pynput

echo " "

echo "Clone RobotsGo AlphaBot2 repo..."
cd ~
git clone https://github.com/RobotsGo/AlphaBot2.git

echo " "

echo "Setting scripts to executable..."
chmod +x ~/AlphaBot2/AlphaBot2-Control/start.sh
chmod +x ~/AlphaBot2/AlphaBot2-Control/startStreamer.sh
chmod +x ~/AlphaBot2/AlphaBot2-Control/startGameHatClient.sh

echo " "

echo "Done........"
exit
}

menu_option_three() {
echo "Set SSID Name"
read SSID

echo " "

echo "SET WPA passphrase - Must be more than eight charters long"
read WPA

echo " "

echo "SET WIFI country code - See https://en.wikipedia.org/wiki/ISO_3166-1"
read CC

echo " "

sudo apt-get install -y hostapd
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo apt-get install -y dnsmasq
sudo systemctl enable dnsmasq

echo " "
echo "Altering /etc/dhcpcd.conf..."
echo "interface wlan0" | sudo tee -a /etc/dhcpcd.conf
echo "static ip_address=10.13.69.1/24" | sudo tee -a /etc/dhcpcd.conf
echo "nohook wpa_supplicant" | sudo tee -a /etc/dhcpcd.conf

echo ""

echo "Altering /etc/dnsmasq.conf"
HOST=$(cat /etc/hostname)
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo touch /etc/dnsmasq.conf
echo "interface=wlan0" | sudo tee -a /etc/dnsmasq.conf
echo "dhcp-range=10.13.69.2,10.13.69.20,255.255.255.0" | sudo tee -a /etc/dnsmasq.conf
echo "domain=wlan" | sudo tee -a /etc/dnsmasq.conf
echo "address=/"$HOST".wlan/10.13.69.1" | sudo tee -a /etc/dnsmasq.conf

echo ""

echo "Building hostap config..."
sudo touch /etc/hostapd/hostapd.conf
echo "country_code="$CC | sudo tee -a /etc/hostapd/hostapd.conf
echo "interface=wlan0" | sudo tee -a /etc/hostapd/hostapd.conf
echo "ssid="$SSID | sudo tee -a /etc/hostapd/hostapd.conf
echo "hw_mode=a" | sudo tee -a /etc/hostapd/hostapd.conf
echo "channel=48" | sudo tee -a /etc/hostapd/hostapd.conf
echo "macaddr_acl=0" | sudo tee -a /etc/hostapd/hostapd.conf
echo "ieee80211d=1" | sudo tee -a /etc/hostapd/hostapd.conf
echo "ieee80211n=1" | sudo tee -a /etc/hostapd/hostapd.conf
echo "ieee80211ac=1" | sudo tee -a /etc/hostapd/hostapd.conf
echo "wmm_enabled=1" | sudo tee -a /etc/hostapd/hostapd.conf
echo "auth_algs=1" | sudo tee -a /etc/hostapd/hostapd.conf
echo "ignore_broadcast_ssid=0" |sudo tee -a /etc/hostapd/hostapd.conf
echo "wpa=2" | sudo tee -a /etc/hostapd/hostapd.conf
echo "wpa_passphrase="$WPA | sudo tee -a /etc/hostapd/hostapd.conf
echo "wpa_key_mgmt=WPA-PSK" | sudo tee -a /etc/hostapd/hostapd.conf
echo "wpa_pairwise=TKIP" | sudo tee -a /etc/hostapd/hostapd.conf
echo "rsn_pairwise=CCMP" | sudo tee -a /etc/hostapd/hostapd.conf


echo " "
echo "AlphaBot2 WIFI AP available @ 10.13.69.1 or " $HOST".wlan"
echo "Please restart for changes to take effect."
exit
}


menu_option_four() {
	echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	echo "@@@((((@@&((((((((((((((((%@@@@@@@@@@@@@"
	echo "@@@(((//@@@/////////////////****@@@@@@@@"
	echo "@@@(((((/&@@///////////////////***&@@@@@"
	echo "@@@((((((((@@(//////@@@@@@@@@///****@@@@"
	echo "@@@(((((((((@@@(((#@@@@#/(@@@@%/////(@@@"
	echo "@@@@@@@@@@@@@@@@@@@@@@/////@@@@/////*@@@"
	echo "@@@@@@@@(((@@@((//(@@@@&(%@@@@#/////(@@@"
	echo "@@@@@@@@((((#@@(((((%@@@@@@@&///////@@@@"
	echo "@@@@@@@@((((((@@@((((((///////////@@@@@@"
	echo "@@@@@@@@##(((((@@@(((((((///////@@@@@@@@"
	echo "@@@@@@@@###(((((&@@/(((((####@@@@@@@@@@@"
	echo "@@@@@@@@#####(((((@@#/////((##@@@@@@@@@@"
	echo "@@@@@@@@########(((@@@////(((((@@@@@@@@@"
	echo "@@@@@@@@###########(@@@///((((((#@@@@@@@"
	echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	echo "AlphaBot2-Setup Version 0.2"
	echo ""
	echo "https://robotsgo.net/ https://github.com/RobotsGo"
	echo "Credits: Spoonieau (Rick Spooner)"
}

launcher_exit() {
exit
}

press_enter() {
  echo ""
  echo -n "	Press Enter to continue "
  read
  clear
}

incorrect_selection() {
  echo "Incorrect selection! Try again."
}

until [ "$selection" = "0" ]; do
  clear
  echo ""
  echo ""
  echo "RobotsGo AlphaBot2-Setup Version 0.3"
  echo ""
  echo "    	1  -  Menu Option 1: Setup RobotsGo AlphaBot2 Robot platform"
  echo "    	2  -  Menu Option 2: Setup up PC client"
  echo "    	3  -  Menu Option 3: Setup AlphaBot2 as 5ghz WIFI AP + DHCP (RUN Menu Option 1 FIRST!!!!!)"
  echo "    	4  -  Menu Option 4: View info"
  echo "    	0  -  Exit"
  echo ""
  echo -n "  Enter selection: "
  read selection
  echo ""
  case $selection in
    1 ) clear ; menu_option_one ;;
    2 ) clear ; menu_option_two ; press_enter ;;
    3 ) clear ; menu_option_three ;;
    4 ) clear ; menu_option_four ; press_enter ;;
    0 ) clear ; launcher_exit ;;
    * ) clear ; incorrect_selection ; press_enter ;;
  esac
done
