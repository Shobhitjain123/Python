"""
Exceptions Handling:
"""
# print("WITHOUT handling Exceptions:")
# print("-"*20)
# # ---------------
#
# a = 10
# b = 0
# result = a / b # Program will terminate abruptly HERE
# print("result:", result)
#
# print("#"*40, end="\n\n")
# ###########################
#


print("Handling Exceptions using (try/except):")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a / b # Program will NOT terminate, instead control will be passed to 'except' block
    print("result:", result) # This line will never execute
except:
    print("Reached except block")
    print("Some error in try")
    print("Here, we are writing code to solve problem occurred in try block")

print("#"*40, end="\n\n")
###########################