#!usr/bin/env python
import sys

def print_details():
    print('The calculations')
    number = 0
    for x in range(10):
        number = number +1
    print('number is : {}'.format(number))

if __name__ =='__main__':
    print_details()
    sys.exit

