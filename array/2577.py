import numpy as np;

A=int(input())
B=int(input())
C=int(input())

R=str(A*B*C)
Answer= np.zeros(10,int)

for i in R:
    i = int(i)
    for j in range (0,10):
        if i==j:
            Answer[j] +=1

for k in range (10) :
    print(Answer[k])
