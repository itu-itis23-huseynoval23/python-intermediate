# multiplication
result = 7 * 5
print(result)

# power operation
result = 2 ** 4
print(result)

# list
zeros = [0] * 10
onetwos = [1, 2] * 5
print(zeros)
print(onetwos)

# tuple
zeros = (0,) * 10
onetwos = (1, 2) * 5
print(zeros)
print(onetwos)

# string
A_string = "A" * 10
AB_string = "AB" * 5
print(A_string)
print(AB_string)

def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
my_function("Hey", 3, [0, 1, 2], name="Alex", age=8)

# Parameters after '*' or '*identifier' are keyword-only parameters and may only be passed using keyword arguments.
def my_function2(name, *, age):
    print(name)
    print(age)

# my_function2("Michael", 5) --> this would raise a TypeError
my_function2("Michael", age=5)

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

*beginning, last = numbers
print(beginning)
print(last)

print()

first, *end = numbers
print(first)
print(end)

print()
first, *middle, last = numbers
print(first)
print(middle)
print(last)

# dump iterables into a list and merge them
my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
my_list = [*my_tuple, *my_set]
print(my_list)

# merge two dictionaries with dict unpacking
dict_a = {'one': 1, 'two': 2}
dict_b = {'three': 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)