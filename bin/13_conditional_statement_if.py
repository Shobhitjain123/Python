"""
Conditional Statement 'if':
We can execute block of code based on the condition
"""

print("Only 'if-blocks'")
print("-"*20)
# ---------------

x = 10
if x == 10:
    print("x is equal to 10")
    print("x is equal to 10")
    print("x is equal to 10")

if x > 10:
    print("x is greater than 10")
    print("x is greater than 10")
    print("x is greater than 10")

if x < 10:
    print("x is smaller than 10")
    print("x is smaller than 10")
    print("x is smaller than 10")

print("#"*40, end="\n\n")
###########################

print("'if and elif blocks'")
print("-"*20)
# ---------------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

elif x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
###########################

print("'if, elif and else blocks'")
print("-"*20)
# ---------------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

else:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
###########################

print("'if with strings, list, tuples etc'")
print("-"*20)
# ---------------

my_string = "Python"
my_list = ["Java", "Python", "C++"]

print("my_string:", my_string)
print("my_list:", my_list, end="\n\n")

if ("tho" in my_string) and (my_string != "Java") and ("Python" in my_list):
    print("All conditions are True")

print("#"*40, end="\n\n")
###########################