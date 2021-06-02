H,M=map(int,input().split())

if M-45>=0:
    M=M-45
    print(H,M)
elif H!=0:
    H=H-1
    M=60-M
    print(H,M)
else:
    H=23
    M=60-M
    print(H,M)
