import os
import xlrd

path =  "D:/"    #A
os.chdir(path)    #B

book = xlrd.open_workbook("Ozone.xlsx")    #C
print("The number of worksheets is {0}".format(book.nsheets))    #D

sh = book.sheet_by_index(0)
print(sh.name, sh.nrows, sh.ncols)    #E
print(sh.cell_value(rowx=29, colx=3) )    #F
print (sh.col(1))
print (sh.row(0))
#A This is system-dependent, and the user should change the path to their folder.
#B Change of the directory 
#C Open the file containing the data
#D Determine the number of sheets
#E Check the numbers of rows and columns
#F Check a random intersection of row and column
#G Check the header of the tabular information

