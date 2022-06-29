#!/usr/bin/env python3

try:
	# Python2
	import Tkinter as tk
except ImportError:
	# Python3
	import tkinter as tk
import random

'''
[ 11 - Razred kvadrat, ki ga kontroliramo s tipkovnico ]
'''
















'''
funkcija main - vstopna tocka programa
'''	
		
def main():
	okno = tk.Tk()
	okno.title("Premikanje objekta")
	plosca = tk.Canvas(okno, width = 600, height = 500, bg = "white")
	plosca.pack()
	okno.update()
	
	x = 10
	y = 10
	# x = (plosca.winfo_width() - Kvadrat.stranica) // 2
	# y = (plosca.winfo_height() - Kvadrat.stranica) // 2

	# do tukaj ni objekta
	# - kreiraj objekt <kvadratek> razreda [Kvadrat]

	# ...
	
	okno.mainloop()


if __name__ == '__main__':
	main()