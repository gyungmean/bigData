import random

words = []
line_counter = 0
with open('output.txt', 'r', encoding='utf-8') as file:
    while 1:
        word = file.readline()
        if not word:break
        if line_counter == 0:
            line_counter += 1
            continue
        else:
            data = word.split(",")
            words.append(data[0])

result = words[random.randint(0, len(words))]
check = 0

answer = "#" * len(result)
print(answer)
for i in range(0, len(result)):
    inp = input("단어 중 한 글자를 말하시오:")
    for c in range(0, len(result)):
        if inp == result[c]:
            answer = answer[:c] + inp + answer[c+1:]
            check += 1
    print(answer)
    if check == len(result):
        break

if check == len(result):
    print("!!성공입니다.!!")
else:
    print("!!실패하였습니다.!!")


