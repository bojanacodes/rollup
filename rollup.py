import argparse
import sys

# print("hello world")

my_parser = argparse.ArgumentParser(description='Output Bill of Materials in Excel')

my_parser.add_argument('filename', type=str)

args = my_parser.parse_args()

print(args.filename)