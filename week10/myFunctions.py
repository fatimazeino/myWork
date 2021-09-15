# myFunctions.py
# this program takes in a number and return a list containing a Fibonacci sequence of that many numbers.
# Author: Fatima Zeino

import logging
#logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number == 0:
        return []
    if number < 0:
        raise ValueError('number must be > 0')
    a = 0
    b = 1
    fibonacciSequence = [0]
    for i in range(1,number):
      fibonacciSequence.append(b)
      a , b = b, a + b
    #logging.debug("%d: %s",number, fibonacciSequence)
    return []
 
'''
try:
 #fibonacci(-1)
except ValueError:
# we want this exception to be thrown
# so this is an example where we want to do nothing
  pass
else:
# if the exception was not thrown we should throw
# Assertion error
  assert False, 'fibonacci missing ValueError'
# or
#raise AssertionError("fibonacci no valueError ") '''

'''
if __name__ =='__main__':

    
    return7 =[0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]

    assert fibonacci(7) == return7
    assert fibonacci(11) == return11
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    
    print("all good") '''