N = int(input())
Count =0
for i in range (N):
    comp = False
    S = str(input())
    if len(S) == 1 or len(S) == 2:
        Count +=1
    elif len(S)>2:
        for j in range(2,len(S)):
            for t in S[j:]:
                if S[j-2] == t:
                    comp = True
        if comp == False:
            Count +=1
print(Count)
