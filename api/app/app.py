import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from service.client import ApiClient
from repository.repository import Repository
from ui.data_visualizer import DataVisualizer
from input.input_handler import UserInputHandler

class ApiApp:
    def __init__(self):
        self.api_client = ApiClient("https://jsonplaceholder.typicode.com")
        self.repository = Repository(self.api_client)

    def run(self):
        while True:
            choice = UserInputHandler.get_user_choice()
            if choice == '1':
                posts = self.repository.get_posts()
                if posts:
                    DataVisualizer.display_data(posts, "Список постів")
                    DataVisualizer.save_to_json(posts, 'posts.json')
                    DataVisualizer.save_to_csv(posts, 'posts.csv')
            elif choice == '2':
                comments = self.repository.get_comments()
                if comments:
                    DataVisualizer.display_data(comments, "Список коментарів")
                    DataVisualizer.save_to_json(comments, 'comments.json')
                    DataVisualizer.save_to_csv(comments, 'comments.csv')
            elif choice == '3':
                print("Вихід...")
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    app = ApiApp()
    app.run()