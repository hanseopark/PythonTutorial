MAX=0
MIN=100
for i in range(0,9):
    temp = int(input())
    if (temp>MAX):
        MAX=temp
    if (temp<MIN):
        MIN=temp
print(MAX)
print(MIN)
