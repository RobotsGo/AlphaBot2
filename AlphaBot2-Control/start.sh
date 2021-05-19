#!/bin/bash

menu_option_one() {
  echo "Start ustreamer"
  ./startStreamer.sh &
  disown
}

menu_option_two() {
  echo "Start Network Client"
  echo "Type in the server ip address"
  read host
  
  python3 client.py -s $host
}

menu_option_three() {
	echo "Start Network Server"
	sudo python3 networkMapping.py
}

menu_option_four() {
	echo "Start PS3 Server"
	sudo python3 ps3Mapping.py
}

menu_option_five() {
	echo "Start XboxOne Server"
	sudo python3 xboxOneMapping.py
}

menu_option_six() {
	echo "Start Mod my pi Server"
	sudo python3 mmp1251Mapping.py
}

menu_option_seven() {
	echo "Start PG-9099 Server"
	sudo python3 ipegaPG9099.py
}

menu_option_eight() {
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
	echo "AlphaBot2-Control Version 0.1"
	echo ""
	echo "https://robotsgo.net/ https://github.com/RobotsGo"
	echo "Credits: Spoonieau (Rick Spooner)"
	echo "Gamepad support by PiBorg Gamepad Library"
	echo "https://github.com/piborg/Gamepad"
}

launcher_exit() {
sudo pkill -f ustreamer
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
  echo "RobotsGo AlphaBot2-Control launcher ver 0.1"
  echo ""
  echo "    	1  -  Menu Option 1: Start ustreamer"
  echo "    	2  -  Menu Option 2: Start Network Client Control"
  echo "    	3  -  Menu Option 3: Start Network Server"
  echo "    	4  -  Menu Option 4: Start PS3 Gamepad Control"
  echo "	5  -  Menu Option 5: Start XboxOne Gamepad Control"
  echo "	6  -  Menu Option 6: Start MMP1251 (Mod my pi) Gamepad Contorl"
  echo "	7  -  Menu Option 7: Start ipega PG-9099 bluetooth Gamepad control"
  echo "    	8  -  Menu Option 8: View component info"
  echo "    	0  -  Exit"
  echo ""
  echo -n "  Enter selection: "
  read selection
  echo ""
  case $selection in
    1 ) clear ; menu_option_one ; press_enter ;;
    2 ) clear ; menu_option_two ; press_enter ;;
    3 ) clear ; menu_option_three ; press_enter ;;
    4 ) clear ; menu_option_four ; press_enter ;;
    5 ) clear ; menu_option_five ; press_enter ;;
    6 ) clear ; menu_option_six ; press_enter ;;
    7 ) clear ; menu_option_seven ; press_enter ;;
    0 ) clear ; launcher_exit ;;
    * ) clear ; incorrect_selection ; press_enter ;;
  esac
done
