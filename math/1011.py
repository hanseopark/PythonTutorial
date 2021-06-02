T= int(input())
Count = []
for _ in range(T):
    x, y = map(int,input().split())
    dist = y-x
    if dist <3:
        Count.append(dist)
    else:
        for i in range (1,dist):
            if i*i<dist<=i*i+i:
                Count.append(2*i)
                break
            elif i*i+i<dist<=(i+1)*(i+1):
                Count.append(2*i+1)
                break
for k in Count:
    print(k)
