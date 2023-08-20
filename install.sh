#!/bin/bash
$config_dir=/home/$USER/.config/konfirmations
mkdir $config_dir
cp ./konfirmations.ini ./konfirmations $config_dir
echo "MessageFile=${config_dir}/konfirmations">>$config_dir/konfirmations.ini
cp ./konfirmations.py /home/$USER/.local/bin/
cp ./konfirmations.service /home/$USER/.config/systemd/user/
printf "All done! Be sure to enable the system service using systemd:\n\tsystemctl --user enable konfirmations.service\n\tsystemctl --user start konfirmations.service\nTry it out: python ~/.local/bin/konfirmations.py"
