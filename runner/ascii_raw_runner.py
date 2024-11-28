import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.ascii_raw import ASCIIArtGenerator

asciiGenerator = ASCIIArtGenerator();
asciiGenerator.run()