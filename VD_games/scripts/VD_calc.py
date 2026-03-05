#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games import engine
from games import calc


def main():
    engine.run_game(calc)


if __name__ == "__main__":
    main()
