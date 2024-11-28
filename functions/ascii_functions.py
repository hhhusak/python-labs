import pyfiglet
import termcolor
from colorama import init

init()

COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

def display_fonts():
    """Показує доступні шрифти користувачу."""
    fonts = pyfiglet.FigletFont.getFonts()
    print("Available fonts:")
    for i, font in enumerate(fonts[:10]):
        print(f"{i + 1}. {font}")
    return fonts

def get_user_input():
    text = input("Enter the text you want to convert to ASCII art: ")
    fonts = display_fonts()
    font_choice = int(input("Choose a font (enter number): ")) - 1
    font = fonts[font_choice] if 0 <= font_choice < len(fonts) else "standard"
    
    color = input(f"Choose a color {COLORS}: ").lower()
    if color not in COLORS:
        print("Invalid color. Using default color.")
        color = "white"
    
    return text, font, color

def create_ascii_art(text, font="standard"):
    figlet = pyfiglet.Figlet(font=font)
    return figlet.renderText(text)

def save_to_file(ascii_art, filename="ascii_art.txt"):
    with open(filename, "w") as file:
        file.write(ascii_art)
    print(f"ASCII art saved to {filename}")

def main():
    text, font, color = get_user_input()
    
    ascii_art = create_ascii_art(text, font)
    
    print("\nPreview of ASCII Art:")
    print(termcolor.colored(ascii_art, color))

    save_option = input("Do you want to save this ASCII art to a file? (y/n): ").lower()
    if save_option == "y":
        save_to_file(ascii_art)

if __name__ == "__main__":
    main()
