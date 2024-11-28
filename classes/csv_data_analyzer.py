class DataAnalyzer:
    @staticmethod
    def find_extremes(data):
        print("\nЕкстремальні значення по кожному стовпчику:")
        
        # Обробка числових стовпчиків
        for column in data.select_dtypes(include='number').columns:
            print(f"{column}: Мінімум = {data[column].min()}, Максимум = {data[column].max()}")
        
        # Обробка текстових стовпчиків
        for column in data.select_dtypes(include='object').columns:
            print(f"{column}: Початок = {data[column].min()}, Кінець = {data[column].max()}")
