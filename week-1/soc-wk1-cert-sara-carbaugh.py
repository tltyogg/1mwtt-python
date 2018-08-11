# # Day 1
# print (' ')
# print ('***** DAY ONE *****')
# print (' ')
#
# # 1 - Hours in a year. How many hours are in a year?
#
# hours = 365.25*24.0
# print ('There are {} in a year.'.format(hours))
# print (' ')
#
# # 2 -  Minutes in a decade. How many minutes are in a decade?
#
# minutes = 365.25*24*10*60
# print ('There are {} in a decade'.format(minutes))
# print (' ')
#
# # 3 - Your age is seconds. How many seconds old are you?
#
# age = ((365.25*24*60*36)*60)+(13*24*60*60)
# print ('I am {} seconds old!'.format(age))
# print (' ')
#
#
# # 4 - Calculate @Andreea Visanoiu's age. She is 48618000 seconds old.
#
# andreea = (486180000/(365.25*24*60*60))
# print ('Andreea is {} years old.'.format(andreea))
# print (' ')
#
# # How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# # Under the assumption that we have a system that increases by 1 every milisecond)
#
# timeout_32 = (2**31)/.001*60*24*364.25
# print ('A 32-bit system with time out in {} days.'.format(timeout_32))
# print (' ')
#
# # How about a 64-bit system?
#
# timeout_64 = ((2**63)/.001*60*24*364.25)
# print ('A 64-bit system will timeout in {} days.'.format(timeout_64))
# print (' ')
# print (' ')
#
#
# # Day 3
# print (' ')
# print ('***** DAY THREE *****')
# print (' ')
#
#
# # Full name greeting
# # f_name = input("What is your first name? ")
# # m_name = input("What is your middle name? ")
# # l_name = input("What is your last name? ")
# # full_name = f_name +(' ')+ m_name +(' ')+ l_name
# # print ('Howdy, ' + full_name + '!!')
# # print (' ')
#
#
# # Bigger, better favorite number
# # fav_number = input('What is your favorite number? ')
# # bigger = int(fav_number) + 1
# # print ('I think you meant to say ' + str(bigger) + '! ;) ')
# # print (' ')
#
#
# # Angry Boss
# # want = input("What do YOU want?! ")
# # print ('WHADDAYA MEAN \"' + want + '\"?!? YOU\'RE FIRED!!')
# # print (' ')
#
#
# # Table of contents
#
# # print ('Table of Contents'.center(50), "\n")
# # print (('Chapter 1'.ljust(15)) + ('Getting Started'.center(20)) + ('page 1'.rjust(15)))
# # print (('Chapter 2'.ljust(15)) + ('Numbers'.center(20)) + ('page 9'.rjust(15)))
# # print (('Chapter 3'.ljust(15)) + ('Letters'.center(20)) + ('page 13'.rjust(15)))
# # print (' ')
#
#
# # Random number generator
# # import random
# # for x in range(1):
# #     print (random.randint(1,10))
# # print (' ')
#
# # Generating a map for Civilization III
# # items = ['X', 'o', 'X', 'o', 'X', 'o', 'X', 'o', 'X', 'o', 'X']
# # array = len(items)
# # while array >= 11:
# #     print (random.sample(items, 11))
# # else:
# #     print ('Map Complete!')
# # print (' ')
#
# # Day 4
#
# print (' ')
# print ('***** DAY FOUR *****')
# print (' ')
#
# # “99 Bottles of Beer on the Wall.”
#
# for x in range(100, 0, -1):
#     if x >= 0:
#         print ( str(x) + " bottles of beer on the Wall! " + str(x) + " bottles of beer! Take one down, pass it around, ")
#         x = x-1
#         print ( str(x) + " bottles of beer on the wall!")
# print ("No more bottles of beer on the wall. No more bottles of beer. Go to the store and buy some more, ")
# print ("99 bottles of beer on the wall!")
# # print (' ')

# Deaf Grandma and Deaf grandma extended
# import random
#
# greeting = input("Talk to Grandma : ")
# grandma = True
# count = 0
#
# while grandma == True:
#     if greeting.islower() or greeting.istitle():
#         print ("HUH?! SPEAK UP, GIRL!")
#         count = 0
#         print (' ')
#         greeting = input("Talk to Grandma : ")
#     if greeting.isupper() and "BYE" not in greeting:
#         # for x in range(1):
#         print ("NO, NOT SINCE " + str(random.randint(1900,1940)) + "!")
#         count = 0
#         print (' ')
#         greeting = input("Talk to Grandma : ")
#     if greeting == "":
#         print ("HUH?! SPEAK UP, GIRL!")
#         count = 0
#         print (' ')
#         greeting = input("Talk to Grandma : ")
#     if greeting == "BYE":
#         print ("NO, NOT SINCE " + str(random.randint(1900,1940)) + "!")
#         print (' ')
#         count+=1
#         if count == 3:
#             print ("SEE YA!")
#             grandma = False
#         else :
#             greeting = input("Talk to Grandma : ")




# Leap years

# first_year = input("Enter your first year: ")
# second_year = input("Enter your second year: ")


# Find something today in your life, that is a calculation



# Building and sorting an array

# word_list = []
#
# word = input("Please enter a word: ")
#
# while word != "" :
#     word_list.append(word)
#     word = input("Please enter a word: ")
#     if word == "":
#         print (sorted(word_list))




# Table of contents revisited
# print('')
# table = {1: {'chapter':'1', 'title': 'The Boy Who Lived', 'page': '1'},
#          2: {'chapter':'2', 'title': 'The Vanishing Glass', 'page': '18'},
#          3: {'chapter':'3', 'title': 'The Letters from No One', 'page': '31'}}
#
# print('Table of Contents'.center(60))
# print('')
# print('Chapter ' + (table[1]['chapter'].ljust(15)) + (table[1]['title'].center(30)) + (table[1]['page'].rjust(15)))
# print('Chapter ' + (table[2]['chapter'].ljust(15)) + (table[2]['title'].center(30)) + (table[2]['page'].rjust(15)))
# print('Chapter ' + (table[3]['chapter'].ljust(15)) + (table[3]['title'].center(30)) + (table[3]['page'].rjust(15)))
#
# print('')

# Write a function that prints out "moo" n times

# def moo(n):
#     print("moo " * n)
#
# moo(4)

# Old-school Roman numerals


# “Modern” Roman numerals

import math

d=0
while ((d > 3000) or (d==0)):
    d=int(input("Enter a number between 1-3000 :"))

rn = ""

decimal=[1000, 500, 100,50,10,5,1]
roman=["M", "D", "C", "L", "X", "V", "I"]
i=0
for n in decimal:
    if (d==9):
        rn=rn+"IX"
        break
    if (d==4):
        rn=rn+"IV"
        break
    q = math.floor(d/n)
    r= d % n
    rn=rn+ (q*roman[i])
    d=r
    i=i+1

print(rn)
