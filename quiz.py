
def check_gender(pin):
pin    =  pin.split('-') [1]
num  = pin[0] # '3'
num  = int (num)

if num % 2 == 0:
    print ('female')
else:
    print('male')
my_pin = '200101 - 3012345'

check_gender(my_pin)
