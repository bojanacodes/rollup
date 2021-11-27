import argparse
import os
import sys
from openpyxl import Workbook
import requests
import pprint

def getData(url):
    response = requests.get("https://interviewbom.herokuapp.com/bom/").json()
    bom_data = response['data']
    return bom_data

def find_root_parent(bom_list):
    root_parent = [part for part in bom_list if part["parent_part_id"] == None]
    print(root_parent)
    return root_parent

def find_parents(bom_list, parent_part_id):
    part_parent = [part for part in bom_list if part["part_id"] == parent_part_id]
    return part_parent

def find_children(bom_list, parent_part_id): 
    part_children = [part for part in bom_list if part["parent_part_id"] == parent_part_id]
    return part_children

    # {'id': 21, 'parent_part_id': 3676, 'part_id': 2069, 'quantity': 3}

def innerProcessData(data, parent_id, quantity, result):
    children = find_children(data, parent_id)

    for child in children: 
        if child["part_id"] not in result:
            result[child["part_id"]] = child["quantity"] * quantity
        else:
            result[child["part_id"]] += child["quantity"] * quantity

        innerProcessData(data, child["part_id"], quantity * child["quantity"], result)


def processData(data):

    result = {}

    innerProcessData(data, None, 1, result)

    return result

def writeData(data, filename):
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "Part ID"
    sheet["B1"] = "Quantity"

    sheet["A2"] = parent_part_id
    sheet["B2"] = parent_part_quantity

    workbook.save(filename = args.filename)

def main():
    my_parser = argparse.ArgumentParser(description='Output Bill of Materials in Excel')
    my_parser.add_argument('filename', type=str)
    args = my_parser.parse_args()

    data = getData("https://interviewbom.herokuapp.com/bom/")
    processedData = processData(data)
    pprint.pprint(processedData)
    # writeData(processData, args.filename)

# def main():
#     my_parser = argparse.ArgumentParser(description='Output Bill of Materials in Excel')

#     my_parser.add_argument('filename', type=str)

#     args = my_parser.parse_args()

#     response = requests.get("https://interviewbom.herokuapp.com/bom/").json()
#     bom_data = response['data']

#     pprint.pprint(bom_data)

#     parent_part_id = bom_data[0]["part_id"]
#     parent_part_quantity = bom_data[0]["quantity"]

#     find_root_parent(bom_data)

#     workbook = Workbook()
#     sheet = workbook.active

#     sheet["A1"] = "Part ID"
#     sheet["B1"] = "Quantity"

#     sheet["A2"] = parent_part_id
#     sheet["B2"] = parent_part_quantity

#     workbook.save(filename=f"{args.filename}")


if __name__ == "__main__":
    main()
