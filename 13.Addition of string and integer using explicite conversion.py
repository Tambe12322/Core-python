num_int=123
num_str="456"
print("datatype of num_int",type(num_int))
print("datatype of num_str before type casting:",type(num_str))

num_str=int(num_str)
print("data type of num_str after type casting:",type(num_str))
num_num=num_int+num_str
print("sum of num_int and num_str;",num_num)
print("Data type of the sum:",type(num_num))