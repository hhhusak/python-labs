import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.lab9_class import RunnerFacade

def runner():
    runner = RunnerFacade()
    while True:
        print("\n--- Меню ---")
        print("1) Запустити програму 1")
        print("2) Запустити програму 2")
        print("3) Запустити програму 3")
        print("4) Запустити програму 4")
        print("5) Запустити програму 5")
        print("6) Запустити програму 6")
        print("7) Запустити програму 7")
        print("0) Вийти")
        
        choice = input("Оберіть пункт меню: ")
        if choice == "0":
            print("Ви вийшли!")
            break
        else:
            runner.run_program(choice)

if __name__ == "__main__":
    runner()