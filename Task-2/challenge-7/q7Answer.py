import csv
from csv import DictReader

def find(filename):
    with open(filename) as csvfile:
        reader = DictReader(csvfile)
        heading=input('Input the column heading:')
        value=input('Input the value you want to find:') 
        have_value_or_heading=False
        for row in reader:
                    # check the arguments against the row
                    if row[heading] == value:
                        have_value_or_heading=True
                        print(row)
                        
        if have_value_or_heading==False:
            print('Heading or value not found!') 
 
find('c7.csv')   

