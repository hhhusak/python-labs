import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.calculator_functions import get_user_input, is_valid_operator, perform_calculation
from interface.base_calculator_interface import ICalculator

class BaseCalculator(ICalculator):
    def __init__(self):
        self._memory = None
        self._history = []

    def get_input(self):
        return get_user_input()

    def is_valid_operator(self, operator):
        return is_valid_operator(operator)

    def calculate(self, num1, operator, num2):
        return perform_calculation(num1, operator, num2)

    def save_to_memory(self, result):
        self._memory = result

    def add_to_history(self, num1, operator, num2, result):
        self._history.append(f"{num1} {operator} {num2} = {result}")

    def show_history(self):
        print("\nІсторія обчислень:")
        for record in self._history:
            print(record)
