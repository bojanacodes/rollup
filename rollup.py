import argparse
import os
import sys
from openpyxl import Workbook
import requests


# my_parser = argparse.ArgumentParser(description='Output Bill of Materials in Excel')

# my_parser.add_argument('filename', type=str)

# args = my_parser.parse_args()

response = requests.get("https://interviewbom.herokuapp.com/bom/").json()
bom_data = response['data']
print(bom_data[0])

# workbook = Workbook()
# sheet = workbook.active

# sheet["A1"] = "hello"
# sheet["B1"] = "world!"

# workbook.save(filename=f"{args.filename}.xlsx")
