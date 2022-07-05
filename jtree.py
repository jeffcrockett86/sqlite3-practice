from main import *
from Cell import Cell as C
from Row import Row as R
from Table import Table as T
from Col import Col
import sys
import nltk
from nltk import word_tokenize

text = word_tokenize("The dog is lazy")
nltk.pos_tag(text)

print(wt)
# print(dir(sys.stdout))

#make a table where the first column is all the five letter words
# and the second column is the part of speech for the word
words = open('wordleAlpha.txt', 'r').read().split('\n')[:-1]
table = T(name="Parts of Speech")
