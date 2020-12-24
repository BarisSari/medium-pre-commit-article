import os

from src.bar import a as bar_a
from src.foo.a import example


def main():
    print(
        "Let's violate maximum line length here. The default line length is 79 for flake8, but this"
        " one has more than 100 characters."
    )
    print("Working directory: ", os.getcwd())
    print(bar_a.example())
    print(example())
    print(bar_a.example_2())


if __name__ == "__main__":
    main()
