
""" 
vector<pair
set of dict 
join split 
touples
string.center
dictionary
set
"""
# vector<pair<int,int>>v
x_values = [1, 3, 5]
y_values = [2, 4, 6]

vector = [(x, y) for x, y in zip(x_values, y_values)]


# create set of dictionary 
dictionaries = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 1, 'b': 2}]

# Create a set of dictionaries
# dictionary_set = set(dictionaries)

# print(dictionary_set)


# or  
dictionaries = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 1, 'b': 2}]

# Create a set of dictionaries
dictionary_set = {(d, d['a']) for d in dictionaries}

print(dictionary_set)


#printing set without bracket or , 
  print(" ".join(str(e) for e in s))
 
# you can import data from another file like lists, by

import hashlib
import this
from sdlfdkl import listingh
# here listingh is a name of the list in sdlfdkl file
data = [4, 5, 7, 3, 6, 3, 6, 7, 3, 6, 3, 67, 3, 6]
min = 4
MAX = 67
for i in range(len(data)):
    print(data[i])


# print backwords
for i in range(len(data) - 1, -1, -1):
    print(data[i], end=' ')
# prints in revesed order and index points from last i.e index 0 points to last element in list
for i, j in enumerate(reversed(data)):
    print(i, j)

# list of lists better to put , in end of list of list
lor = [["wr5234", "r434", "wert"], ["wr5234", "r434", "wert"], ["wr5234", "r434", "wert"], ["wr5234", "r434", "wert"],
       "wr5234",
       "r434", ["wert", "wr5234", "r434"], ["wert", "wr5234", "r434", "wert", "wr5234", "r434", "wert"], ]

print(lor)
for i in lor:
    for j in i:
        print(j)
# sep is a keyword used to separate value inside single print statement
print(4, 34, 245, "4fdsg", sep=", ")

llooa = ['t', 'y', 'u', 'f',
         "fdghf", "fglfdjl"
         ]
print(llooa)
# join method prints elements like normal text not like list
print(", ".join(llooa))

# here separator is a string .join is a string method that joins the llooa list string with separator in between
separator = " \ "
print(separator.join(llooa))

# split is a function that is used to separate the word or character which has one or more whilte spaces it stores in form of lists or
# you can also provide split parameter like , or | in " " quotes

sgh = "dlfds lsdfjds sdlfjds sadf sdf s sdf dsf sdf "
print(sgh.split())
lre = "dfgf|dfgfd,fdgdf|gdfg,rtr"
print(lre.split("|"))

ere = "".join(llooa)
print(ere)
sdfdsf = ere.split(" ")
print(sdfdsf)


# touples
inr = ("lfjdsf", "sdfjds", "sdf")
print(inr)
print(inr[1])  # in touples you cant change the values

# convert touples to list by using list function
print(list(inr))

eryrr = [("sdfds", "sdf", 4),
         ("sfes", "er", "erqt"),
         ("sf", "4645", "2342"),]
print(eryrr)
for i in eryrr:
    print(i)
# using no of variables to unpack the items in touple
for a, b, d in eryrr:
    print(a, b, d)


output = "wheaeere sderew tweoi"
screen_width = 80
# string.center function prints string at center of the width given
print("*{0}*".format(output.center(screen_width-4)))

wre = 5
if (wre > 7):
    # the raise keyword makes the program to print value as error if it wasnt satisfied
    raise ValueError("the value is greater")

# it displays the documentation or docstring means information about the function
print(input.__doc__)

# or use help
help(input)
# its a like escape sequence it specifies the RED means color some type means if you use it in print it will print the string in that color
RED = '\u001b[36m'
print(RED, "adsgfjreo")
# reset reset to default
RESET = '\u001b[0m'
print(RESET, "SDTER")

nu = (4, 5, 2, 65, 2, 4)
print(nu)
# *unpacks the values from it sep can be used to display with separator
print(*nu)
print(*nu, sep=";")


# *args is used to unpack the list or touple you can pass any no of args

def muto(*args):
    print(args)
    for i in args:
        print(i)


muto(3, 2, 54, 5, 2, 4)

# dictionary
eootewt = {"werew": "WEREW",
           "SA": "PUPOU",
           "wetr": "[ai[pi",
           "PIp": " woeqry",

           }

print(eootewt)
for i in eootewt:
    print(i, eootewt[i], sep=":")

# add item to dictionary
eootewt["gdserwt"] = "owqtrwqe[prw"
print(eootewt)

# deleting  a element
del eootewt["PIp"]
print(eootewt)
# or use pop method
eootewt.pop("SA")
print(eootewt)


# its a zen of python


# it means type of input and ->int is return type
def multiply(x: int, y: int) -> int:
    return x*y


print(multiply(4, 3))

print(f"wrwrpw")

# setdefault is a method which assigns values to the items if not present in dictionary
# else return value after running it adds the item to dictionary with default value where get method only returns
# value not adds to dictionary
id = eootewt.setdefault("wetwe", 0)
die = eootewt.setdefault("SA", 0)
print(die)
print(id)

pantry = ["dwaer", "asefr", "-r4e", "23-u4wfre"]
# from key method creates a dictionary of items in list and  assigns default values
# provided if not assigns None to it.
new = dict.fromkeys(pantry)
print(new)
new = dict.fromkeys(pantry, 9)
print(new)
# returns key values
keys = eootewt.keys()
print(keys)

rer = {
    "SA": "goej"
}
# to chage the values of keys in dictionary
eootewt.update(rer)
print(eootewt)

# finding values in dictionary with key correspond to it
kit = list(eootewt.keys())
values = list(eootewt.values())
print(values)
if "goej" in values:
    index = values.index("goej")
    key = kit[index]
    print(f"{eootewt[key]} was found with the key {key}")
else:
    print("not found")

# creats a list of strings empty can hold upto 10 values
woru = [""]*10
vawer = woru.copy()
# ewrf={
#     '1':"wrwe","wperwe"
#     '3':"qw2req","wperoew"
#    ' 5':"3r3","weruw"
#     '9':"q1w","werwe"
# }

# def sinp(s:str)->int:
#     basic_hash=ord(s[0])
#     return basic_hash%10
#

# for ke,val in ewrf:
#     h=sinp(val)
#     print(h)

# its a library in python for using hashfunction
py = """for isnre e9rw2rwfj wefrweo"""
print(py)
# it has .encode function which hashes the charachters
for v in py.encode('utf8'):
    print(v, chr(v))

# sets
# it also represented using flower brackets  order of elements are not unique it prints randomly
farm = {"coe", "weorj", "woejf", 'sfweo', "fweoi"}
print(farm)
for i in farm:
    print(i)


# create empty set\
nu = {*""}
print(type(nu))
# or
nu = {*{}}
print(nu)
# or more direct way is
nu = set()
nu.add(1)
print(nu)

# removing dublicates by putting values of list to sets
eijw = set(data)
print(eijw)
# while removeing dublicates along with want to retain order
# it outputs in form of list
wpe = list(dict.fromkeys(data))
print(wpe)

# deleting items
set = set(range(21))
print(set)
set.discard(3)  # it removes if exits
set.remove(5)  # if dosnt exist then creashes
print(set)
# it removes items from start
set.pop()
print(set)
# set union
setis = set.union(farm)
print(setis)

# or
setis = set | farm
print(setis)
