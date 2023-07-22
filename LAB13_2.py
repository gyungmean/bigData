import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 학생의 이름, 중간고사 점수, 기말고사 점수 입력 받기
students = []
for i in range(3):
    name = input("이름 입력: ")
    midterm = float(input("중간 점수 입력: "))
    final = float(input("기말 점수 입력: "))
    students.append((name, midterm, final))

# 학생별 평균 계산
averages = []
for student in students:
    name, midterm, final = student
    average = np.mean([midterm, final])
    averages.append(average)

# 그래프 그리기
x = np.arange(len(students))
labels = [student[0] for student in students]

plt.plot(x, [student[1] for student in students], label="중간고사")
plt.plot(x, [student[2] for student in students], label="기말고사")
plt.plot(x, averages, label="평균 점수")
plt.xticks(x, labels)
plt.xlabel("이름")
plt.ylabel("점수")
plt.title("이름별 점수")
plt.legend()
plt.show()

