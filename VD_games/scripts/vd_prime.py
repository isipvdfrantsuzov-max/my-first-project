import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games import engine
from games import prime

def main():
    engine.run_game(prime)

if __name__ == "__main__":
    main()
