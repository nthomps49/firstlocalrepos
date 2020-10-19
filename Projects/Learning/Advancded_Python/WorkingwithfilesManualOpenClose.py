file = open("data_file/sample.txt")

#print(file.mode)
#print(file.name)
#print(file.closed)
print(file.read())

file.seek(0)#puts cursor back to the start of file
print(file.read(5))
print(file.tell())
print(file.read(5))
print(file.readline())#returns rest of line that has not been read yet
print(file.readline())
print(file.readline())# now we read all the lines
print(file.readline())#retruns blank there is no more to read.
file.seek(0)
print(file.readlines())#returns list of each line of text
file.close()
print(file.closed)









