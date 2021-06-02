N = int(input())

Num5kg = N//5
Num3kg = (N%5)//3

if N%15==0:
    print(N//5)
elif N%3==0:
    print(N//3)
elif 5*Num5kg+3*Num3kg!=N:
    print(-1)
else:
    print(Num5kg+Num3kg)
