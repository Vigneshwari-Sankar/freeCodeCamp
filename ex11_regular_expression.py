# Search for lines that start with From and have an at sign
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    # the search string ^From:.+@ will successfully match lines that start with 
    # “From:”, followed by one or more characters (.+), followed by an at-sign.
    if re.search('^From:.+@', line):
        print(line)


s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
#substrings that have at least one (\S)non-whitespace character, 
# followed by an at-sign, followed by at least one more (\S)non-whitespace character
lst = re.findall('\S+@\S+', s)
print(lst)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)