from library_.config import config
import xlrd
path = config.Data_path

def read_locators():
    workbook = xlrd.open_workbook(config.Data_path)
    worksheet = workbook.sheet_by_name("offerpage")
    rows = worksheet.nrows
    print(rows)
    d = {}

    for i in range(1,rows):
        row = worksheet.row_values(i)
        print(row)
        d[row[0]] = (row[1],row[2])
    return d

print(read_locators())