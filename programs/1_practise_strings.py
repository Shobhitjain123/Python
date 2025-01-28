#HOMEWORK
"""
From the given string below,
extract
DATE

Expected Output:
------------
26/Apr/2000
------------
"""

print("input data:")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
output_start_index = input_data.find("[")
output_end_index = input_data.find(":")

print(input_data[output_start_index+1 : output_end_index])

print("#"*40, end="\n\n")
###########################


