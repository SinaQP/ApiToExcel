import pandas as pd

class ToExcel:
    def __init__(self, excel_file_name, data):
        self.excel_file_name = excel_file_name
        self.data_frame = pd.DataFrame(data)

    def convert_data_to_excel(self):
        self.data_frame.to_excel(self.excel_file_name, index=False)

