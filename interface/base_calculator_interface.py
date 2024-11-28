from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def is_valid_operator(self, operator):
        pass

    @abstractmethod
    def calculate(self, num1, operator, num2):
        pass

    @abstractmethod
    def save_to_memory(self, result):
        pass

    @abstractmethod
    def add_to_history(self, num1, operator, num2, result):
        pass

    @abstractmethod
    def show_history(self):
        pass