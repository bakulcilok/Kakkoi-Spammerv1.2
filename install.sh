#!/bin/bash
# Installing Module
# Waktu
sleep 1
echo "[•] Wait..."
echo
sleep 2
echo "			[!] Updating/Upgrade Program "
echo
sleep 2
pkg update && pkg upgrade -y
echo
echo "			[!] Installing Module..."
sleep 2
echo
pkg install python
pkg install python2
pip2 install ipython
pip2 install requests
pip2 install mechanize
pkg install neofetch
pkg install imagemagick
pkg install ruby
gem install lolcat
pkg install screenfetch
seleep 2
echo
echo "			[!] Sedang Menampilkan Informasi System..."
sleep 3
clear
screenfetch -A Slackware
sleep 2
echo
echo "				[✓] Module Telah Terinstall..."
sleep 1
echo
echo "				[•] Sekarang Anda Bisa Run Program Spam Nya..."
echo
sleep 1
# Note !!! Module Jangan Di Ubah Yaaa!!! Apa Lagi Program Python nYa!!!
# Kalau Mau Script Buat Sendiri Lah Jangan Hasil Recode...
# Kecuali Sudah Dapat Izin Dari Pemilik Sc Nya Baru Boleh...
			# STAY HALAL... BRO...
