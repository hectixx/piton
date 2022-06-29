#!/usr/bin/env python

'''
[ 12 - Risanje na platno; dogodki miske ]
'''

import sys

if sys.version_info.major == 2:
	import Tkinter as tk
elif sys.version_info.major == 3:
	import tkinter as tk

'''
poslusalci za dogodke
'''
def mouse_button_pressed(event):
    print(str(event.num))

def left_mouse_button_pressed(event, canvas):
    print("klik [Levi gumb] " + ("na plosci" if (event.widget == canvas) else " "))




def main():
    okno = tk.Tk()
    canvas = tk.Canvas(okno, width = 300, height = 200, bg = 'white')
    canvas.pack()

    okno.bind("<Button>", mouse_button_pressed)
    okno.bind("<Button-1>", lambda event : left_mouse_button_pressed(event, canvas))



    okno.mainloop()

if __name__ == '__main__':
	main()