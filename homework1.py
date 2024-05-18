
# Version 1   Function


def convert(num):
    if isinstance(num, str):
        if num.isdigit():
            return int(num)
        else:
            return "contains non numeric characters."
        
    elif isinstance(num, int):
        return str(num)
    
    elif isinstance(num, float):
        return str(num)

    else:
        return "something wrong"




my_num = "256"
print(convert(my_num))  
print(type(convert(my_num))) 

my_num = 259
print(convert(my_num)) 
print(type(convert(my_num))) 

my_num = 0.65
print(convert(my_num)) 
print(type(convert(my_num))) 

my_num = "Legolas"
print(convert(my_num)) 
print(type(convert(my_num))) 





# Version 2    


# my_num = 456       

# if type(my_num) is str:
#     my_num = int(my_num)
# elif type(my_num) is int: 
#     my_num = str(my_num)
# else :
#     print("Invalid input")


# print(type(my_num))  
# print(my_num) 









