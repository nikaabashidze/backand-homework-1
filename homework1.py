

# Version 1  


my_num = "156"       #

if type(my_num) is str:
    my_num = int(my_num)
elif type(my_num) is int: 
    my_num = str(my_num)

print(type(my_num))  
print(my_num) 



# Version 2   Function


# def convert(num):
#     if isinstance(num, str):
#         return int(num)
#     elif isinstance(num, int):
#         return str(num)
#     else:
#         return "!!!!!!!!!!!!!!"

# my_num = "259"
# print(convert(my_num))  
# print(type(convert(my_num))) 


# my_num = 259
# print(convert(my_num)) 
# print(type(convert(my_num))) 


# my_num = 0.98
# print(convert(my_num)) 



