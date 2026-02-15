# install openpyxl: pip install openpyxl


# Create Workbook and Sheet
def create_workbook():
    from openpyxl import Workbook
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Hello"
    sheet["B1"] = "World"
    sheet["C1"] = "!"
    sheet["A2"] = "Welcome"
    sheet["B2"] = "to"
    sheet["C2"] = "openpyxl"
    sheet["A3"] = "This"
    sheet["B3"] = "is"
    sheet["C3"] = "Excel"
    sheet["D3"] = "File"
    sheet["E3"] = "Created"
    sheet["F3"] = "with"
    sheet["G3"] = "openpyxl"
    sheet["H3"] = "Library"
    workbook.save(filename="./files/openpyxl_files/hello_world.xlsx")


# create_workbook()

# Read external spreadsheet
def read_spreadsheet():
    from openpyxl import load_workbook
    workbook = load_workbook(filename="./files/openpyxl_files/openpyxl_sample_data.xlsx")
    print(f"Sheets: {workbook.sheetnames}")
    sheet = workbook.active
    print(f"Active Sheet: {sheet.title}")
    
    # Read cells of sheets
    # First Method: Using []
    print(f"Cell of [H5]: {sheet["H5"].value}")
    print(f"Cell of [A6]: {sheet["A6"].value}")
    print(f"Cell of [C3]: {sheet["C3"].value}")
    
    # Second Method: Using Cell method
    print(f"Cell of [H5](row=5, column=8): {sheet.cell(row=5, column=8).value}")
    print(f"Cell of [A6](row=6, column=1): {sheet.cell(row=6, column=1).value}")
    print(f"Cell of [C3](row=3, column=3): {sheet.cell(row=3, column=3).value}")


read_spreadsheet()