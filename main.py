def calculate(expression):
    result = 0
    current_number = 0
    operator = '+'

    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in '+-*/':
            if operator == '+':
                result += current_number
            elif operator == '-':
                result -= current_number
            elif operator == '*':
                result *= current_number
            elif operator == '/':
                result / current_number
            operator = char
            current_number = 0

    if operator == '+':
        result += current_number
    elif operator == '-':
        result -= current_number
    elif operator == '*':
        result *= current_number
    elif operator == '-':
        result /= current_number

    print(result)
if __name__ == '__main__':
    _expression = input()
    calculate(_expression)