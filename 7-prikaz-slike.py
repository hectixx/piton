#!/usr/bin/python3

'''
[ 7 - Risanje na platno; prikaz slike v formatu GIF ]
'''

import sys
if sys.version_info.major == 2:
	import Tkinter as tk
elif sys.version_info.major == 3:
	import tkinter as tk


FILE_NAME = 'invader.gif'


'''
Prikaz slike na risalni plosci
'''

def narisi(canvas):
	None


def prikazi_okno():
	okno = tk.Tk()
	# 1.1 - skrijemo okno med spremembami
	okno.withdraw()	
	okno.title("Poletna sola")
	okno.configure(background = 'light grey')

	panel = tk.Canvas(okno, width = 300, height = 200, bg = 'white')
	panel.pack()

	# funkcija na platno izrise sliko iz datoteke 'images/invader.gif'
	# -- referenco na sliko image (v funkciji img) potrebujemo, da je python ne izbrise
	image = narisi(panel)

	# 1.2 - prikazi okno
	okno.deiconify()
	okno.mainloop()

if __name__ == '__main__':
	prikazi_okno()
