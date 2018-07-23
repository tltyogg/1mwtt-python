# Calculate a table for each letter in the alphabet from a-z,
# and count how many times each letter appears in Alice in WONDERLAND

import codecs
import string
import pprint
from collections import Counter
from string import ascii_lowercase
pp = pprint.PrettyPrinter(indent=4)

with codecs.open('alice_in_wonderland.txt', encoding='utf-8', errors='ignore') as f:
    alice = Counter(letter for line in f
                    for letter in line.lower()
                    if letter in ascii_lowercase)
pp.pprint(sorted(alice.most_common()))






# raw = file.read()
#
# list = {}
#
# for letter in filename:
#     list[letter] = list.get(letter, 0) + 1
#
# print(list)
