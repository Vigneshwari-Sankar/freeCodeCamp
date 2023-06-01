#Calculate the pay and round it off to 2 decimal places with try and except.
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    pay = float(hours) * float(rate)
except:
    pay = -1
    
if pay > 0:
    print('Pay:', round(pay, 2))
else:
    print('Error, please input numeric input')