import os
from time import sleep
import sys
import random
from ridef import *
from ridef import logo, exe

def hapus():
	linux = "clear"
	windows = "cls"
	os.system([linux,windows][os.name == "nt"])
hapus()

#buat cmd linux nih om
def oss(cmd):
	os.system(cmd)
######################

#Ajg Malu maluim aja nih aowmakwmakwoakwkm :V
#def shell():
#	linus = "ls"
#	windos = "dir"
#	os.system([linus,windos][os.name == "nt"])
	
#Awoakwokawok
#def shel(file):
#	she = "sh"
#	shells = " {}".format(file)
#	os.system(she+shells)
#Sangat	
#def bash(file):
#	ba = "bash"
#	shh = " {}".format(file)
#	system(ba+shh)
#Primitifff :V
		
def reg():
	hapus()
	logo = fig(" [+] Registrasi [+] ")
	print(h+logo)
	print(r)
	try:
		user = input("Username: ")
		email = input("E-Mail: ")
		pw = input("Password: ")
		frml = email.find("@")
		if frml > 0 and frml > 1 and frml > 2 and frml > 3:
			asw = json.dumps({'username': user, 'email': email, 'password': pw}, sort_keys=False, indent=4)
			f = open("data/"+user, "w")
			f.write(asw)
			f.close()
			hapus()
			sleep(1)
			print("Registrasi selesai silahkan login...")
			sleep(random.random() * 3.5)
			pyth("risen.py")
		elif frml < 1:
			print("Email tidak valid!\nMohon masukkam E-mail yg valid!\nError: Couldn't find Character before '@'\nSilahkan isi bidang email dengan Benar!!!\n")
			sleep(3.5)
			reg()
		else:
			print("Email tidak valid!\nMohon masukkan E-mail yg valid!\nError: Character doesn't exists\nSilahkan gunakan '@' untuk mengisi bidang Email!\n")
			sleep(3.5)
			reg()
	except IOError as err:
		e = "Error: {}\n".format(err)
		print(e)
		sleep(3)
		reg()

def main_logo():
	#print(m+fig("[#] Login [#]")+r)
	logo(m, "[#] Login [#]", r)

def login():
	hapus()
	main_logo()
	paler = input("Masukkan Username: ")
	paler1= input("Masukkan Password: ")
	
	try:
	
		akuns = open("data/"+paler, "r")
		mek = akuns.read()
		meki = json.loads(mek)['username']
		nih = json.loads(mek)['password']
		imel = json.loads(mek)['email']
		akuns.close()
		
		if paler == meki or paler == imel and paler1 == nih:
			hapus()
			print(m+"Anda Telah Login... ")
			print(c+"[+]~~~~Profile~~~~[+]")
			print(k+"Username Anda: "+paler)
			print(h+"E-Mail Anda: "+imel)
			print(c+"Password Anda: "+bm+m+paler1+r)
			print(r+m+"[+]~~~~~~~~~~~~~~~[+]"+r)
			imput = input("[×]~ Back to menu? Y/n ")
			
			if imput == 'Y' or imput == 'y':
				print("Tunggu Sebentar...")
				sleep(3)
				hapus()
			
			elif imput == 'n' or imput == 'N':
				print("Oke.. kamu akan keluar dari tool...")
				sleep(2)
				exit()
				exit()
				exit()
				
			else:
				print(f"Masukkan Y/n :'(")
				sleep(2)
				login()
		
		else:
			print("Username atau Password anda salah!")
			sleep(2)
			pyth("risen.py")
		
	except NameError as oi:
		peler = "Silahkan registrasi bila belum mempunyai akun.\nError: {}\n".format(oi)
		print(peler)
		wh = input("Apakah anda sudah punya akun? Y/n > ")
		if wh == 'y' or wh == 'Y':
			sleep(2)
			pyth("risen.py")
		else:
			reg()
		login()
	
	except (FileNotFoundError):
		pedo = "Username atau Password tidak ditemukan!\nJika belum registrasi Jawablah pertanyaan .berikut!\n"
		print(pedo)
		wt = input("Apakah anda sudah punya akun? Y/n > ")
		
		if wt == 'y' or wt == 'Y':
			pyth("risen.py")
			
		elif wt == 'N' or wt == 'n':
			reg()
			
		else:
			print("Pilih Y atau N saja!")
			sleep(1)

risensama = os.getlogin()
if risensama == "u0_a201" or risensama == "RidhoSenpai":
	hapus()
	print(lbp+x+"Youkoso Ridho-sama! Saya menanti kedatangan anda...\n"+r)
	sleep(2)
else:
	print("Maaf sepertinya anda bukan orang yang saya cari, jadi mohon untuk login terlebih dahulu...")
	sleep(1)
	login()

def profiles():
	
	try:
		
		pro = open("data/"+paler, "r")
		baca = pro.read()
		user = json.loads(baca)['username']
		mail = json.loads(baca)['email']
		pw = json.loads(baca)['password']
		pro.close()
		print(c+"[+]~~~~Profile~~~~[+]")
		print(k+"Username Anda: "+user)
		print(h+"E-Mail Anda: "+mail)
		print(c+"Password Anda: "+m+bm+pw)
		print(r+m+"[+]~~~~~~~~~~~~~[+]"+r)
		imput = input("[×]~ Execute~> ")
		
		if imput == "back":
			print("Tunggu Sebentar...")
			sleep(3)
			hapus()
			logo_menu()
			
		elif imput == "exit":
			print("Thanks for Using my tool")
			sleep(1)
			hapus()
			exit()
			
		elif imput == "show pw" or imput == "show pass" or imput == "show password":
			clear()
			profiles()
			
		elif imput == "hide password" or imput == "hide pass" or imput == "hide pw":
			clear()
			print(c+"[+]~~~~Profile~~~~[+]")
			print(k+"Username Anda: "+user)
			print(h+"E-Mail Anda: "+mail)
			print(c+"Password Anda: "+bm+pw)
			print(r+m+"[+]~~~~~~~~~~~~~[+]"+r)
		
		else:
			sleep(0.8)
			hapus()
			print("Usage:\n\n\tback:\tUntuk kembali ke menu utama.\n\thelp:\tMenampilkan informasi ini.\n")
			
	except:
		sleep(random.random() * 9999999999)
		print("\n\nWOW!!! Anda sangat \"Primitif!\"\n")
	
	if __name__ == "__main__":
			
			while(True):
				profiles()
			

def deface():
	webdav = fig("WebDav")
	print(p+bm+webdav+r)
	print("\nContoh: www.google.com\n\tridhosenpai.my.id\n")
	web = input("Website > ")
	print("""
Contoh:
		Windows: D:\\Data\sc\index.html
		untuk android lokasinya ada di /storage/emulated/0/ tinggal masukin nama sc doang
	Note: Nama Script Harus index.html""")
	nama = input("Insert Script > ")
	
	try:
		
		if web == "exit" and path == "exit":
			print("Njirs Hekerr!")
			sleep(1)
			hapus()
			exit()
			
		else:
			#pycurl
			wdv(nama, web)
			print("Masih belum selesai nih PR :v")
			sleep(3)
			deface()
			
	except IOError as ngentot:
		loli = "Maaf terjadi kesalahan mohon coba beberapa saat lagi!\nError: {}\n".format(ngentot)
		print(loli)
		
	except KeyboardInterrupt as lol:
		print("Yahh bukan heker nih :'(")
		exit()

def figlets(warna,teks):
	red = Fore.RED
	green = Fore.GREEN
	blue = Fore.BLUE
	magenta = Fore.MAGENTA
	cyan = Fore.CYAN
	yellow = Fore.YELLOW
	black = Fore.BLACK
	white = Fore.WHITE
	lightred = Fore.LIGHTRED_EX
	lightgreen = Fore.LIGHTGREEN_EX
	lightblue = Fore.LIGHTBLUE_EX
	lightmagenta = Fore.LIGHTMAGENTA_EX
	prim = fig(teks)
	if warna == "red" or warna == "RED" or warna == "Red" or warna == "MERAH" or warna == "Merah" or warna == "merah":
		print(red+prim+r)
	elif warna == "yellow" or warna == "YELLOW" or warna == "Yellow" or warna == "kuning" or warna == "Kuning" or warna == "KUNING":
		print(yellow+prim+r)
	elif warna == "green" or warna == "Green" or warna == "GREEN" or warna == "hijau" or warna == "Hijau" or warna == "HIJAU" or warna == "ijo":
		print(green+prim+r)
	elif warna == "blue" or warna == "Blue" or warna == "BLUE" or warna == "biru" or warna == "Biru" or warna == "BLUE":
		print(blue+prim+r)
	elif warna == "magenta" or warna == "Magenta" or warna == "MAGENTA" or warna == "pink" or warna == "ungu" or warna == "merah muda" or warna == "Pink" or warna == "Ungu" or warna == "Merah muda" or warna == "Merah Muda" or warna == "PINK" or warna == "PINK" or warna == "UNGU" or warna == "MERAH MUDA":
		print(magenta+prim+r)
	else:
		err = "\t\nWarna {} tidak ditemukan!\n".format(warna)
		print(err)
	exece()

def exece():
	
	try:
		i = input(m+"$i "+r)
		py = i.find('python')
		sh = i.find('sh')
		bash = i.find('bash')
		if i == "exit":
			exit()
			
		elif i == "help":
			print("Usage:\n[!] Same like a ShellScript\n\tls:\tList directory.\n\tcd:\tChange directory.\n\tpython:\tExecute python file or interpreter python.\n\tfiglet:\tShowing a figlet text\n\tback:\tBack to main menu\n\texit:\tExit from this tool.\n")
			sleep(1)
			exece()
			
		elif i == "back":
			logo_menu()
		
		elif i == "figlet":
			teks = input("Masukkan Text: ")
			warna = input("Masukkan Warna: ")
			figlets(warna,teks)
			
		elif py == 0:
			rep = i.replace('python ', '')
			pyth(rep)
		
		elif i == "{}".format(i):
			oss(i)
			
		else:
			print("Usage: \n\tKetik help untuk info lebih lanjut.\n")
			sleep(2)
			
			while(True):
				exece()
	
	except (KeyboardInterrupt):
		jam = "\nMaaf om tool ini ga bisa pake ctrl+c :v!\n"
		print(m+jam+r)
		
	if __name__ == "__main__":
		while(True):
			exece()

def sub_menu():
	print("\n")
	f = fig("KONTOL")
	print(m+f+r)
	print("\n")
	exece()

def logom():
	cpc = os.cpu_count()	
	logonya = fig("      	Ridho        ")
	print(r)
	logonya1 = fig("      	Senpai   ")
	print(r)
	print(c+"[+]-----------------------------------[+]"+r)
	print(r)
	print(r+lp+lbm+logonya+r+lm+lbp+logonya1+r+r+r)
	print("\nAuthor: RidhoSenpai\nGitHub:"+lh+" https://github.com/RidhoSenpai"+r)
	if cpc > 3:
		print(lb+"Core Used"+r+":"+lm, cpc,r+"\nTotal Tool: 17\n{}\n".format("Bagi hp kentang cpu used 4 udah masuk mode ngebut om :v"))
	elif cpc >= 2:
		print(lb+"Core Used"+r+":"+h, cpc,r+"\nTotal Tool: 17\n")
	elif cpc == 1:
		print(lb+"Core Used"+r+":"+lm, cpc,r+"\nHP anda sedang dalam kondisi Prima!\n\nTotal Tool: 17\n")

	print(m+"[{}+{}]---------------".format(k,m)+r+k+"MENU"+r+m+"----------------[{}+{}]".format(k,m)+r)
	print(r)
	print("[1]~ Profile")
	print("[2]~ Register")
	print("[3]~ Keluar")
	print("[4]~ Menu Lainnya")
	print("[5]~ IP Geo Location")
	print("[6]~ Deface (WebDav)")
	print("[7]~ Nulis di kertas")
	print("[8]~ Kusonime Scrapper")
	print("[9]~ Encoder File & Gambar (base64)")
	print("[10]~ Decoder File & Gambar (base64)")
	print("[11]~ Quotes-sad [new]")
	print("[12]~ Script Deface Creator")
	print("[13]~ Spam SMS")
	print("[14]~ Hater Alpin (Khusus Hater alpin)")
	print("[15]~ WinRate Kalkulator")
	print("[16]~ WebDav (Only PC and Termux)")
	print("[17]~ Penghitung Togel SGP & HK 2D Jitu!")
	print(r)
	print(k+"[{}+{}]------------------".format(m,k)+m+"-----------------[{}+{}]".format(k, m)+r)
	print("\n")
logom()
def logo_menu():
	try:
		mas = int(input(m+"[+]~"+b+bc+"Choose"+r+k+"~> "+r))
		
		if mas == 1:
			print("Sedang Loading...")
			sleep(2)
			hapus()
			profiles()
			
		elif mas == 2:
			print("Register om")
			sleep(2)
			reg()
			
		elif mas == 3:
			print("Sampai Bertemu Kembali!")
			flet = fig("Bye Bye")
			print(flet)
			sleep(3)
			hapus()
			exit()
			exit()
			
		elif mas == 4:
			print("\n\n")
			sub_menu()
			
		elif mas == 5:
			print("Sabar ya mas... :v\n")
			sleep(1)
			hapus()
			pyth("data/ip")
			
		elif mas == 6:
			deface()
			
		elif mas > 17:
			primitif = '''
	Hah? sejak kapan tool ku jadi banyak gini :v

Total Tool:\t17
Choosed   :\t{}\n
'''.format(mas)
			print(p+primitif+r)
		
		elif mas == 7:
			pyth("data/nulis")
			
		elif mas == 8:
			pyth("data/Kusonime")
			
		elif mas == 9:
			pyth("data/encoder")
			
		elif mas == 10:
			pyth("data/decoder")
			
		elif mas == 11:
			pyth("data/quotes")
			
		elif mas == 12:
			pyth("data/screator")
			
		elif mas == 13:
			pyth("data/spamsms")
		
		elif mas == 14:
			pyth("data/alpin")
			
		elif mas == 15:
			pyth("data/wrcalc")
			
		elif mas == 16:
			pyth("data/webdav")
			
		elif mas == 17:
			pyth("data/mahal.py")
			
		else:
			print("\n")
			print(bm+x+"Plihan tidak tersedia!"+r)
			sleep(2)
				
	except ValueError as err:
		e = "\nUsage:\n\t1\t---\tSee Profile\n\t2\t---\tRegistration\n\t3\t---\tExit from this tool\n\t4\t---\tBash Menu\n\t5\t---\tIP Geolocation\n\t6\t---\tDeface Method WebDav\n\t7\t---\tNulis di Kertas V1.0(Beta)\n\t8\t---\tRemote Bot Telegram\n"
		print(e)
			
logo_menu()

if __name__ == "__main__":
	 
	while(True):
		
		logo_menu()