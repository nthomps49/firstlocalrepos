import csv

file = open('data_file/dictnames.csv', 'w')

with file:
    
    fnames = ['FirstName', 'LastName']
    writer = csv.DictWriter(file, fieldnames=fnames)
    
    writer.writeheader()
    writer.writerow({'FirstName' : 'Sofia', 'LastName': 'Reyes'})
    writer.writerow({'FirstName' : 'Jerome', 'LastName': 'Jackson'})
    writer.writerow({'FirstName' : 'Jia', 'LastName': 'Zhong'})