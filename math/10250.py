T = int(input())
for i in range(T):
    H,W,N=map(int,input().split())
    cW=1
    temp=0
    while(True):
        temp+=H
        print(temp)
        if temp>=N:
            break
        cW+=1
    X=str(cW)
    if len(X)==1:
        X = '0'+X
    Y=str(N-H*(cW-1))
    print(Y+X)
