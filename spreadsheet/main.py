import openpyxl

inv_file = openxyl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]