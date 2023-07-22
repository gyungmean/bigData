import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import numpy as np

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

data = [['자두', 150, 45], ['짱구', 130, 28], ['유리', 125, 30], ['맹구', 140, 48], ['철수', 140, 35]]
idx = [0, 1, 2, 3, 4]
col = ['이름', '키', '몸무게']
df = pd.DataFrame(data, index=idx, columns=col)
print(df)
print('-'*25)

df['BMI'] = round(df['몸무게'] / ((df['키'] / 100) * (df['키'] / 100)), 2)
tmp = []
for b in df['BMI']:
    if b < 18:
        tmp.append('저체중')
    elif 18 <= b < 23:
        tmp.append('정상')
    elif 23 <= b < 25:
        tmp.append('과체중')
    elif 25 <= b < 30:
        tmp.append('비만')
    elif 30 <= b:
        tmp.append('고도비만')
df['비만도'] = tmp
print(df)

print('<<BMI 지수가 최소인 사람>>')
min_bmi = df['BMI'].min()
min_bmi_rows = df[df['BMI'] == min_bmi]
print(min_bmi_rows[['이름', 'BMI']])

print('<<비만도를 기준으로 그룹핑한 결과>>')
datas = df.groupby('비만도')['BMI'].mean()
print(datas)

print('<<비만도별 사람 수>>')
print(df.groupby('비만도')['이름'].nunique())

# 그래프 그리기
x = df['BMI']
y = np.arange(len(df['이름']))
labels = df['이름']

plt.plot(x)
plt.xticks(y, labels)
plt.xlabel("이름")
plt.ylabel("BMI")
plt.title("체질량지수")
plt.legend()
plt.show()

