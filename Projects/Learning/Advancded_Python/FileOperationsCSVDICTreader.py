import csv

file = open('data_file/record_pipe.csv', 'r')

with file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(dict(row))