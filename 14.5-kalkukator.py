#!/usr/bin/python3


'''
Program za kalkulator
'''

import sys
import math
import functools

if sys.version_info.major == 2:
	import Tkinter as tk
elif sys.version_info.major == 3:
	import tkinter as tk


# konstante
WINDOW_WIDTH = 312
WINDOW_HEIGHT = 318


'''
Razred [ Kalkulator ]
'''

class Kalkulator(object):

	def __init__(self, okno, sirina, visina):
		self.okno = okno
		self.izraz = '0'
		
		# 2.1 - spremenljivka za display
		self.displayString = tk.StringVar()
		self.displayString.set(self.izraz)
		
		# 2.2 - display frame
		dispFrame = tk.Frame(okno, width = sirina, height = 50, bg = 'light green', bd = 1, 
							highlightbackground = 'black', highlightcolor = 'black')
		dispFrame.pack(side = 'top')
		# 2.3 - display
		display = tk.Entry(dispFrame, font = ('arial', 16, 'bold'), textvariable = self.displayString, 
							width = 50, bg = '#EEE', bd = 0)
		display['justify'] = 'right'
		display.grid(row = 0, column = 0)
		display.pack(ipady = 10)
		
		# 3.1 - button frame
		self.btnFrame = tk.Frame(okno, width = visina, bg = 'grey')
		self.btnFrame.pack()
		# 3.2 - buttons
		sqrt = tk.Button(self.btnFrame, text = u'\u221A', fg = 'black', bg = '#DCDCDC', width = 10, height = 3, bd = 0, 
						cursor = 'hand2', command = lambda: self.klik('sqrt'))
		clear = tk.Button(self.btnFrame, text = 'C', fg = 'red', bg = '#DCDCDC', width = 21, height = 3, bd = 0, 
						cursor = 'hand2', command = lambda: self.clearIzraz())
					
		# vrstice: 2, 3, 4, 5
		self.createRow([7, 8, 9, '/'], 2)
		self.createRow([4, 5, 6, '*'], 3)
		self.createRow([1, 2, 3, '-'], 4)
		self.createRow([0, ','], 5)
		
		equals = tk.Button(self.btnFrame, text = '=', fg = 'black', bg = '#AFDBF5', width = 10, height = 3, bd = 0, 
							cursor = 'hand2', command = lambda: self.evaluate())
		plus = tk.Button(self.btnFrame, text = '+', fg = 'black', bg = '#DCDCDC', width = 10, height = 3, bd = 0, 
							cursor = 'hand2', command = lambda: self.klik('+'))
	
		# vrstica: 1
		sqrt.grid(row = 1, column = 1)
		clear.grid(row = 1, column = 2, columnspan = 2)
		# vrstica: 5
		equals.grid(row = 5, column = 2)
		plus.grid(row = 5, column = 3)
	
		for child in self.btnFrame.winfo_children(): 
			child.grid_configure(padx=1, pady=1)

		
	def createRow(self, values, vrstica):
		for i, value in enumerate(values):
			tipka = tk.Button(self.btnFrame, text=str(value), fg='black', bg='#FFF', width=10, height=3, bd=0, cursor='hand2')
			# functools: Higher-order functions and operations on callable objects
			# functools.partial: return a new partial object which when called will behave like func called
			tipka['command'] = functools.partial(self.klik, value)
			if (i == len(values) - 1):
				tipka['bg'] = '#DCDCDC'
			tipka.grid(row = vrstica, column = i)		
		
	'''
	event handlers
	'''
		
	def klik(self, key):
		#global izraz
		
		if (self.izraz == '0'):
			self.izraz = '';
			self.displayString.set(self.izraz)
		# 1.2 - dvakratno dodajanje * ali / ni dovoljeno
		if (self.izraz.endswith(tuple(['*', '/'])) and key in ['*', '/']):
			return
		# 1.3 - med operatorji dodaj presledek
		if (self.izraz != '' and key in ['+', '-', '*', '/']):
			self.izraz = self.izraz + ' '
		# 1.4 - za operatrjem dodaj presledek
		if (self.izraz != '' and str(key).isdigit() and not self.izraz[-1].isdigit() and self.izraz[-1] != ','):
			self.izraz = self.izraz + ' '
		
		# 2 - stevilko pripni nizu <izraz>
		if (key == 'sqrt'):
			self.izraz = key + '(' + self.izraz + ')';
		else:
			self.izraz = self.izraz + str(key)
		# 3 - osvezi spremenljivko, ki se prikazuje na displaju
		self.displayString.set(self.izraz)

	def evaluate(self):
		try:
			self.izraz = self.izraz.replace(",", ".")
			self.izraz = self.izraz.replace("sqrt", "math.sqrt")
			izracun = str(eval(self.izraz))
			izracun = izracun.replace(".", ",")
			self.displayString.set(izracun)
			self.izraz = str(izracun)
		except Exception as e:
			# pri izracunu je prislo do napake
			self.displayString.set("ERR")
			self.izraz = ''		

	def clearIzraz(self): 
		self.izraz = '0' 
		self.displayString.set('0')


def main():
	# 1 - okno
	#     window for calculator
	okno = tk.Tk()
	okno.title('Kalkulator')
	okno.configure(background = 'light green')
	okno.resizable(0, 0)
	x = (okno.winfo_screenwidth() - WINDOW_WIDTH) / 2
	y = okno.winfo_screenheight() / 4
	okno.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, x, y))
	
	# 2 - ustvarimo objekt razreda "Kalkulator"
	kalkulator = Kalkulator(okno, WINDOW_WIDTH, WINDOW_HEIGHT)	
	
	okno.mainloop()	

if __name__ == "__main__":
	main()