#!/bin/bash
sudo mkdir /etc/konfirmations
suco cp ./konfirmations.ini ./konfirmations /etc/konfirmations/
sudo cp ./konfirmations.py /bin/konfirmations.py
sudo cp ./konfirmations.service /etc/systemd/system/
printf "All done! Be sure to enable the system service using systemd:\n\tsystemctl --user enable ~/.config/konfirmations/konfirmations.service\nTry it out:\n\tpython /bin/konfirmations.py\n"
