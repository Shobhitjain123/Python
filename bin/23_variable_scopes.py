"""
Here,
Scope-3: Global Scope
"""

print("Scope-3: Global Scope: CASE-1")
print("-"*20)
# ---------------

x = 100 # Global Scope
# We can access anywhere, which means in any block as well,
# like if, for, function, class


def my_function_1():
    print("In my_function_1, accessing global variable x:", x) # 100


my_function_1()
print("Value of x, outside the function:", x) # 100

print("#"*40, end="\n\n")
###########################

print("Scope-3: Global Scope: CASE-2")
print("-"*20)
# ---------------

x = 100 # Global Scope
# We can access anywhere, which means in any block as well,
# like if, for, function, class


def my_function_1():
    # x = 10000 # This will create local variable

    global x # Access global variable
    x = 200 # Change global variable value
    print("In my_function_1, accessing global variable x:", x) # 200


my_function_1()
print("Value of x, outside the function:", x) # 200

print("#"*40, end="\n\n")
###########################