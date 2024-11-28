import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.csv_data_loader import DataLoader
from classes.csv_data_analyzer import DataAnalyzer
from classes.csv_data_visualizer import DataVisualizer

class App:
    def __init__(self, file_path):
        self.data_loader = DataLoader(file_path)

    def run(self):
        self.data_loader.load_data()
        data = self.data_loader.get_data()

        if data is not None:
            DataAnalyzer.find_extremes(data)
            visualizer = DataVisualizer(data)

            # Лінійний графік
            x_column = input("Введіть стовпчик для осі X (наприклад, 'Date'): ")
            y_column = input("Введіть стовпчик для осі Y (наприклад, 'Value'): ")
            visualizer.plot_line_chart(x_column, y_column)

            # Стовпчиковий графік
            visualizer.plot_bar_chart(x_column, y_column)

            # Діаграма розсіювання
            visualizer.plot_scatter_chart(x_column, y_column)

            # Кілька піддіаграм
            visualizer.create_subplots([(x_column, y_column)])

            # Збереження візуалізації
            file_name = input("Введіть ім'я файлу для збереження (наприклад, 'visualization.png'): ")
            visualizer.save_visualization(file_name)