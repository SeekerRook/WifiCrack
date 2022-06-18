mkdir bin
cp listen.sh ./bin/wclisten
cp crack.sh ./bin/wccrack
cp coffeeshop.py ./bin/coffeeshop
cp deauth.sh ./bin/wcdeauth
cp uninstall.sh ./bin/uninstallwc

chmod +x ./bin/*
sudo mv ./bin/* /usr/bin

rm -r ./bin

