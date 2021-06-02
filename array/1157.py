S = str(input().upper())

A = []
for i in set(S):
    A.append(S.count(i))

idx = []
for i,v in enumerate(A):
    if v == max(A):
        idx.append(i)

if len(idx)>1:
    print('?')
else:
    print(list(set(S))[A.index(max(A))])


