mkdir bin
cp src/listen.sh ./bin/wclisten
cp src/crack.sh ./bin/wccrack
cp src/coffeeshop.py ./bin/coffeeshop
cp src/deauth.sh ./bin/wcdeauth
cp src/uninstall.sh ./bin/uninstallwc

chmod +x ./bin/*
sudo mv ./bin/* /usr/bin

rm -r ./bin

