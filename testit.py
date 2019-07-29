#!/usr/bin/env python3

# To import from a zip file, with or without importlib.resources,
# add the string representation of the zip file's path to sys.path.
from pathlib import Path
import sys
import importlib.resources

data_zip = Path('data.zip').resolve()
sys.path.insert(0, str(data_zip))


def main() -> None:
    # Read the contents of of a text file from the package.
    message = importlib.resources.read_text('data', 'hello.txt')
    print(message)


if __name__ == '__main__':
    main()
