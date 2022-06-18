
echo "   CARDS   "
iwconfig

read -p "interface to change to monitor : " wlanad

read -p "channel(use 9 if  unsure) : " monc 

sudo airmon-ng start $wlanad $monc
echo "\n\n"
echo "   CARDS   "
iwconfig

read -p "monitor interface : " wlanmon 


read -p "Press ENTER to start monitoring ... " check
trap ' ' INT
sudo airodump-ng $wlanmon 

read -p "BSSID : " bssid

read -p "CH : " ch

read -p "select dest filename : " path

read -p "Press ENTER to start monitoring .." check
trap ' ' INT
echo "sudo airodump-ng -c $ch --bssid $bssid -w $path $wlanmon" 

sudo airodump-ng -c $ch --bssid $bssid -w $path $wlanmon 

sudo airmon-ng stop $wlanmon

iwconfig
