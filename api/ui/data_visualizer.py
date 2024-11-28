import json
import csv

class DataVisualizer:
    @staticmethod
    def display_data(data, title):
        print(f"\n{title}")
        print("=" * len(title))
        for item in data:
            print(item)

    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Дані збережено в {filename}")

    @staticmethod
    def save_to_csv(data, filename):
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())
        print(f"Дані збережено в {filename}")