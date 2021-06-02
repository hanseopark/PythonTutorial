A,B,C = map(int,input().split())
Point =0
if B>C:
    Point = -1
else:
    i = A//(C-B)
    while(True):
        print(i)
        if A+B*i<C*i:
            Point = i
            break
        else:
            i +=1
print(Point)
