#!/usr/bin/python3

'''
[ 8 - Risanje na platno; primer premikanja objekta ]
'''

import sys

if sys.version_info.major == 2:
	import Tkinter as tk

elif sys.version_info.major == 3:
	import tkinter as tk

	
	
SIRINA_OKNA = 400
VISINA_OKNA = 250
BARVA_PLOSCE = 'white'

IMAGES_FOLDER = './images'
INVADER = 'invader.gif'

CIRCLE_SIZE = 20
dx = 5
dy = 2
barva = "#ED1C24"
barvaObroba = "#C40233"


'''
callback metodi 'move_ball' in 'move_invader'
'''

def move_ball(okno, plosca, krogla, dx):
	None


def move_invader(okno, plosca, image):
	None

'''
funkcija za izris risalne plosce
'''

def narisi(okno, plosca, pimg):
	None


'''
funkcija za prikaz okna
'''	

def prikazi_okno():
	# 1 - okno
	okno = tk.Tk()
	# 1.1 - skrijemo okno med spremembami
	okno.withdraw()	
	okno.title("Premikanje objektov")
	okno.configure(background = 'light grey')
	
	sirina_zaslona = okno.winfo_screenwidth()
	visina_zaslona = okno.winfo_screenheight()
	x = (sirina_zaslona - SIRINA_OKNA) / 2
	y = (visina_zaslona - VISINA_OKNA) / 3
	okno.geometry('%dx%d+%d+%d' % (SIRINA_OKNA, VISINA_OKNA, x, y))

	plosca = tk.Canvas(okno, width = SIRINA_OKNA, height = VISINA_OKNA, bg = BARVA_PLOSCE)
	plosca.pack()
	pimg = tk.PhotoImage(file = IMAGES_FOLDER + "/" + INVADER)

	# 2 - na canvas narisi sliko in kroglico
	#     kot argument podamo risalno plosco in sliko
	narisi(okno, plosca, pimg)

	# 1.2 - prikazi okno
	okno.deiconify()	
	okno.mainloop()

if __name__ == "__main__":
	prikazi_okno()