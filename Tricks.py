# Value swapping
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
# also possible in a list
mylist = [1, 2, 3, 4, 5]
print("Initial list :", mylist)
mylist[0], mylist[1] = mylist[1], mylist[0]
print("Modified list:", mylist)

# Create a single string from list
my_list = ["I", "am", "awesome"]

# bad
a = ""
for i in my_list:
    a += i + " "
print(a)

#good
a = " ".join(my_list)
print(a)

## join method is much faster
from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print(end - start)
# print(a)

# good
start = timer()
a = " ".join(my_list)
end = timer()
print(end - start)
#p rint(a)