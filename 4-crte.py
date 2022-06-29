#!/usr/bin/env python3

'''
[ 4 - Risanje na platno; crte in elipse ]
'''

import sys
if sys.version_info.major == 2:
	import Tkinter as tk
elif sys.version_info.major == 3:
	import tkinter as tk

'''
funkcija, narise na plosco (Canvas) nekaj crt in elips
'''

def narisi(plosca):
	None

def prikazi_okno():
	okno = tk.Tk()
	# 1.1 - skrijemo okno med spremembami
	okno.withdraw()
	okno.title('Risanje crt na platno')
	okno.configure(background = 'light gray')

	panel = tk.Canvas(okno, width = 300, height = 200, bg = 'white')
    
	# postavitev plosce na okno
	panel.pack(side = tk.TOP)
	narisi(panel)
	
	# 1.2 - prikazi okno
	okno.deiconify()
	okno.mainloop()

if __name__ == '__main__':
	prikazi_okno()
