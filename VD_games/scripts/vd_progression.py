import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games import engine
from games import progression

def main():
    engine.run_game(progression)

if __name__ == "__main__":
    main()
