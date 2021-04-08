#!/bin/bash

menu_option_one() {
  echo "Start openCV/flask Streamer"
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
	echo "AlphaBot2-Control launcher Version 0.1"
	echo "openCV/flask Streamer helper script Version 0.1"
	echo "AlphaBot2-Control Network Client Version 0.1"
	echo "AlphaBot2-Control Network Server Version 0.1"
	echo "AlphaBot2-Control PS3 Control Version 0.1"
	echo ""
	echo "https://robotsgo.net/ https://github.com/RobotsGo"
	echo "Credits: Spoonieau (Rick Spooner)"
}

launcher_exit() {
pkill flask
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
  echo "    	1  -  Menu Option 1: Start openCV/flask Streamer"
  echo "    	2  -  Menu Option 2: Start Network Client"
  echo "    	3  -  Menu Option 3: Start Network Server"
  echo "    	4  -  Menu Option 4: Start PS3 Control"
  echo "    	5  -  Menu Option 4: View component info"
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
    0 ) clear ; launcher_exit ;;
    * ) clear ; incorrect_selection ; press_enter ;;
  esac
done
