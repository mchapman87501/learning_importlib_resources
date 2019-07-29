#!/bin/bash

# Create a standalone executable that uses testit.py's main as the entry point.

set -e

rm -rf dist testit.pyz
mkdir dist
cp -r testit.py dist

shiv --site-packages dist --compressed -p '/usr/bin/env python3' -o testit.pyz -e testit.main

