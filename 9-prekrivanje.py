#!/usr/bin/python3

'''
[ 9 - Risanje na platno; prekrivanje objektov ]
'''

import sys
if sys.version_info.major == 2:
	import Tkinter as tk
elif sys.version_info.major == 3:
	import tkinter as tk

# sirina in visina okna
wOkno = 300
hOkno = 200

'''
spremeni barvo vsem objektom v tabeli 'elementi'
'''

def spremeni_barvo(okno, elementi, canvas, podrocje):
	for zadetek in zadetki:
		canvas.itemconfig(zadetek, fill = "#D0F0C0")	
'''
izris risalne plosce
'''

def narisi(okno, plosca):
	# 1 - gradniki na zaslonu
	crta = plosca.create_line(50, 170, 280, 130, fill = '#0087BD', width = 2)
	kvadrat = plosca.create_rectangle(80, 80, 130, 130, fill = '#0087BD', outline = '#C0C0C0')
	krog = plosca.create_oval(160, 110, 180, 130, fill = '#4000FF', outline = '#1034A6')
	zunanji = plosca.create_oval(200, 20, 250, 70, fill = '#E60026', outline = '#960018')

	# 1.1 - podrocje, ki nas zanima
	(x1, yz, xd, ys) = (100, 100, 200, 150)
	podrocje = plosca.create_rectangle(x1,yz,xd,ys,dash = (4,2), outline= "#C0C0C0")

	zadetki= plosca.find_overlapping(x1, yz, xd,ys)
	print(zadetki)
	print(" ")

	for zadetek in zadetki:
		string = " "
		string = str(zadetek) + ". " + plosca.type(zadetek) + " ["
		string = str + plosca.itemceg(zadetek, "fill") + "]"


	# ...

def main():
	okno = tk.Tk()
	okno.withdraw()	
	okno.title('Risanje na platno')
	okno.configure(background = 'light grey')
	
	wZaslon = okno.winfo_screenwidth()
	hZaslon = okno.winfo_screenheight()
	xOkno = (wZaslon - wOkno) // 2
	yOkno = (hZaslon - hOkno) // 3
	okno.geometry('%dx%d+%d+%d' % (wOkno, hOkno, xOkno, yOkno))
	plosca = tk.Canvas(okno, width = wOkno, height = hOkno, bg='white')
	plosca.pack(side = tk.TOP)
	
	narisi(okno, plosca)
	
	okno.deiconify()
	okno.mainloop()

if __name__ == '__main__':
	main()
