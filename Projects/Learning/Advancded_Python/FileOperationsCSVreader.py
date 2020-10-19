import csv

file = open('data_file/record_pipe.csv', 'r')

with file:
    read = csv.reader(file,delimiter="|")
    
    for row in read:
        print(row)