def nato(phonetic_dict, in_str):
	'''
	This function can be used to convert a sentence into its NATO equivalent
	The sentence can contain alphanumeric characters or symbols, but the output will ignore the symbols
	except the space which is used for sparsing

	Returns -- A response string which spells the sentence and a list which consists of translations of
	each word
	'''

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
	ld_dict = load_dict.load_dict()

	output_string, output_list = nato(ld_dict, "Hello World")
	print("Input string : {}".format("Hello World"))
	print("NATO string : {}".format(output_string))
	print("NATO list : {}".format(output_list))
	print()

	# The same function can be called with numbers as its parameters
	output_string, output_list = nato(ld_dict, "123467890")
	print("Input string : {}".format("123467890"))
	print("NATO string : {}".format(output_string))
	print("NATO list : {}".format(output_list))
	print()

	# Note that spaces are used for sparsing words and all other symbols are ignored
	output_string, output_list = nato(ld_dict, "!@#$% ^&*()")
	print("Input string : {}".format("!@#$% ^&*()"))
	print("NATO string : {}".format(output_string))
	print("NATO list : {}".format(output_list))
