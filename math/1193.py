X = int(input())
if X == 1:
    print('1/1')
else:
    for i in range (X):
        X = X-i
        if X <= i+1:
            a = str(i+1-(i+1-X))
            b = str(1+i+1-X)
            print(a+'/'+b)
            break



