import os
import xlrd

path =  "D:/" 
# Change the directory
os.chdir(path)

# Open the file
book = xlrd.open_workbook("Ozone.xlsx")  
# Check for the number of sheets
print("The number of worksheets is {0}".format(book.nsheets))

# Check for the name, number of rows, and number of columns
sh = book.sheet_by_index(0)
print(sh.name, sh.nrows, sh.ncols)

# Check a certain value at intersection of row and column
print(sh.cell_value(rowx=29, colx=3) )

# Values from column 1
print (sh.col(1))

# Values from the header of the table
print (sh.row(0))

