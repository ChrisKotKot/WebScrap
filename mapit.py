#! python3
#mapit.py - Wyświetla mapę na podstawie pobranego adresu podanego z wiersza poleceń oraz pogodę

import webbrowser, sys
if len(sys.argv) > 1:
	#Pobranie adresu z wiersza poleceń
	address = ''.join(sys.argv[1:])
else:
	#Pobranie adresu ze schowka
	address = pyperclip.paste()

webbrowser.open('https://www.google.pl/maps/place/' + address)
webbrowser.open('https://www.google.pl/search?q=' + address + ' weather')