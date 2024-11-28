import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_line_chart(self, x_column, y_column):
        plt.figure(figsize=(8, 6))
        plt.plot(self.data[x_column], self.data[y_column], marker='o', linestyle='-', color='blue')
        plt.title(f"Лінійний графік: {y_column} відносно {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
        plt.show()

    def plot_bar_chart(self, x_column, y_column):
        plt.figure(figsize=(8, 6))
        plt.bar(self.data[x_column], self.data[y_column], color='green')
        plt.title(f"Стовпчиковий графік: {y_column} відносно {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.xticks(rotation=45)
        plt.show()

    def plot_scatter_chart(self, x_column, y_column):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.data[x_column], self.data[y_column], color='red')
        plt.title(f"Діаграма розсіювання: {y_column} відносно {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
        plt.show()

    def create_subplots(self, plots):
        # Перевіряємо кількість піддіаграм
        fig, axes = plt.subplots(1, len(plots), figsize=(16, 6))

        # Якщо одна піддіаграма, обертаємо її у список
        if len(plots) == 1:
            axes = [axes]

        for ax, (x_column, y_column) in zip(axes, plots):
            ax.plot(self.data[x_column], self.data[y_column], marker='o', linestyle='-', color='blue')
            ax.set_title(f"{y_column} відносно {x_column}")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
        plt.tight_layout()
        plt.show()

    def save_visualization(self, file_name):
        plt.savefig(file_name, format='png')
        print(f"Візуалізацію збережено у файл {file_name}.")
        plt.close()