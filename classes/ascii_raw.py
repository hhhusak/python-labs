from config.base_font import LETTERS_MAP

class ASCIIArtGenerator:
    def __init__(self):
        self.text = ""
        self.height = 7
        self.width = 5
        self.alignment = "center"
        self.symbol = "#"

    def get_user_input(self):
        self.text = input("Введіть текст для ASCII-арту: ").upper()
        
        self.symbol = input("Введіть символ для створення ASCII-арту (наприклад, @, #, *): ") or "#"
        
        self.alignment = input("Виберіть вирівнювання (left, center, right): ").strip().lower() or "center"

    def generate_ascii_letter(self, letter):
        ascii_art = LETTERS_MAP.get(letter, [" " * self.width] * self.height)
        return [line.replace("#", self.symbol) for line in ascii_art]

    def generate_ascii_art(self):
        ascii_art = []
        
        for row in range(self.height):
            row_text = ""
            for letter in self.text:
                letter_art = self.generate_ascii_letter(letter)
                row_text += letter_art[row] + " "
            aligned_row = self._align_text(row_text)
            ascii_art.append(aligned_row)
        
        return "\n".join(ascii_art)

    def _align_text(self, row_text):
        if self.alignment == "center":
            return row_text.center(len(self.text) * (self.width + 1))
        elif self.alignment == "right":
            return row_text.rjust(len(self.text) * (self.width + 1))
        return row_text.ljust(len(self.text) * (self.width + 1))

    def display_ascii_art(self, art):
        print("\nВаш ASCII-арт:\n")
        print(art)

    def run(self):
        print("ASCII Art Generator")
        self.get_user_input()
        art = self.generate_ascii_art()
        self.display_ascii_art(art)