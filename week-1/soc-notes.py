# Day 2
print (' ')

print ('moo'*3)

print ('Hello, World!')
# person = input("What's your name? ")
# print ('Hello,' + person )
print ('23' * 3)
print (' ')

# Day 3

name = 'Sara Carbaugh'
i = 1
result = " "

for i in range(0,len(name)):
    print(name[i])

for i in range(0, len(name)):
    if i % 2 == 0:
        print(name[i])
        result = result + name[i]
        print ('result just changed to: ' + result)

# str() method
hours = str(365.25*24.0)
print ('There are ' + hours + ' in a year.')
