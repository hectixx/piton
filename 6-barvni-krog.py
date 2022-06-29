#!/usr/bin/env python3

# shebang line: doloca, kako naj se izvede skripta
# ce v konzoli napisemo: ./krog.py  konzola izvede:  /usr/bin/env python krog.py

'''
[ 6 - Risanje na platno; izris elips ]
'''

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

'''
Vrne potemnjen odtenek barve za 'shade_factor'
- shade_factor
  novi R/G/B = trenutni R/G/B * (1 - shade_factor)
- tint_factor
  novi R/G/B = trenutni R/G/B + (255 - trenutni R/G/B) * tint_factor
'''

def odtenek_barve(hexColor, shade_factor):
	if (not hexColor.startswith('#')):
		print("[Napaka]: Barva mora biti podana v hex formatu #RRGGBB.")
		return hexColor
    # #FFA023 --> [0xFF, 0xA0, 0x23]
    # int(string, osnova): pretvori niz v stevilo; npr. int(0x0E, 16) --> 15 
	rgbHexValues = ["0x" + hexColor[x : x + 2] for x in [1, 3, 5]]
	rgb = [int(rgbHex, 16) for rgbHex in rgbHexValues]
	newRgb = [int((1 - shade_factor) * barva) for barva in rgb]
	# hex(15) --> '0x0E'
	newRgbHex = [hex(barva)[2:] for barva in newRgb]
	newHexColor = '#'
	for barva in newRgbHex:
		if len(barva) < 2:
			barva = '0' + barva
		newHexColor = newHexColor + barva
	return newHexColor

'''
funkcija za izris kroga
'''	

def circle(canvas, xs, ys, r, color = "red"):
	None
	
'''
Na platno 'canvas' narise pobarvan krog
'''

def narisi(canvas):
	None


def spremeni_rob(canvas, circles):
	None

def main():
	okno = tk.Tk()
	# 1. med spremembami skrijemo okno
	okno.withdraw()
	okno.title('Krog')

	# 2. na oknu naredimo; platno(vsebovalnik, sirina, visina, *lastnosti)
	panel = tk.Canvas(okno, width = 240, height = 230, bg = 'white')
	# upravitelj platna komponenete organizira v bloke in jih postavi na okno  
	panel.pack()

	# 3. klicemo metodo za izris kroga na platno in ji podamo platno
	narisi(panel)

	# 4. prikazemo okno in zazenemo dogodkovno zanko
	okno.deiconify()
	okno.mainloop()

if __name__ == '__main__':
	main()