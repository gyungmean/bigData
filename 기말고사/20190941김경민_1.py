import numpy as np

def fun(score):
    name = score[0]
    sum = score[1] + score[2] + score[3]
    mid = round(np.mean([score[1], score[2], score[3]]),1)
    result = '불합격'
    if mid >= 80 :
        result = '합격'
    return (name, sum, mid, result)


score1=['김봄', 100, 90, 97]
score2=['오여름', 90, 98, 89]
score3=['나가을', 60, 70, 60]
score4=['이겨울', 90, 80, 91]

answer = []
answer.append(fun(score1))
answer.append(fun(score2))
answer.append(fun(score3))
answer.append(fun(score4))

print(answer)
print()

for a in answer:
    print(a)