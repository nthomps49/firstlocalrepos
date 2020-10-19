with open('data_file/sample.txt') as f:

    line = f.readline()

    data = f.readlines()

#print(data)
#print(f.closed)

    while line:
        print(line)
        line = f.readline()










