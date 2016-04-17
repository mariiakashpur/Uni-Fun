from __future__ import division
from collections import Counter, defaultdict
import math, re
from itertools import izip
from Token import Token
from Sentence import Sentence


class Corpus():
	def __init__(self, goldPath, predictedPath):
		self.goldPath = goldPath
		self.predictedPath = predictedPath
		self.sents = []
		with open(goldPath) as gf, open(predictedPath) as pf:
			sent = Sentence()
			for gline,pline in izip(gf, pf): # open two files simultaneously
				if gline.strip() and pline.strip(): # check if lines not empty
					gtoken_tag = re.split(r'\t', gline)
					ptoken_tag = re.split(r'\t', pline)
					if gtoken_tag[0] == ptoken_tag[0]:
						token = Token(gtoken_tag[0], gtoken_tag[1], ptoken_tag[1]) # create new Token object
						sent.addToken(token) 
					else:
						raise Exception("Files not in sync")
				else:
					self.sents.append(sent)
					sent = Sentence()


    	










    
