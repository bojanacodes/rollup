# Rollup technical task

## The program

This program calculates the total amounts required for each part in a Bill of Materials. The output is an Excel file. 

To run this program, run "python rollup.py output.xlsx" in the command line. The second command line argument (“output.xlsx”) must be provided, but it can be named anything.

The Argparse library is used to process this second argument, and will print an error if it is missing. 

The program gets Bill of Materials part data from an API using the Python Requests library. 

This data is processed using a helper recursive function, starting from the "root" part with no parent. The recursive function finds all parent parts of each part and multiplies their quantities to get the final total amount required of each part. 

The openpyxl library is used to create, write and save Excel files. The command line argument provided is used as the name of the file. 

The is_valid_data function checks that the data is complete, so that the process_data function can run. Currently, the function will end after a piece of data is found to be missing and print a message to identify it. For example:

```
 if "parent_part_id" not in item:
    print(f"A parent part id is missing for the part with API ID: {id}.")
    return False 
```

 However, this is not helpful for cases where multiple pieces of data are missing. If I had more time, I would have written this so that all the missing pieces of data are captured before the function ends. I would have liked to include more validation, such as ensuring that the command line argument must end in an Excel file format.

## The test

The test will check that the calculations performed by the process_data function are correct. It used a short sample of hard-coded data obtained from the BOM API.

With more time I would have liked to add more tests, for example to check that the calculation works in cases where a part has multiple parent parts, such as the example drawn in the task outline. 


