def foo(a, b, c):
    print(a, b, c)
    
# positional arguments
foo(1, 2, 3)

# keyword arguments
foo(a=1, b=2, c=3)
foo(c=3, b=2, a=1) # Note that the order is not important here

# mix of both
foo(1, b=2, c=3)

# This is not allowed:
# foo(1, b=2, 3) # positional argument after keyword argument
# foo(1, b=2, a=3) # multiple values for argument 'a'


# default arguments
def foo(a, b, c, d=4):
    print(a, b, c, d)

foo(1, 2, 3, 4)
foo(1, b=2, c=3, d=100)

# not allowed: default arguments must be at the end
# def foo(a, b=2, c, d=4):
#     print(a, b, c, d)

