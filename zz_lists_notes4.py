
listingh = ["adslg", 5, 4, 2, "afdg"]
print(len(listingh))
# enumerate has two variables first one index second one value or element
for a, b in enumerate(listingh):
    print("{0}:{1}".format(a+1, b))

empty = []
for i in range(1, len(listingh)+1):
    empty.append(str(i))
print(empty)
empty.remove('5')  # delelting an element from list
print(empty)
empty.extend(listingh)  # merging two lists
# or
number = empty+listingh
print(empty)
loe = [1, 3, 4, 6, 3, 5, 6]
loe.sort()  # sorting a list
print(loe)
# sorting desending order
loe.sort(reverse=True)

#sorting copied list without affection original list 
new_list = loe[:]#copying 
new_list.sort()
print(new_list)
print(loe)

print(loe)
loert = loe
print(loert)
# another function that sorts is  sorting
# it considers white spaces also it doesnt affect original list
ty = "dgFdg ytr sdfgfsd ert sdg s"
print(sorted(ty))
# if you want to sort with some rules like uppercase or lowercase in this case
print(sorted(ty, key=str.casefold))

strinjg = "ldfofgsgsg"
inyt = list(strinjg)  # list function converts them into a list
print(inyt)

print(inyt is empty)  # is checks the two are equal return boolin values
# if you want to replace from a range
lsit = [4, 5, 7, 7, 4, 2]
total = sum(list) #sum of all elements in list 

# lsit[2:]=[4]
# print(lsit)
# deleting an element in list
del lsit[0:2]  # deletes in range 0 to 2
print(lsit)
