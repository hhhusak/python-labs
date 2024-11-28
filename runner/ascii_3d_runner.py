import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.ascii_3d_functions import ASCIIArt3DGenerator

generator = ASCIIArt3DGenerator()
generator.run()