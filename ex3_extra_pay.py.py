#Compute the pay and increase the pay to 1.5 times after 40 hours
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

#Convert string to floating point
try:
    fl_hours = float(hours)
    fl_rate = float(rate)
except:
    print('Error, please input numeric input')
    quit()

if fl_hours > 40:
    extra_hours = fl_hours - 40
    extra_rate = 1.5 * fl_rate
    extra_pay = extra_hours * extra_rate
    pay = (40 * fl_rate) + extra_pay

else:
    pay = fl_hours * fl_rate

print('Pay:', round(pay, 2))
    
