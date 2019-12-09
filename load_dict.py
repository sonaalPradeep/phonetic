import requests
from bs4 import BeautifulSoup

def load_dict(verbose = False, format = None):
	'''
	This function is used to load the phonetic dictionary, and should be called before using the NATO translator.
	If connected to the internet, the dictionary is loaded after scrapping the official ICAO website. Else a predefined set is used.

	The url of the ICAO specifications -- 'https://www.icao.int/Pages/AlphabetRadiotelephony.aspx'

	Returns -- Dictionary of letters and numbers and their corresponding NATO translation
	'''
	
	url = "https://www.icao.int/Pages/AlphabetRadiotelephony.aspx"
	page = requests.get(url).text

	try:
		soup = BeautifulSoup(page, 'lxml')

		table = soup.find("tbody")
		table1 = soup.find("th", attrs = {"class" : "ms-rteTableHeaderFirstCol-default"}).text
		table2 = soup.find("th", attrs = {"class" : "ms-rteTableHeaderLastCol-default"}).text

		alpha = {}

		alpha1 = table1.split('\n')
		alpha1[-1] = alpha1[-1][:-1]

		alpha2 = table2.split()[0::2][1:]
		for i in range(len(alpha2)):
			if alpha2[i] != alpha2[-1]:
				alpha2[i] = alpha2[i][:-1]

		for i in alpha1:
			ch, _, word = i.split(' ')
			alpha[ch] = word

		for i in alpha2:
			alpha[i[0]] = i

		numbers = {"1" : "One",
			"2" : "Two",
			"3" : "Three",
			"4" : "Four",
			"5" : "Five",
			"6" : "Six",
			"7" : "Seven",
			"8" : "Eight",
			"9" : "Niner",
			"0" : "Zero"}

		for ch, word in numbers.items():
			alpha[ch] = word

		if(format == "all_caps"):
			for ch, word in alpha.items():
				alpha[ch] = word.upper()

		if(format == "all_caps_off"):
			for ch, word in alpha.items():
				alpha[ch] = word.lower()

		if verbose:
			print("Loaded dictionary from URL")

	except:
		alpha = {
			"A" : "Alpha",
			"B" : "Bravo",
			"C" : "Charlie",
			"D" : "Delta",
			"E" : "Echo",
			"F" : "Foxtrot",
			"G" : "Golf",
			"H" : "Hotel",
			"I" : "India",
			"J" : "Juliett",
			"K" : "Kilo",
			"L" : "Limo",
			"M" : "Mike",
			"N" : "November",
			"O" : "Oscar",
			"P" : "Papa",
			"Q" : "Quebec",
			"R" : "Romeo",
			"S" : "Sierra",
			"T" : "Tango",
			"U" : "Uniform",
			"V" : "Victor",
			"W" : "Whiskey",
			"X" : "X-ray",
			"Y" : "Yankee",
			"Z" : "Zulu",
			"1" : "One",
			"2" : "Two",
			"3" : "Three",
			"4" : "Four",
			"5" : "Five",
			"6" : "Six",
			"7" : "Seven",
			"8" : "Eight",
			"9" : "Niner",
			"0" : "Zero"
		}

		if verbose:
			print("Loaded predefined dictionary")

	return alpha
