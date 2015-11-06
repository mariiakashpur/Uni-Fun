import collections, math, numpy

def expectation(numlist):
    '''returns expectation value of all elements in numlist
    numlist - list of real numbers'''
    dictnum = {}
    exp = 0
    for num in numlist:
        if num not in dictnum:
            dictnum[num] = 1
        else:
            dictnum[num] += 1
    for key in dictnum:
        exp += key * (dictnum[key]/float(len(numlist))) # formula of expectation is sum of x*p(x) for all variables
    return exp   

def information(numlist, y):
    '''returns information content of variable y (natural number) that occurs at least once in list numlist '''
    dictnum = {}
    for num in numlist:
        if num not in dictnum:
            dictnum[num] = 1
        else:
            dictnum[num] += 1
    probnum = dictnum[y]/float(len(numlist))
   
    return math.log(1/probnum,2) # formula of information is log(1/p(x)); we use log with base 2 - hence the second argument in log

def entropy(numlist):
    '''returns entropy for all elements in list of numbers numlist'''
    inf = []
    for num in numlist:
        inf.append(information(numlist,num)) # append to the inf list the information for each number in numlist
    return expectation(set(inf)) # since entropy is EXPECTATION OF INFORMATION, we get the expectation for the numbers in numlist; use set to prevent duplicates
                                 # e.g. if number occurs in numlist more than once

#print entropy([1,2,3,4,5,6,7,8])

# def wordList(wordFile):
#     '''return a list of unique words from wordFile'''
#     with open(wordFile, "r") as f:
#         words = f.read().split() # list of all word in file
#     return words


# ---------------- TASK 4 --------------

def wordDict(wordFile):
    '''return a dictionary of unique words from wordFile as keys and their probabilities as values'''
    wordDict = {}
    with open(wordFile, "r") as f:
        words = f.read().split() # list of all word in file
    for word in words:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1
    for word in wordDict:
        wordDict[word] = wordDict[word] / float(len(words))
    wordDict = collections.OrderedDict(wordDict)
    return wordDict

#print wordDict("10000-sentences.txt")

def wordsEntropy(wordDict):
    inf = []
    exp = 0
    for word in wordDict:
        inf.append(math.log(1/wordDict[word], 2)) #calculate information for each word
    return expectation(inf)  # use expectation function and pass a list of information values as argument


# print wordsEntropy(wordDict("10000-sentences.txt"))


#-------- TASK 5 ----------

mu, sigma = -7.5, 1 # mean and standard deviation
s = np.random.normal(mu, sigma)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()