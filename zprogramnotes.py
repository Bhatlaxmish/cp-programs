
# 784 div 4 g fall down
l = list(map(int, input().split()))
di = dict()
for i in range(len(l)):
    if l[i] in di:
        di[l[i]] += 1
    else:
        di[l[i]] = 1
print(di)
for i in range(int(input())):
    a,b=map(int,input().split())
    ty=list()
    for j in range(a):
        s=input()
      
        ty.append(s)
        # check all elements in list are equal
    if (all(ele == ty[0] for ele in ty)):
        print("yes")
    for j in range(b):
        gh=list()
        # reverse the list
        gh.sort(reverse=True)
        for k in range(a-2,-1,-1):
            
            # print(ty[k][j],end='')
            if(ty[k][j]=='.'):
                gh.append(k)
            if(ty[k][j]=='o'):
                gh.clear()
            if(ty[k][j]=='*'):
                u="*"
                ty[gh[0]][j]=u
                gh.remove(gh[0])
                ty[k][j]='.'
        print()
    for j in range(a):
        for k in range(b):
            print(ty[i][k],end='')
        print()     
            
           
             
                