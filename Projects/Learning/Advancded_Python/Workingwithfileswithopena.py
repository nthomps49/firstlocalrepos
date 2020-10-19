import os
#file = open('data_file/example.txt', 'w')
#"r"   Opens a file for reading only.
#"r+"  Opens a file for both reading and writing.
#"rb"  Opens a file for reading only in binary format.
#"rb+" Opens a file for both reading and writing in binary format.
#"w"   Opens a file for writing only.
#"a"   Open for writing.  The file is created if it does not exist.
#"a+"  Open for reading and writing.  The file is created if it does not exist.
#file.write("Let's check the write operation")
#with open the file again to write mode
#file.seek(6) to move to the 6th byte in the file
#    e.seek(6)
#    e.write(" examine ") # Let's  examine  write operation (produces this output now)
#for lines in file:
#    print(lines)

with open('data_file/example.txt', 'w') as f:

    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

with open('data_file/example.txt', 'r') as f:
    
    for lines in f:
        print(lines)

f = open('data_file/example.txt', 'a')
print(f.tell())

f.writelines(["Another line was appended\n", "WHat will it look like now?\n", "Lets check it out\n"])

f.close()

f = open("data_file/example.txt", "r")
print(f.readlines())

#for lines in f:
#    print(lines)
#f.fileno()
#f.isatty()
#f.readable
#f.writable()
f.close()

print(os.stat('data_file/example.txt').st_size)

#you can just wack off data based on size with f.truncate(37) for example

#os.rename("data_file/example.txt", "ata_file/changed_example.txt") renames the file
#os.remove("data_file/changed_example.txt") deletes the file
