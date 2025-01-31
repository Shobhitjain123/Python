"""
Get data from web_server.log

then

extract
IP
DATE
URL

then

Create Below Dictionary:
------------
{
0:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
1:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
2:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
3:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
4:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
5:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
}
------------

then

Write data in dictionary to log_report_4.json

"""
print("Get data from web_server.log file")
print("-"*20)
# -------------
import json
my_json_file_handle = open('log_report_4.json', 'w')
my_log_file_handle = open(r"../log/web_server.log", 'r')

log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

myDict = {}

index = 0
for each_line in log_file_content:
    if each_line.startswith("123"):
        sp = each_line.split()
        # print("sp:", sp)

        ip = sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        dt = raw_date[1:raw_date.index(":")]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1:-1]
        myTuple = (ip, dt, url)
        myDict[index] = myTuple
        index = index + 1

print(myDict)
json.dump(myDict, my_json_file_handle)
my_json_file_handle.close()
print("#"*40, end="\n\n")
############################