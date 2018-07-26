
# Dictionarys are a built in data-type

# creating a dictionary using a constructor

# anne_niekrenz = dict(name = "Anne Niekrenz", dicord_id = "anne", fav_food = "ice cream")
#
# # creating a dictionary with notation{}
#
# my_dict = {
#     "a": 35000,
#     "b": 8000,
#     "z": 450
# }
#
# print(my_dict)
#
#
#
# #working with dictionary items
#
# # accessing
#
# my_dict["a"]  # accesses the "a" item
#
# # add
#
# my_dict["c"] = 250
#
#
# # modify
#
# my_dict["a"] = 50
#
# # delete items
#
# del(my_dict["a"])
#
#
# # delete dictionary
#
# del(my_dict)



# Classes

# class Student():
#     discord_id = "virginia [Gold] [Volunteer]" #hard-coded - NOT GOOD
#
# # instantiate (using our shiny new Constructor fuction that we got for free from the Class)
# s1 = Student()
#
# # dot notation
# print(s1.discord_id)


class Student():
    def __init__(self, name, discord_id, fav_food, dream ): # adds fuctionality
        self.name = name
        self.discord_id = discord_id
        self.fav_food = fav_food
        self.dream = dream

    def my_print(self): # method instead of a fuction because it siting inside of an object
        print(self.name + self.discord_id + self.fav_food + self.dream)

# instantiate (using our shiny new Constructor fuction that we got for free from the Class)
s1 = Student("Virginia Balseiro ", "yesvirginia [Gold] [Volunteer] ", "pasta ", "moving to Europe")
s2 = Student("Andreea Visanoiu ", "Andreea[Gold] ", "wontonmee ", "becoming a University teacher")
s3 = Student("Cristy Tarantino ", "CristyTarantino[Gold] ", "pasta ", "being an amazing developer")

# dot notation
s1.my_print()
s2.my_print()
s3.my_print()

# modify properties

si.fav_food ="ice cream"
s1.my_print()

# delete properties

del s1.fav_food
s1.my_print()
# this will error out because my_print is still looking for fav_food and it's not There
