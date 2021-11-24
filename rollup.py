import argparse
import sys
from openpyxl import Workbook

# print("hello world")

my_parser = argparse.ArgumentParser(description='Output Bill of Materials in Excel')

my_parser.add_argument('filename', type=str)

args = my_parser.parse_args()

# print(args.filename)

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename=f"{args.filename}.xlsx")