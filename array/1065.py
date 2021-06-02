def function(x):
    temp = str(x)
    if len(temp) == 1 or len(temp) == 2:
        return True
    for i in range (len(temp)-2):
        if (int(temp[i+2])-int(temp[i+1]) == int(temp[i+1])-int(temp[i])):
            return True
        else :
            return False

N = int(input())
Count=0

for i in range (1,N+1):
    if function(i)==True:
        Count+=1
print(Count)
