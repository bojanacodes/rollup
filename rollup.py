import argparse
import os
import sys
from openpyxl import Workbook
import requests
import pprint

def get_data(url):
    response = requests.get("https://interviewbom.herokuapp.com/bom/").json()
    bom_data = response['data']
    return bom_data

def find_root_parent(bom_list):
    root_parent = [part for part in bom_list if part["parent_part_id"] == None]
    return root_parent

def find_parents(bom_list, parent_part_id):
    part_parent = [part for part in bom_list if part["part_id"] == parent_part_id]
    return part_parent

def find_children(bom_list, parent_part_id): 
    part_children = [part for part in bom_list if part["parent_part_id"] == parent_part_id]
    return part_children

def inner_process_data(data, parent_id, quantity, result):
    children = find_children(data, parent_id)

    for child in children: 
        if child["part_id"] not in result:
            result[child["part_id"]] = child["quantity"] * quantity
        else:
            result[child["part_id"]] += child["quantity"] * quantity

        inner_process_data(data, child["part_id"], quantity * child["quantity"], result)


def process_data(data):
    result = {}
    inner_process_data(data, None, 1, result)
    return result

def write_data(data, filename):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Part ID"
    sheet["B1"] = "Quantity"
    count = 1

    for id, quantity in data.items():
        count += 1
        sheet[f"A{count}"] = id
        sheet[f"B{count}"] = quantity

    workbook.save(filename = filename)

def main():
    my_parser = argparse.ArgumentParser(description='Output Bill of Materials in Excel')
    my_parser.add_argument('filename', type=str)
    args = my_parser.parse_args()
    
    data = get_data("https://interviewbom.herokuapp.com/bom/")
    processed_data = process_data(data)
    write_data(processed_data, args.filename)


if __name__ == "__main__":
    main()
