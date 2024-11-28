class ASCIIArt3DGenerator:
    def __init__(self):
        self.figure = None
        self.size = (10, 10)
        self.projection = []

    def set_figure(self, figure_name):
        if figure_name.lower() == 'cube':
            self.figure = self.generate_cube()
        elif figure_name.lower() == 'pyramid':
            self.figure = self.generate_pyramid()
        elif figure_name.lower() == 'sphere':
            self.figure = self.generate_sphere()
        else:
            print("Невідома фігура. Спробуйте 'cube', 'pyramid' або 'sphere'.")
            self.figure = None

    def generate_cube(self):
        size = self.size[0]
        # Базова проекція куба в ASCII
        return [["#" if x == 0 or x == size - 1 or y == 0 or y == size - 1 else " " for x in range(size)] for y in range(size)]

    def generate_pyramid(self):
        size = self.size[0]
        projection = []
        for i in range(size):
            row = [" "] * (size - i) + ["#"] * (2 * i + 1) + [" "] * (size - i)
            projection.append(row)
        return projection

    def generate_sphere(self):
        size = self.size[0]
        center = size // 2
        projection = []
        for y in range(size):
            row = []
            for x in range(size):
                distance = ((x - center) ** 2 + (y - center) ** 2) ** 0.5
                if distance < center:
                    row.append("#")
                else:
                    row.append(" ")
            projection.append(row)
        return projection

    def display_ascii_art(self):
        if not self.figure:
            print("Фігура не визначена.")
            return
        for row in self.figure:
            print("".join(row))

    def run(self):
        while True:
            user_input = input("Введіть фігуру для відображення (cube, pyramid, sphere) або 'exit' для виходу: ")
            if user_input.lower() == 'exit':
                break
            self.set_figure(user_input)
            self.display_ascii_art()