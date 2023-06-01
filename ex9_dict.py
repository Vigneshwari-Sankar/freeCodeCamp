# write a program that counts the number of words using dict and find the word 
# with highest freqeuncy uses dict.txt

new_dict = {}
fname = input('Enter the file name: ')
fhandle = open(fname)

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        # this is used to add 1 if the word already exsist in dictionary or append 
        # the new word and assign 0 to it.
        new_dict[word] = new_dict.get(word, 0) + 1
    
print(new_dict)

max_count = -1
max_word = None
for k,v in new_dict.items():
    if max_count == -1 or v > max_count:
        max_count = v
        max_word = k
print(max_word, max_count)

