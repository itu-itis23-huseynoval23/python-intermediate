# a = 5 print(a)
a = 5 + '10'
x = -5
if x < 0:
    raise Exception('x should not be negative.')
x = -5
assert (x >= 0), 'x is not positive.'
# --> Your code will be fine if x >= 0
# This will catch all possible exceptions
try:
    a = 5 / 0
except:
    print('some error occured.')
    
# You can also catch the type of exception
try:
    a = 5 / 0
except Exception as e:
    print(e)
    
# It is good practice to specify the type of Exception you want to catch.
# Therefore, you have to know the possible errors
try:
    a = 5 / 0
except ZeroDivisionError:
    print('Only a ZeroDivisionError is handled here')
    
# You can run multiple statements in a try block, and catch different possible exceptions
try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)

try:
    a = 5 / 1
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
else:
    print('Everything is ok')

try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)
else:
    print('Everything is ok')
finally:
    print('Cleaning up some stuff...')