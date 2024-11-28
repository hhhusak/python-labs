import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("Дані успішно завантажено.")
        except FileNotFoundError:
            print(f"Файл {self.file_path} не знайдено.")
        except pd.errors.EmptyDataError:
            print("Файл порожній.")
        except Exception as e:
            print(f"Помилка при завантаженні даних: {e}")

    def get_data(self):
        return self.data