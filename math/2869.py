A,B,V = map(int,input().split())
i=V//(A-B)-A
pos = (A-B)*i
while(True):
    print(i,pos)
    pos += A
    if pos>=V:
        print(i+1)
        break
    pos -= B
    i+=1

