import math

def get_user_input():
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, %, sqrt): ")
        if operator != 'sqrt':
            num2 = float(input("Введіть друге число: "))
        else:
            num2 = None
        return num1, operator, num2
    except ValueError:
        print("Помилка! Введіть правильне число.")
        return get_user_input()

def is_valid_operator(operator):
    if operator in ['+', '-', '*', '/', '^', '%', 'sqrt']:
        return True
    else:
        print("Помилка! Невірний оператор.")
        return False

def perform_calculation(num1, operator, num2=None):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Помилка! Ділення на нуль."
            return num1 / num2
        elif operator == '^':
            return num1 ** num2
        elif operator == '%':
            return num1 % num2
        elif operator == 'sqrt':
            return math.sqrt(num1)
    except Exception as e:
        return f"Помилка обчислення: {str(e)}"
