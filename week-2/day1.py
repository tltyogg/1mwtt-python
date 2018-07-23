# Functions, parameters
def moo(n):
    print('moo' * n)
    return 'moo' * n

# moo(0)
# moo(1)
# moo(2)

#for i in range(3):
#    moo(i)

def ask_recursively(question):
    print(question)
    reply = input('>').lower()
    if reply == 'yes':
        return True
    if reply == 'no':
        return False
    else:
        print('Please answer "yes" or "no".')
        ask_recursively(question)

ask_recursively('Have you read Chris Pines book?')

# Testing
# Test in another file to see what is not working in your code
# see file test_day5.py

# Reading and wrting files
import codecs

filename = "alice_in_wonderland.txt"
file = codecs.open(filename, "r",encoding='utf-8', errors='replace')
# for line in file:
#     print(line)

raw = file.read()
# print(raw[:65]) #prints from 0 character to 65th character
# print(raw[0:65]) #prints from 0 character to 65th character
# print(raw[65:500]) #prints from 65th character to 500th character
#
# print(len(raw))
#
# print(raw[163000:])

# Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in Alice in WONDERLAND
#
