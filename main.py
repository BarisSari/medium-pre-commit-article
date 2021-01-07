import os

from src.bar.first_module import example as bar_example
from src.bar.first_module import example_2 as bar_example_2
from src.foo.first_module import ExampleFooClass as fooClass
from src.foo.first_module import example as foo_example


def main():
    print(
        "Let's violate maximum line length here. The default line length is 79 for flake8, but this"
        " one has more than 100 characters."
    )
    print("Working directory: ", os.getcwd())
    print(bar_example())
    print(foo_example())
    print(bar_example_2())
    cls = fooClass()
    cls.print()


if __name__ == "__main__":
    main()
