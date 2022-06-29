#!/usr/bin/python3

'''
[ 14 - Obraze; preprost primer ]
'''

import sys
if sys.version_info.major == 2:
	import Tkinter as tk
elif sys.version_info.major == 3:
	import tkinter as tk


LABEL = 'Ime:'
BARVE = ['light blue', 'white']

'''
poslusalci za dogodke
'''







def main():
	okno = tk.Tk()
	okno.title('Preprost obrazec')
	okno.geometry('400x300')


	okno.mainloop()

if __name__ == '__main__':
	main()