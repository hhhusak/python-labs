import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.csv_visualizer_app import App

app = App('../assets/data.csv')
app.run()