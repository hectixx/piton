#!/usr/bin/python3

'''
[ 10 - Dogodki tipkovnice ]
'''

import sys
if sys.version_info.major == 2:
	import Tkinter as tk
elif sys.version_info.major == 3:
	import tkinter as tk

'''
Event handlers - poslusalci
'''
def esc_pressed(event):
	print("[esc]")
	print(event.keysym)
	sys.exit()

def key_pressed(event, okno, premik):
	dx = 0
	dy = 0
	if (event.keysym == "Up"):
		dy=-premik
	elif(event.keysym == "Down"):
		dy=premik
	elif(event.keysym == "Left"):
		dx=-premik
	elif(event.keysym == "Right"):
		dx=premik
	x = okno.winfo_x()
	y = okno.winfo_y()
	okno.geometry("+{}+{}".format(x + dx, y+ dy))

	print("[Tipka]: {}, {}".format(event.keycode, event.keysym))


def prikazi_okno():
	okno = tk.Tk()
	okno.title('Dogodki tipkovnice')
	# okno.geometry('200x100+300+200')
	okno.geometry('{}x{}+{}+{}'.format(200, 100, 300, 200))
	

	# povezava poslusalcev z dogodki (key_pressed, esc)
	# ...
	okno.bind("<Escape>", esc_pressed)
	okno.bind("<Key>", lambda event, d = 5 : key_pressed(event, okno, d))


	# Return, Cancel, BackSpace, Tab, Escape, ...
	okno.mainloop()

if __name__ == "__main__":
	prikazi_okno()