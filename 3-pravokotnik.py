#!/usr/bin/env python3

'''
[ 3 - Risanje na platno; pravokotnik ]
'''

import sys
if sys.version_info.major == 2:
	import Tkinter as tk
elif sys.version_info.major == 3:
	import tkinter as tk


'''
metoda postavi like na plosco
'''

def narisi(plosca):
	print('aaaa')
	a = 100
	b = 30 
	pravokotnik = plosca.create_rectangle(10, 20, 10 + a, 20 +b, fill = "green", outline ="green")
	kvadratek = plosca.create_rectangle(240, 600, 240 + b, 60 +a, fill = "blue", outline ="black")
	kvadrat = plosca.create_rectangle(100, 80, 100 + a, 80 +a, fill = "red", outline ="darkgreen", width = 4)


'''
ustvari okno (frame)
'''

def prikazi_okno():
	okno = tk.Tk()
	# 1.1 - skrijemo okno med spremembami
	okno.withdraw()
	okno.title("Pravokotnik")
	okno.configure(background = 'light gray')
	
	plosca = tk.Canvas(okno, width = 300, height = 200, bg = 'white')
	# postavi plosco na okno
	plosca.pack()

	narisi(plosca)

	# 1.2 - prikazi okno in pozeni dogodkovno zanko
	okno.deiconify()
	okno.mainloop()

if __name__ == '__main__':
	prikazi_okno()
