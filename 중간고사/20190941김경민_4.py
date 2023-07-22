import random

scores = []
for i in range(1, 10):
    score = random.randint(10, 100)
    if score % 10 != 0:
        score = int(score / 10) * 10
    scores.append(score)

print("<생성된 점수 리스트>")
print(scores)
print("<딕셔너리를 이용한 정보 조회>")
print("-" * 50)

dic = {}
dic.clear()
for s in scores:
    dic[s] = 0
for s in scores:
    dic[s] = dic[s] + 1

print("점수별 학생수 출력:", dic)
max_score = -1
for k in dic.keys():
    if k > max_score:
        max_score = k
print(f"최고 점수와 학생 수 : {max_score}점 --> {dic[max_score]}명")

count = -1
for k in dic.keys():
    if count < dic[k]:
        count = dic[k]
for k in dic.keys():
    if dic[k] == count:
        print(f"동점이 가장 많은 점수와 학생 수 : {k}점 --> {dic[k]}명")
        
print("-" * 50)

check = int(input("학생수를 확인하고 싶은 점수 입력:"))
noKey = True
for k in dic.keys():
    if k == check:
        print(f"점수에 해당하는 학생수는 {dic[check]}명이다.")
        noKey = False

if noKey == True:
    print("점수에 해당하는 학생수는 0명이다.")
        
