import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games import engine
from games import gcd

def main():
    engine.run_game(gcd)

if __name__ == "__main__":
    main()
