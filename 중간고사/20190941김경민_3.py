def getBMI(h, w):
    h = h / 100
    result = w / (h * h)
    return result

def display(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    elif bmi < 30:
        return "경도비만"
    else :
        return "고도비만"

name = input('이름 입력:')
height = int(input('키(cm단위) 입력:'))
weight = int(input('몸무게(kg단위) 입력:'))
bmi = getBMI(height, weight)
result = display(bmi)

print(f"{name}, {bmi}, {result}")
