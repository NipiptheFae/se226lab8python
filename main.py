from collections import Counter
from classes import *

f = open('weirdWords.txt', 'r')
a = ListCount(f)
b = DictCount(f)
a.calculateFreqs()
b.calculateFreqs()


