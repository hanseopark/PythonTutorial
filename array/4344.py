C= int(input())

Sur=[]
for i in range (C):
    N = list(map(int,input().split()))
    Ave =0
    Count=0
    for j in range (1,len(N)):
        Ave +=N[j]
    Ave = Ave/(len(N)-1)
    for j in range (1,len(N)):
        if N[j]>Ave:
            Count +=1
    Sur.append(Count/(len(N)-1)*100)

for i in Sur:
    print('%.3f'%(i)+'%')
