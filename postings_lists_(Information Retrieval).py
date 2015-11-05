# A task for the Information Retrieval and Text Mining Class. 
# It deals with creating postings lists for terms
import re, os

def index(foldername):
	'''takes the path to the folder as an argument and puts all documents into a non-positional inverted index; 
	   result is a dictionary that contains the (normalized) term as key, the size of the postings list and the postings list itself as values. 
	   The postings list consists of ids of documents which contain the term.'''
	finalDict = {} # create an empty dictionary
	counter = 0
	for reviewFile in os.listdir(foldername): # for each file in the folder
		prelDict = [] # create an empty list where the unique words will be stored
		counter += 1
		if counter < 1000:
			with open(foldername + "/" + reviewFile, "r") as f: # open the file
				words = f.read().split() # split the text into a list of words, use spaces as separators
				for word in words: # for each word in the words list
					word = word.strip('\'\"-,.:;!?*()').lower() # delete punctuation that may be glued to the word
					pattern = re.compile("^[a-zA-Z'-0-9]+$") # compile a regex which checks for words being alphanumeric, with possible apostrophes and dashes
					if pattern.match(word): # if the word corresponds to regex
						if word not in prelDict: # if such word has not yet been added to prelDict
							prelDict.append(word) # append the word to it
				for word in prelDict: # for word in prelDict
					if word not in finalDict: # check if the word is not yet a key in our final dictionary
						finalDict[word] = [1, [int(reviewFile[:-4])]] # if not - add it, plus set size of postings lists to 1 (it's the first one for the word), 
						                                              # and create a list where postings list will be stored, add current file name without .txt 
					else:
						finalDict[word][0] += 1 # if the word is already in dict, increment size of postings lists by one
						finalDict[word][1].append(int(reviewFile[:-4])) # add current file name without .txt to postings list
	return finalDict
#print index("./files/files")

def query(term, foldername):
	'''returns the postings list for the term'''
	return index(foldername)[term][1]

# print query("camera", "./files/files")
# print query("nice", "./files/files")

def query2(term1, term2, foldername):
	'''returns intersection of postings lists for term1 and term2'''
	intersection= [] # create empty list for intersection postings list
	pl1 = (query(term1, foldername)) # set pl1 to postings list of term1
	pl2 = (query(term2, foldername)) # set pl2 to postings list of term2
	l1 = iter(list(pl1)) # set iterator for pl1
	l2 = iter(list(pl2)) # # set iterator for pl2
	l1Cur = next(l1) # set current in l1 to its first element
	l2Cur = next(l2) # set current in l2 to its first element
	status = True # set a flag for a while loop
	while status: # while status is True
		if l1Cur == l2Cur: # check if current elements in both postings lists are the same
			intersection.append(l1Cur) # add the intersection to the list
			l1Cur = next(l1, None) # set current element to next for l1; set a default value of None in case we ran out of elements
			l2Cur = next(l2, None) # set current element to next for l2
		elif l1Cur > l2Cur: # if current element in l1 is bigger than current element in l2
			l2Cur = next(l2, None) # set current element to next for l2
		else:
			l1Cur = next(l1, None) # set current element to next for l1
		if len(pl1) > len(pl2): # if length of pl1 is bigger
			status = l2Cur is not None # set status in accordance with existence of the next element in the shorter list
		else: # vice versa
			status = l1Cur is not None
	return intersection



# print query2("camera", "nice", "./files/files")
