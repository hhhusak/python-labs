import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.calculator import Calculator
from functions.ascii_functions import main
from classes.ascii_raw import ASCIIArtGenerator
from functions.ascii_3d_functions import ASCIIArt3DGenerator
from tests.calculator_test import TestCalculatorFunctions
from api.app.app import ApiApp
from classes.csv_visualizer_app import App

calc = Calculator()
asciiArtGenerator = ASCIIArtGenerator()
asciiArt3DGenerator = ASCIIArt3DGenerator()
testCalculatorFunctions = TestCalculatorFunctions()
apiApp = ApiApp()
csvVisualizer = App('../assets/data.csv')

class RunnerFacade:
    def __init__(self):
        self.programs = {
            "1": Calculator(),
            "2": main,
            "3": ASCIIArtGenerator(),
            "4": ASCIIArt3DGenerator(),
            "5": TestCalculatorFunctions(),
            "6": ApiApp(),
            "7": csvVisualizer,
        }

    def run_program(self, program_number):
        program = self.programs.get(program_number)
        if program:
            program.run()
        else:
            print("Невірний вибір. Спробуйте ще раз.")
