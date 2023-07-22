code = input('주민등록번호(14자리):')
if len(code)!= 14:
	print('주민등록번번호 자리수 입력 오류입니다.')
else:
    month = code[2:4]
    if month == "01" or month == "05" or month == "09" :
        print("당신은 월요일, 금요일, 토요일, 일요일에 운행 가능")
    elif month == "02" or month == "06" or month == "10" :
        print("당신은 화요일, 금요일, 토요일, 일요일에 운행 가능")
    elif month == "03" or month == "07" or month == "11" :
        print("당신은 수요일, 금요일, 토요일, 일요일에 운행 가능")
    elif month == "04" or month == "08" or month == "12" :
        print("당신은 목요일, 금요일, 토요일, 일요일에 운행 가능")
          
