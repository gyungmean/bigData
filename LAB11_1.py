import calculator
expression = input("사칙연산 프로그램: ")
operators = ['+', '-', '*', '/']

for operator in operators:
    if operator in expression:
        operands = expression.split(operator)
        a = int(operands[0])
        b = int(operands[1])

        if operator == '+':
            result = calculator.sum_func(a, b)
        elif operator == '-':
            result = calculator.minus_func(a, b)
        elif operator == '*':
            result = calculator.multiply_func(a, b)
        elif operator == '/':
            result = calculator.divide_func(a, b)
        else:
            result = None

        if result is not None:
            print(f"실행 결과는 {result}")
        break
