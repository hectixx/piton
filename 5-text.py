#!/usr/bin/env python3

'''
[ 5 - Risanje na platno; tekst ]
'''

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

'''
Prikaz metode create_text
'''

def narisi(platno):
	None

def main():
	okno = tk.Tk()
	okno.withdraw()
	okno.iconbitmap(r'text.ico')
	okno.title("Tekst")
    
	panel = tk.Canvas(okno, width = 300, height = 200, bg = 'white')  
	panel.pack()

	# funkcija na platno narise nekaj napisov
	narisi(panel)

	okno.deiconify()
	okno.mainloop()

if __name__ == '__main__':
	main()