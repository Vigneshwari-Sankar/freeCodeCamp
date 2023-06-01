# write a program that counts the number of words using dict and  
# sort the words based on values and not keys using sorted.

new_dict = {}
fname = input('Enter the file name: ')
fhandle = open(fname)

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        # this is used to add 1 if the word already exsist in dictionary or append 
        # the new word and assign 0 to it. uses dict.txt
        new_dict[word] = new_dict.get(word, 0) + 1
    
#print(new_dict)

new_list = []
new_list = sorted([(v,k) for k,v in new_dict.items()], reverse=True)

for v,k in new_list[:10]:
    print(k,v)
