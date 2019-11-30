def nato(in_str):
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
	"Z" : "ZULU"
	}

	in_str = in_str.upper()
	out_str = ""
	out_list = []

	for ch in in_str:
		if out_str == "":
			out_str += phonetic_dict[ch]
		else:
			out_str += " " + phonetic_dict[ch]

		out_list.append(phonetic_dict[ch])


	return out_str, out_list


if __name__ == "__main__":
	input_string = input("Enter the string : ")

	output_string, output_list = nato(input_string)

	print(output_string)
