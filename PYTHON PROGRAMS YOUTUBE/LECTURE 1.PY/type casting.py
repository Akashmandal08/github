
#TYPE CASTING.
# a="2"
# b=4.25        THIS WILL NOT BE EXICUATTED BECAUSE IN PYTHON WE CANNOT ADD STRING 
# sum=a+b       WITH FLOAT .

# print(sum)    WE CAN ADD IT BY A DIFFERENT METHOD THAT IS CALLED AS TYPE CASTING.

a=int("2")
b=4.25        #adding int infront of a string changes is type and makes it integer value 
sum = a+b      # this process is called as "TYPE CASTING"
print(type(a))
print("Addition:", sum)