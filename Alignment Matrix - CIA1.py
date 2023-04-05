import random
import numpy as np

#Equal Distribution
str1="ACGT"
a1=""
a2=""
for i in range (4):
    a1 += ''.join(random.sample(str1,4))
    a2 += ''.join(random.sample(str1,4))
print(a1,'\n',a2)


l1=list(a1)
l2=list(a2)

print(l1)
print(l2)

m=np.zeros([17,17])
 
#Adding Values  
for i in range(16):
    for j in range(16):
        if(l1[i]==l2[j]):
            m[i+1][j+1]=m[i][j]+5
        else:
            v=max(m[i][j],m[i+1][j],m[i][j+1])
            m[i+1][j+1]=v-4

for i in range(17):
    for j in range(17):
        print(m[i][j])
      
#Finding Max value       
def maxim(m):
    b=0
    for i in range(17):
        for j in range(17):
            if(m[i][j]>b):
                b=m[i][j]
                maxrow=i
                maxcol=j
    return b,maxrow,maxcol

n,maxrow,malcol=maxim(m)

#Backtracking
def backtrack(n, c, maxrow, maxcol, a, b):
    
    if(n<0):
         return 
    else:
        print(c[maxrow][maxcol]," ")
        if(a[maxrow-1]==b[maxcol-1]):
            return backtrack(n-1,c,maxrow-1,maxcol-1,a,b)
        
        else: 
            if(c[maxrow-1][maxcol-1]>c[maxrow-1][maxcol] and c[maxrow-1][maxcol-1]>c[maxrow][maxcol-1]):
                return backtrack(n-1,c,maxrow-1,maxcol-1,a,b)

            elif(c[maxrow-1][maxcol]>c[maxrow-1][maxcol-1] and c[maxrow-1][maxcol]>c[maxrow][maxcol-1]):
                return backtrack(n-1,c,maxrow-1,maxcol,a,b)
            
            else:
                return backtrack(n-1,c,maxrow,maxcol-1,a,b)
            
backtrack(16,m,maxrow,malcol,l1,l2)