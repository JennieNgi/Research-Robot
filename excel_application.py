from RPA.Excel.Application import Application

from openpyxl import Workbook
import os

class ExcelApplication():
    def __init__(self):
        self.excel_app = Application()
        self.filename = ""

    def write_to_cells(self, scientist_info):
        """
        Writes scientist information to cells in an Excel workbook.

        Args:
            scientist_info (list): A list containing dictionaries of scientist information.
        """
        # Prompt the user to enter the workbook name
        self.filename = input("**Enter the excel workbook name for saving the scientists data: ")
        # Define the file path on the desktop with the given filename and .xlsx extension
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, self.filename + ".xlsx")

        # create a new excel workbook and save it; if it already exists, override the file
        workbook = Workbook()
        workbook.save(file_path)

        # Open the Excel application
        self.excel_app.open_application()
        
        # Open the workbook
        self.excel_app.open_workbook(file_path)
        
        # Set the active worksheet
        self.excel_app.set_active_worksheet()
        
        # Write header values to the cells
        self.excel_app.write_to_cells(row=1, column=1, value='Scientist Name')
        self.excel_app.write_to_cells(row=1, column=2, value='Death Date')
        self.excel_app.write_to_cells(row=1, column=3, value='Birth Date')
        self.excel_app.write_to_cells(row=1, column=4, value='Age')
        self.excel_app.write_to_cells(row=1, column=4, value='Description')

        # Iterate over the scientist information and write it to the cells
        for index, scientist in enumerate(scientist_info):
            self.excel_app.write_to_cells(row=index+2, column=1, value=scientist['name'])
            self.excel_app.write_to_cells(row=index+2, column=2, value=scientist['death_date'])
            self.excel_app.write_to_cells(row=index+2, column=3, value=scientist['birth_date'])
            self.excel_app.write_to_cells(row=index+2, column=4, value=scientist['age'])
            self.excel_app.write_to_cells(row=index+2, column=4, value=scientist['description'])

        # Save the workbook
        self.excel_app.save_excel()
        
        # Quit the Excel application
        self.excel_app.quit_application()