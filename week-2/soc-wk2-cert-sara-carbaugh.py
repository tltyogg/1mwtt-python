
# Day 1
# print('')
# print('***** DAY ONE *****')
# print('')

# Calculate a table for each letter in the alphabet from a-z,
# and count how many times each letter appears in Alice in WONDERLAND
# Referenced https://stackoverflow.com/questions/18647707/count-letters-in-a-text-file

import codecs
import string
import pprint
# from collections import Counter
# from string import ascii_lowercase
# pp = pprint.PrettyPrinter(indent=4)
#
# with codecs.open('alice_in_wonderland.txt', encoding='utf-8', errors='ignore') as f:
#     alice = Counter(letter for line in f
#                     for letter in line.lower()
#                     if letter in ascii_lowercase)
# pp.pprint(sorted(alice.most_common()))
#
# print('')

# Day 2

print('')
print('***** DAY TWO *****')
print('')

# Make a function that prints A-Z and a-z
# for i in range((65,65+26),(97,97+26)):
#     print(i, "stands for ", chr(i))

# Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))
# message = input('Write your secret message : ')
#
# for i in message:
#     print(i, ord(i))


# Write a function that prints out all elements of the above board, starting from the first element of the first line, till the end. Each line should be read from beginning to end.
# M = 'land'
# o = 'water'
# world = [
#          [o,o,o,o,o,o,o,o,o,o,o],
#          [o,o,o,o,M,M,o,o,o,o,o],
#          [o,o,o,o,o,o,o,o,M,M,o],
#          [o,o,o,M,o,o,o,o,o,M,o],
#          [o,o,o,M,o,M,M,o,o,o,o],
#          [o,o,o,o,M,M,M,M,o,o,o],
#          [o,o,o,M,M,M,M,M,M,M,o],
#          [o,o,o,M,M,o,M,M,M,o,o],
#          [o,o,o,o,o,o,M,M,o,o,o],
#          [o,M,o,o,o,M,o,o,o,o,o],
#          [o,o,o,o,o,o,o,o,o,o,o]
#         ]
#
# for i in list(world):
#     print(i)


# Now write a function that prints out all elements in reverse.
# for i in list(world):
#     if world[i] >= 0
#     world = (max(world) - 1)
#     print(i, (max(world)) - 1)


# There is one small bug in the continent counter above. Can you find it and fix it? (Hint: change the world so that the continent borders the edge)



# Write a function that generates an n x n sized board with either land or water chosen randomly.


# Day 3

print('')
print('***** DAY THREE *****')
print('')
