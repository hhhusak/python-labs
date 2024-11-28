import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.base_calculator import BaseCalculator

class Calculator(BaseCalculator):
    def run(self):
        while True:
            num1, operator, num2 = self.get_input()
            
            if not self.is_valid_operator(operator):
                print("Невірний оператор. Спробуйте ще раз.")
                continue

            result = self.calculate(num1, operator, num2)
            self.save_to_memory(result)
            self.add_to_history(num1, operator, num2, result)

            print(f"Результат: {result}")
            self.show_history()

            another = input("Виконати ще одне обчислення? (y/n): ").lower()
            if another != 'y':
                print("Дякую за використання калькулятора!")
                break
