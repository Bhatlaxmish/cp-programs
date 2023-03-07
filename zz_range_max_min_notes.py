import math

"""  range, isnumeric,
print backwords, max min """





#  isnumeric used to check numerical values
string = "3505353-rtir-258454358"
st = ""
for i in string:
    if not i.isnumeric():
        st = st+i
print(st)

# from 0 to 20 of every 3 number
for i in range(0, 20, 3):
    print(i, end='')

print()


# print backwords
for i in range(20, 0, -1):
    print(i, end='')

# searching
inlist = [4, 'w4', 223, 64]
search = 223
pos = None  # is a const equivalent to null
for i in range(len(inlist)):
    if (inlist[i] == search):
        pos = i
        break
print("it found at index", pos)

# or

if search in inlist:
    pos = inlist.index(search)
print("item found at ", pos)

fontiio = ["pero", "oritr", "aerotor"]
print(fontiio) 
# directly prints it
a = b = c = f = h = fontiio
# you can assign values directly

print(a)

fontiio.append("toere")
print(fontiio)

#max and min
arra = [4, 5, 2, 5, 1, 7]
print(max(arra))
print(min(arra))
print("aogoetoawn".count('o'))
print(len(arra))
print(arra)
print("ho")
