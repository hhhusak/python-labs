import re

class UserInputHandler:
    @staticmethod
    def get_user_choice():
        print("1. Показати пости")
        print("2. Показати коментарі")
        print("3. Вийти")
        choice = input("Введіть номер вибору: ")
        return choice

    @staticmethod
    def validate_input(input_value, pattern):
        return bool(re.match(pattern, input_value))
    
    