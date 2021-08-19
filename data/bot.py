import sys
import telebot
import random
from os import name
from os import system
from time import sleep
#from telebot import types
from colorama import Back, Fore, Style
from pyfiglet import figlet_format as figlet

m = Fore.RED
k = Fore.YELLOW
h = Fore.GREEN
b = Fore.BLUE
r = Style.RESET_ALL

kontol = "Bot Sudah Berjalan"
token = "1924407073:AAHd0ID-ZqxvhRYI0RheHNCcRpQIXyNukzI"
risen = telebot.TeleBot(token)
			
def clear():
	l = "clear"
	w = "cls"
	system([l,w][name == "nt"])

def wawan(type):
	for kontol in type + '\n':
		sys.stdout.write(kontol)
		sys.stdout.flush()
		sleep(random.random() * 0.5)

def program():
	clear()
	try:

			'''
			def core():
				icom = figlet("Bot Started")
				print(h+icom+r)
				risen.polling()
			'''
			@risen.message_handler(commands=['help'])
			def sub_main(message):
				first = types.InlineKeyboardMarkup()
				second = types.InlineKeyboardButton(text="Kontak Admin",url="t.me/hide_fact")
				first.add(second)
				risen.send_message(message.chat.id,"Untuk info lebih lanjut silahkan chat admin\nsilahkan tekan tombol di bawah ini",reply_markup=first)
				
			@risen.message_handler(commands=['menu'])
			def main(message):
				first = types.ReplyKeyboardMarkup()
				two = types.InlineKeyboardMarkup()
				second = types.KeyboardButton("Menu Game")
			#	third = types.KeyboardButton(["Group_Menu"])
				fourth = types.InlineKeyboardButton(text="Menu Game",url="t.me/hide_fact")
				first.add(second)
				two.add(fourth)
				risen.send_message(message.chat.id,"Menu",reply_markup=two)
				first = types.ReplyKeyboardMarkup()
				second = types.KeyboardButton("Game Ular")
				third = types.KeyboardButton("Game Tetris")
				fourth = types.KeyboardButton("Game TicTacToe")
				fifth = types.KeyboardButton("Game Lainnya!")
				first.row(second,third,fourth,fifth)
				risen.send_message(message.chat.id,"Menu Game",reply_markup=first)
					
			wawan(kontol)
			icom = figlet("Bot Started")
			print(h+icom+r)
			risen.polling()
			
	except:
			pass
			
program()
if __name__ == "__main__":
	while(True):
		program()