# -----------------------
# install openpyxl: pip install openpyxl
# -----------------------

# -----------------------
# Create Workbook and Sheet
# -----------------------
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


# -----------------------
# Read external spreadsheet
# -----------------------
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
# read_spreadsheet()


# -----------------------
# Read_only mode
# -----------------------
def read_only_mode():
    from openpyxl import load_workbook
    workbook = load_workbook(filename="./files/openpyxl_files/openpyxl_sample_data.xlsx", read_only=True)
    print(f"Sheets: {workbook.sheetnames}")
    sheet = workbook.active
    print(f"Active Sheet: {sheet.title}")
    
    # Read cells of sheets
    print(f"Cell of [H5]: {sheet['H5'].value}")
    print(f"Cell of [A6]: {sheet['A6'].value}")
    print(f"Cell of [C3]: {sheet['C3'].value}")
# read_only_mode()


# -----------------------
# Data only mode
# -----------------------
def data_only_mode():
    from openpyxl import load_workbook
    workbook = load_workbook(filename="./files/openpyxl_files/openpyxl_sample_data.xlsx", data_only=True)
    print(f"Sheets: {workbook.sheetnames}")
    sheet = workbook.active
    print(f"Active Sheet: {sheet.title}")
    
    # Read cells of sheets
    print(f"Cell of [H5]: {sheet['H5'].value}")
    print(f"Cell of [A6]: {sheet['A6'].value}")
    print(f"Cell of [C3]: {sheet['C3'].value}")
# data_only_mode()


# -----------------------
# How to access range of cells values
# -----------------------
class access_cell_values:
    def __init__(self): 
        from openpyxl import load_workbook
        workbook = load_workbook(filename="./files/openpyxl_files/openpyxl_sample_data.xlsx")
        self.sheet = workbook.active
    # Method 1: Accessing a range of cells
    def access_with_special_row_column(self):
        print(f"Accessing range of cells A1:C3: {self.sheet['A1:C3']}")
        print("---------------------------------")
        for row in self.sheet["A1:C3"]:
            print(f"Row: {row}")
            for cell in row:
                print(f"Cell of {cell.coordinate}: {cell.value}")
    
    # Method 2: Get All cells from special column (like. column A)
    def access_to_special_column(self):
        print(f"Accessing column A: {self.sheet['A']}")
        print("---------------------------------")
        for cell in self.sheet["A"]:
            print(f"Cell of {cell.coordinate}: {cell.value}")

    # Method 3: Get All cells for range of columns (like. columns A to C)
    def access_to_range_of_columns(self):
        print(f"Accessing columns A to C: {self.sheet['A:C']}")
        print("---------------------------------")
        for column in self.sheet["A:C"]:
            for cell in column:
                print(f"Cell of {cell.coordinate}: {cell.value}")
    
    # Method 4: Get All cells from special row (like. row 5)
    def access_to_special_row(self):
        print(f"Accessing row 5: {self.sheet[5]}")
        for cell in self.sheet[5]:
            print(f"Cell of {cell.coordinate}: {cell.value}")
    
    # Method 5: Get All cells for range of rows (like. rows 1 to 5)
    def access_to_range_of_rows(self):
        print(f"Accessing rows 1 to 5: {self.sheet[1:5]}")
        print("---------------------------------")
        for row in self.sheet[1:5]:
            for cell in row:
                print(f"Cell of {cell.coordinate}: {cell.value}")
    
    # iter_rows() method: Get cells by iterating over rows
    def access_with_iter_rows(self):
        print(f"Accessing cells with iter_rows() method: {self.sheet.iter_rows(min_row=1, max_row=5, min_col=1, max_col=3)}")
        print("---------------------------------")
        for row in self.sheet.iter_rows(min_row=1, max_row=5, min_col=1, max_col=3, values_only=True):
            print(f"Row: {row}")
            for cell in row:
                print(f"{cell}")
        
    
    # iter_cols() method: Get cells by iterating over columns
    def access_with_iter_cols(self):
        print(f"Accessing cells with iter_cols() method: {self.sheet.iter_cols(min_row=1, max_row=5, min_col=1, max_col=3)}")
        print("---------------------------------")
        for column in self.sheet.iter_cols(min_row=1, max_row=5, min_col=1, max_col=3, values_only=True):
            print(f"Column: {column}")
            for cell in column:
                print(f"{cell}")
    
    # Get All data cell info of rows
    def access_all_rows_data(self):
        print(f"Accessing all rows data with values_only=True: {self.sheet.rows}")
        print("---------------------------------")
        for row in self.sheet.rows:
            print(row)

    # Get All data cell info of columns
    def access_all_columns_data(self):
        print(f"Accessing all columns data with values_only=True: {self.sheet.columns}")
        print("---------------------------------")
        for column in self.sheet.columns:
            print(column)


def access_data_of_spreadsheet():
    access = access_cell_values()
    # access.access_with_special_row_column()
    # access.access_to_special_column()
    # access.access_to_range_of_columns()
    # access.access_to_special_row()
    # access.access_to_range_of_rows()
    # access.access_with_iter_rows()
    # access.access_with_iter_cols()
    # access.access_all_rows_data()
    # access.access_all_columns_data()

# access_data_of_spreadsheet()

