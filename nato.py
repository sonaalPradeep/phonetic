def nato(in_str):
	'''
	This function can be used to convert a sentence into its NATO equivalent
	The sentence can contain alphanumeric characters or symbols, but the output will ignore the symbols
	except the space which is used for sparsing

	Returns -- A response string which spells the sentence and a list which consists of translations of
	each word
	'''

	phonetic_dict = {
	"A" : "ALPHA",
	"B" : "BRAVO",
	"C" : "CHARLIE",
	"D" : "DELTA",
	"E" : "ECHO",
	"F" : "FOXTROT",
	"G" : "GOLF",
	"H" : "HOTEL",
	"I" : "INDIA",
	"J" : "JULIETT",
	"K" : "KILO",
	"L" : "LIMA",
	"M" : "MIKE",
	"N" : "NOVEMBER",
	"O" : "OSCAR",
	"P" : "PAPA",
	"Q" : "QUEBEC",
	"R" : "ROMEO",
	"S" : "SIERRA",
	"T" : "TANGO",
	"U" : "UNIFORM",
	"V" : "VICTOR",
	"W" : "WHISKEY",
	"X" : "XRAY",
	"Y" : "YANKEE",
	"Z" : "ZULU",
	"1" : "ONE",
	"2" : "TWO",
	"3" : "THREE",
	"4" : "FOUR",
	"5" : "FIVE",
	"6" : "SIX",
	"7" : "SEVEN",
	"8" : "EIGHT",
	"9" : "NINER",
	"0" : "ZERO",
	}

	in_str = in_str.upper()
	words = in_str.split()

	out_str = ""
	out_list = []

	for word in words:
		word_list = []
		for ch in word:
			if ch.isnumeric() or ch.isalpha():
				if out_str == "":
					out_str += phonetic_dict[ch]
				else:
					out_str += " " + phonetic_dict[ch]

				word_list.append(phonetic_dict[ch])

		out_list.append(word_list)

	return out_str, out_list


if __name__ == "__main__":
	# The nato(in_str) function can be called as follows :
	output_string, output_list = nato("Hello World")
	print("Input string : {}".format("Hello World"))
	print("NATO string : {}".format(output_string))
	print("NATO list : {}".format(output_list))
	print()

	# The same function can be called with numbers as its parameters
	output_string, output_list = nato("123467890")
	print("Input string : {}".format("123467890"))
	print("NATO string : {}".format(output_string))
	print("NATO list : {}".format(output_list))
	print()

	# Note that spaces are used for sparsing words and all other symbols are ignored
	output_string, output_list = nato("!@#$% ^&*()")
	print("Input string : {}".format("!@#$% ^&*()"))
	print("NATO string : {}".format(output_string))
	print("NATO list : {}".format(output_list))
