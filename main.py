# --- CREDITS ----
# By MistyMan435
# EMAIL - diaralb@outlook.com 
# ----------------
# ---- License ----
# MIT LICENSE


from tkinter import *
import sys
import threading
import os
from dotenv import load_dotenv, find_dotenv
import requests
import json
import time

load_dotenv(find_dotenv('.env_vars'))

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'



buttonClicked = False


def give_hadith():
	global buttonClicked

	buttonClicked = True

	url = "https://api.sunnah.com/v1/hadiths/random"

	payload = {}
	headers = {'x-api-key':str(os.getenv('SUNNAH-API-KEY'))}

	response = requests.request("GET", url, data=payload, headers=headers)

	hadith = json.loads(response.text)

	collection = hadith['collection']
	bookNumber = hadith['bookNumber']
	chapterID = hadith['chapterId']
	hadithnumber = hadith['hadithNumber']

	thehadith = hadith['hadith']

	try:
		if buttonClicked is True:
			SmartHadithText.config(state=NORMAL)
			SmartHadithText.delete('1.0', 'end')
			SmartHadithText.insert(INSERT, thehadith[0]['body'].strip("<b></b><p></p><br/><br/><b></b>.<br/><br"))
			print(thehadith[0]['body'].strip("<b></b><p></p><br/><br/><b></b>.<br/><br") + color.BOLD + '\n --- WORKING STATUS CODE 200 ---' + color.END)
			SmartHadithText.config(state=DISABLED)
	except:
		print(color.BOLD + color.RED + 'Error has occurred' + color.END)

	collectionLabel.config(text=f"Collection - {collection}")
	hadithNumLabel.config(text=f"Hadith Number - {hadithnumber}")


def clear_page():
	SmartHadithText.config(state=NORMAL)
	SmartHadithText.delete(1.0, END)
	SmartHadithText.config(state=DISABLED)
	collectionLabel.config(text='')
	hadithNumLabel.config(text='')


root = Tk()
root.title('Hadith A Day')
root.geometry("1980x1080")
icon = PhotoImage(file='h-ico.png')
root.iconphoto(True, icon)
root.config(background='#D9D68B')

SmartHadithImg = PhotoImage(file='smart-hadith.png')



SmartHadith = Label(
	root,
	image=SmartHadithImg,
	bg='#D9D68B',
	text='',
	font=('Arial',20,'bold'),
	fg='white',
	compound='top',
	pady=10,
	padx=10

	)
SmartHadith.place(x=550, y=30)

SmartHadithText = Text(
	root,
	padx=15,
	pady=15,
	bg='#D9D68B',
	fg='white',
	font=('arial',20,'bold'),
	highlightthickness=0,
	borderwidth=1,
	state=DISABLED
	)
SmartHadithText.place(x=380, y=300)


StartHadithsButton = Button(
	root,
	text='Tell me a Hadith',
	fg='white',
	bg='black',
	activeforeground='white',
	activebackground='black',
	relief=RAISED,
	pady=5,
	command=give_hadith
	)

StartHadithsButton.pack(side=BOTTOM)

collectionLabel = Label(
	root,
	text='',
	font=('arial',22,'bold'),
	fg='white',
	bg='#D9D68B',
	

	)
collectionLabel.place(x=0, y=430)


hadithNumLabel = Label(
	root,
	text='',
	font=('arial',22,'bold'),
	fg='white',
	bg='#D9D68B'


	)

hadithNumLabel.place(x=0, y=480)

clearButton = Button(
	root,
	text='CLEAR PAGE',
	fg='white',
	bg='black',
	activeforeground='white',
	activebackground='black',
	relief=RAISED,
	pady=5,
	command=clear_page
	)

clearButton.place(x=1023, y=846)

root.mainloop()













