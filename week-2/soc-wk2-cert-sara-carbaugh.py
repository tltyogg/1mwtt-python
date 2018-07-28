
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

# Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.
#
# my_dict = {
#     "a": 35000,
#     "b": 8000,
#     "z": 450
# }
#
# print(my_dict)
#
# my_dict["a2"] = 35000
#
# del(my_dict["a"])
#
# print(my_dict)


# Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.
#




# Create a dictionary with your own personal details, feel free to be creative and funny so for example, you could include key-value pairs with quirky fact, fav quote, pet. Practice adding, modifying, accesing.

# sara_dict = {
#     "name": "Sara Carbaugh",
#     "age": 36,
#     "mood": "overwhelmed",
#     "fav_quote": "I'd rather be absolutely ridiculous than absolutly boring. - Marilyn Monroe",
#     "fav_color": "dark goth purple",
#     "fav_tv_show": "Doctor Who"
# }
#
# sara_dict["mood"] = "really overwhelmed"
#
# sara_dict["fav_quote2"] = "Bitches get stuff done. - Tina Fey"
#
# print(sara_dict)


# Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.

# class Student():
#     def __init__(self, name, discord_id, fav_food, dream):
#     self.name = name
#     self.discord_id = discord_id
#     self.fav_food = fav_food
#     self.dream = dream
#
# s1 = Student("Virginia Balseiro ", "yesvirginia [Gold] [Volunteer] ", "pasta ", "moving to Europe")
# s2 = Student("Andreea Visanoiu ", "Andreea[Gold] ", "wontonmee ", "becoming a University teacher")
# s3 = Student("Cristy Tarantino ", "CristyTarantino[Gold] ", "pasta ", "being an amazing developer")
# s4 =
# s5 =



# Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.

# class Student():
#     def __init__(self, name, email, discord_id, skill_level, time_zone, country):
#         self.name = name
#         self.email = email
#         self.discord_id = discord_id
#         self.skill_level = skill_level
#         self.time_zone = time_zone
#         self.country = country


# Come up with a whole taxonomy of Classes for 1MWTT

# class Diy_student():
#     def __init__(self, name, email, discord_id, donation_amount, skill_level, time_zone, country):
#         self.name = name
#         self.email = email
#         self.discord_id = discord_id
#         self.donation_amount = donation_amount
#         self.skill_level = skill_level
#         self.time_zone = time_zone
#         self.country = country
#
# class Vip_student():
#     def __init__(self, name, email, discord_id, skill_level, time_zone, country):
#         self.name = name
#         self.email = email
#         self.discord_id = discord_id
#         self.skill_level = skill_level
#         self.time_zone = time_zone
#         self.country = country
#
#
# class Gold_student():
#     def __init__(self, name, email, discord_id, skill_level, time_zone, country):
#         self.name = name
#         self.email = email
#         self.discord_id = discord_id
#         self.skill_level = skill_level
#         self.time_zone = time_zone
#         self.country = country
#
#
# class Volunteer():
#     def __init__(self, name, email, discord_id, time_zone, country, language ):
#         self.name = name
#         self.email = email
#         self.discord_id = discord_id
#         self.skill_level = skill_level
#         self.time_zone = time_zone
#         self.country = country
#         self.language = language
#
#
# class Mentor():
#     def __init__(self, name, email, discord_id, time_zone, country, language, availability):
#         self.name = name
#         self.email = email
#         self.discord_id = discord_id
#         self.skill_level = skill_level
#         self.time_zone = time_zone
#         self.country = country
#         self.availability = availability


# Day 3

print('')
print('***** DAY FOUR *****')
print('')

#
# Exercise #5 from http://www.nltk.org/book/ch01.html ☼ Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?
