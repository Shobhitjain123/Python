"""
From the given string below,
extract
PICS

Expected Output:
------------
wpaper.gif
------------
"""

print("input data:")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
start_index = input_data.find('"GET') + len('"GET ')
end_index = input_data.find(' ', start_index)
path = input_data[start_index:end_index]
filename = path.split('/')[-1]
print(filename)
print("#"*40, end="\n\n")