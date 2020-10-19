import csv

names = [['First Name', 'Last Name'], ['Sofia', 'Reyes'],['Jerome', 'Jackson'],['Jia', 'Zhong']]

file = open('data_file/names.csv', 'w')

with file:
    file_writer = csv.writer(file)
    
    for row in names:
        file_writer.writerow(row)
        