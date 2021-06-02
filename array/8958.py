N=int(input())

for i in range (N):
    Score=0
    BonusScore=0
    A=input()
    A=A+'X'
    temp = []
    for j in A:
        if j == 'O':
            Score +=1
            temp.append(j)
        else :
            for k in range (len(temp)):
                BonusScore+=k
                temp.clear()
    print(Score+BonusScore)
