
# Exercise 1: Hello World!

# a) Write a program that prints out `Hello Python!'.
def helloPython():
	print "Hello Python!"

# b) Write a function greet that takes a name as input, prints a greeting to that person and returns the number of characters.
def greet(name):
	print "Hello " + name + "!"
	return len(name)


# Exercise 2:

# Write a program that calculates and prints the sum of all even numbers from 1 to 200.
# Hint: You can use the modulo operator % in order to determine divisibility.

def evenSum():
	total = 0
	for num in range(1, 201):
		if num % 2 == 0:
			total += num
	print total

# Exercise 3: Odd words

# a) Write a function count_odd_words that takes a list of words and returns the number of words in that list that consist of an uneven number of characters.
def count_odd_words(wordList):
	numOdd = 0
	for word in wordList:
		if len(word) % 2 == 0:
			continue
		numOdd += 1
	return numOdd


# b) Write a function get_odd_words that takes a list of words and returns a list of the words uneven length.
def get_odd_words(wordList):
	oddWords = list()
	for word in wordList:
		if len(word) % 2 != 0:
			oddWords.append(word)
	return oddWords

# Exercise 4: Words in a sentence

# Assume that a sentence is represented by a list of words: sent = ["It", "was", "a", "slow", "day"]
# Write a function upto_last that takes such a sentence and, using a for loop, prints every word together with its
# length except the last one (in this example `day'). That is, the loop should be exited after the word `slow'.

def upto_last(sentList):
	for i in range(len(sentList) - 1):
		print sentList[i], len(sentList[i])

# Exercise 5: Limerick statistics
# Assume that we are given a list of sentences where each nested list is a list of strings:
# sents = [["There", "was", "a", "young", "lady", "of", "Niger"],
# ["Who", "smiled", "as", "she", "rode", "on", "a", "tiger"],
# ["They", "returned", "from", "the", "ride"],
# ["With", "the", "lady", "inside"],
# ["And", "the", "smile", "on", "the", "face", "of", "the", "tiger"]]

# Write a function lim stats, that takes this list and then computes and prints the following values:
# a) How many words are there in all five sentences?
# b) How many characters are there in all five sentences?
# c) How many words are there on average in one sentence?
# d) How many characters does a word contain on average?
# Hint: For the exercises c) and d) it is not relevant, whether the result is a float or an integer.

def lim_stats(sentList):
	sentTotal = 0
	wordsTotal = 0
	charTotal = 0
	for sent in sentList:
		sentTotal += 1
		for word in sent:
			wordsTotal += 1
			for char in word:
				charTotal += 1
	wordsSentAv = wordsTotal / float(sentTotal)
	charWordAv = charTotal / float(wordsTotal)
	print wordsTotal, charTotal, wordsSentAv, charWordAv

s = """Hey! Hast du schon gesehen,
wie einfach es ist, in Python zu programmieren?
Es ist viel einfacher als in den meisten
anderen Sprachen, die man so kennt."""

def print_all_uppercased(s):
	"""prints all words from the string s that start with an upper cased letter"""
	words = s.split()
	for word in words:
		if word[0].isupper():
			print word

print_all_uppercased(s)
print "\n"

def a_to_o(s):
	"""replaces all a letters by o letters in the string s and then prints out the new text"""
	print s.replace("a", "o").replace("A", "O")

a_to_o(s)



def get_translations(in_file):
	"""from in_file, returns dict of German words as keys and their English translations as values"""
	de_en_dict = {}
	with open(in_file) as f:
		for line in f:
			word_list = line.split()
			de_en_dict[word_list[0]] = word_list[1]
	return de_en_dict



de_en_dict = get_translations("./Files_for_Assignment_2/de-en-dict.txt")


def translate(in_dict, in_filename, out_filename):
	"""writes translations of each word in in_filename from in_dict to out_filename; if it's not there writes the word in >< brackets; lines preserved"""
	with open(out_filename, 'w') as out_file, open(in_filename) as in_file:
		for line in in_file:
			word_list = line.split()
			new_line = ""
			for word in word_list:
				if word in in_dict:
					new_line += in_dict[word] + " "
				else:
					new_line += ">" + word + "<" + " "
			out_file.write(new_line[:-1] + "\n") # slice to get rid of unnecessary whitespace added by previous word changes

translate(de_en_dict, "./Files_for_Assignment_2/detext.txt", "./Files_for_Assignment_2/entext.txt")



import string


##
def delete_punctuation(s):
    """
    Deletes characters from string 's' which are contained in the string
    string.punctuation.
    """
    result = ""
    # your code goes here
    for char in s:
        if char in string.punctuation:
            result += ""
        else:
            result += char
    return result

# print delete_punctuation("Hello, hi!")

##
def get_words(filename):
    """
    Get a list with all words. Reads the file, lowercase all the words and delete all punctuation from the text. Returns the cleaned text as a list of words.
    """
    file_words = []
    # your code goes here
    with open(filename) as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                file_words.append(delete_punctuation(word.lower()))
    return file_words

# print get_words("sheet3.txt")

##
def get_bigrams(word_list):
    """
    Get all bigrams from the word list and store them with their frequency
    to a dictionary.
    """
    bigrams = {}
    # your code goes here
    for i in range(len(word_list)-1):
        bigram = (word_list[i], word_list[i+1])
        bigrams[bigram] = bigrams.get(bigram, 0) + 1
    return bigrams

# print get_bigrams(get_words("sheet3.txt"))

##
def sort_bigrams(bigrams):
    """
    Sort bigrams by frequency.
    """

    bigrams_list = []
    # your code goes here
    bigrams_list = [bigram for (bigram, freq) in sorted(bigrams.iteritems(), key=lambda x: x[1], reverse=True)]
    return bigrams_list

# print sort_bigrams(get_bigrams(get_words("sheet3.txt")))

# the main function of the program
def main():
    # your code goes here (Ex. 5)
    print sort_bigrams(get_bigrams(get_words("sheet3.txt")))
    pass


