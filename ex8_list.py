#Write a program to read through the mail box data and when you find line that 
#starts with “From”, you will split the line into words using the split function.
#We are interested in who sent the message, which is the second word on the From line.
#Count the number of lines

email = list()
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Invalid file name')
    quit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    
    words = line.split()
    print(words[1])
    email.append(words[1])
        
print('There were '+ str(len(email)) +' in the file with From as the first word')
        