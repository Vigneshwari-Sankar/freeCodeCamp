#exercise: Write a program to read through a file and 
#print the contents of the file (line by line) all in upper case. 

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Invalid file name')
    quit()

for line in fhand:
    line = line.rstrip()
    print(line.upper())
