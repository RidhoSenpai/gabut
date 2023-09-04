import os
import re
import sys
import json
import random
import requests
import subprocess
from time import sleep
from os import name as nm
from itertools import cycle
from os import system as sis
from threading import Thread
from random import random as acak
from colorama import Fore, Back, Style
from pyfiglet import figlet_format as figlet


#warna Foreground
m = Fore.RED
lm = Fore.LIGHTRED_EX
k = Fore.YELLOW
lk = Fore.LIGHTYELLOW_EX
h = Fore.GREEN
lh = Fore.LIGHTGREEN_EX
b = Fore.BLUE
lb = Fore.LIGHTBLUE_EX
u = Fore.MAGENTA
lu = Fore.LIGHTMAGENTA_EX
x = Fore.BLACK
p = Fore.WHITE
lp = Fore.LIGHTWHITE_EX
#warna Background
bm = Back.RED
lbm = Back.LIGHTRED_EX
bk = Back.YELLOW
lbk = Back.LIGHTYELLOW_EX
bh = Back.GREEN
lbh = Back.LIGHTGREEN_EX
bb = Back.BLUE
lbb = Back.LIGHTBLUE_EX
bu = Back.MAGENTA
lbu = Back.LIGHTMAGENTA_EX
bx = Back.BLACK
bp = Back.WHITE
lbp = Back.LIGHTWHITE_EX
#reset warna
r = Style.RESET_ALL
	
def clear():
	sis(["clear", "cls"][nm == "nt"])

def echo(text):
#	try:
#		import argparse
#		parser = argparse.ArgumentParser(description='Menampilkan Text')
#		parser.add_argument('text', help="Menampilkan Text Sederhana")
#		args = parser.parse_args()
#		for t in text:
#			sis(["python3 ridef.py "+t, "py ridef.py "+t][nm == "nt"])
#	except:
#		print("Maaf ada yang Error hehe")
#		if __name__ == "__main__":
#			print(text+args.text)
	#print("{}\n".format(text))
	print(text)

def printf(texts):
	print(f"\r"+texts)
	
def ain(pkg):
	subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
#	try:
#		import pkeg
#		print(f"modul {pkeg} ga ada!")
#		sleep(0.5)
#		print(f"sedang menginstall modul {pkeg}")
#		ain(pkeg)
#		sleep(1)
#		clear()
#	except (IOError, ValueError):
#		print("intinya ada mslh")

stop = False

def rilod(text):
	for lds in cycle(['^', '>', 'v', '<']):
		if stop:
			break
			
		sys.stdout.write('\r{}	' + lds).format(text)
		sys.stdout.flush()
		sleep(0.05)

	
def logo(textc, text, textf):
	return print(textc, figlet(text), textf)

def logok(textc, text, textf, teks, ter):
	return print(textc, figlet(text), textf, figlet(teks), ter)

def tulis(ketik):
	for tu in ketik:
		sys.stdout.write(tu)
		sys.stdout.flush()
		sleep(acak() * 0.25)
		
def ngetik(ketikan):
	for tik in ketikan:
		sys.stdout.write(tik)
		sys.stdout.flush()
		sleep(acak()*0.12345)
		
def rsleep(wkt):
	sleep(acak() * wkt)

def exe(file):
	try:
		return sis("python3 {}".format(file))
	except:
		return sis("python {}".format(file))

def remove(cmd):
	linux = "rm -rf {}".format(cmd)
	windows = "del {}".format(cmd)
	try:
		filez = os.path.isfile(cmd)
		adakah = os.path.lexists(cmd)
		if filez == True:
			if adakah == True:
				sis([linux, windows][nm == "nt"])
				print(lh+"\nSelesai!\nFile {} sudah dihapus...\n".format(cmd)+r)
			else:
				print("File {} Mungkin sudah terhapus!\n".format(cmd))
		else:
			if adakah == True:
				sis([linux, windows][nm == "nt"])
				print(lh+"\nSelesai!\nFolder {} sudah dihapus...\n".format(cmd)+r)
			else:
				print("Folder {} Mungkin sudah terhapus!\n".format(cmd))
	except(IOError):
		print("ErRoR")


def jsl(api, data, data1, data2):
	pk = requests.get(api).text
	i = open(".cache_json", "w")
	i.write(pk)
	i.close()
	try:
		tl = json.loads(".cache_json")[data][data1][data2]
		
	except(IOError):
		print("Maaf ada kesalahan!")
	
		