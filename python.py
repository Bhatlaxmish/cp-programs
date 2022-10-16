from traceback import print_list
# import itertools

# string output methods
print("what is that")
# using backslash(\) to escape end of the line
print("what is that \"its not corrext\".'nooot' ")

# to use \ in strig use \\
print("c:home\\projects\\myproject")



# printing character in string
# negative index prints from last
parrot="hoherthag afdjsdofjosdf"
print(parrot[-1])

# prints part of string

print(parrot[0:6])
print(parrot[2:-12])
print(parrot[0:9:3])#it print s string form 0 to 9 every 3 steps jump i.e. parrot[0],[3][6] not 9th 

print(parrot[0::3])#it dont have end point runs upto endpoint
seperators=parrot[1::3]

print(seperators)


# reverse a string 
def revere(parrot):
   tor="".join(reversed(parrot))
   return tor

print(revere(parrot))

# or
st=parrot[::-1]
print(st)

print("ehesL "*4)#prints 4 times 

print("o" in parrot)#checks whether it exits or not

#converting int to string using str() function
age=23
print("agae is "+str(age))
# using format to print witout converting into string
print("age is {0}".format(age))

print("how are a{0:3}\n not easy {1:4}".format(3,6967))#{0:3}tells space for that (3)
print("how are a{0:<3}\n not easy {1:<4}".format(3,6967))#{0:3}tells space for that (3)from starting use {0:^3}for display in center

print("po is {0:12}".format(22/7))
print("po is {0:12f}".format(22/7))
print("po is {0:12.40f}".format(22/7))
print("po is {0:12.40}".format(22/7))
print("po is {0:12}".format(22/7))




array={"what ","where","how","now"};
another={"now","notnow","why","no"};
for array ,another in zip(array, another):
    print('{0} {1}'.format(array,another))
    
cars=[2,6,"yut"]
for i in cars:
    print(i)  
    
    
# using len for iteration
for i in range(len(cars)):
   print(cars[i])  
   
            
    # using dictionnary
d={"what":"are","now":"notnow"};
for i ,j in d.items():
    print(i,j)
     
    
    
    # using sorted to sort it doesnot sort list but prints as sorted ,(end='') is used to display in line and space as " " or ''; 
ls=[3,5,2,6]
for i in sorted(ls):
   print(i,end=' ') 
print()
   
    # if you want to print without dublicate use 
    # i in sorted(set(ls))
    # use  i in reversed(ls) for reverse printing
    # use below to print 2 to 4
for i in range(1,5):
    print(i,end='') 
print()

# itertools is a headerfile used as iteratortools.count or iteratortools.cycle(used to print again and again after end of loop like cycle) or repeat(value,no-oftimes)
import itertools

# for in loop
for i in itertools.count(5, 5):	
    if i==30:
       break
    print(i, end =" ")

print()
# using iter it generates iterators for list in while loop use True not true here __next__() moves pointer to next elemnt
listing=[53,6,7,9,3,5]
itw=iter(listing)
while True:
     try:
            print(itw.__next__())
     except:
         break;  
     
# printing possible permutations
from itertools import permutations

for i in itertools.permutations(["gs","for","eks"],3):
    print(i)

# printing possible combinations
from itertools import combinations
for i in itertools.combinations(["ab","df","as"],2):
    print(i)   
    
    #or you can directly use as 
print(list(combinations([3,4,6,2],2))) 
    
# using islice(list name,staring pos,ending pos,i=i+jump i.e increment)
tor=[4,3,6,2,6,2,4,2,5,2]
for i in itertools.islice(tor,2,8,2):
    print(i)


# using starmap(function,list) prints min in every list of lists
lew=[(4,5,2),(2,5,1),(6,5,3)]
for i in itertools.starmap(min,lew):
    print(i,end='')
    
# greater comparison can be easily done by
print(2<5<7)
print(4<9>2)



# cant use  for in range cant pass name of list pass whole list
def function( lsse):
    for i in  lsse:
      print(i)   
function([4,6,2,7])




def callingfunction(): 
    for i in range(1,8):
       print(i,end='')
callingfunction()

def create(**args):
  for key,value in args.items():  
    print("%s==%s"%(key,value))

create(first='Geeks', mid='for', last='Geeks')

# print upto 3 precesion
r=45.44567
print('%.3f'%r) 
print(round(r,3))
       
       
       
       #searhing an element in str or array
       
peogen="what are the use of that "
if('a'in peogen):
    print("it is in it")
else:
    print("it is not there")    
#use not in 
if('e' not in peogen):
    print("good to go")
    
