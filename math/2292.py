N = int(input())

Point =0
for i in range (N):
    N = N-6*i
    if N <= 6*(i+1)+1:
        Point = i+2
        break
print(Point)
