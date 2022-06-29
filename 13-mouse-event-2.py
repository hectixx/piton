#!/usr/bin/python

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

'''
[13 - Razred RisanjeElips ]
'''

class RisanjeElips(object):
	
	BARVE = ['red', 'green', 'blue', 'yellow', 'magenta', 'grey']

	def __init__(self, okno, panel):
		None

	
		
def main():
	okno = tk.Tk()
	okno.title("Risanje elips")
	panel = tk.Canvas(okno, width = 500, height = 400, bg = 'white')
	panel.pack()
	
	# 
	
	okno.mainloop() 

if __name__ == '__main__':
	main()