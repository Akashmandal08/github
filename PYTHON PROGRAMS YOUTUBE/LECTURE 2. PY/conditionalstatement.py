# 1]IF is used when something is true.
# this is used when first statement is true.

# age=16

# if(age >=18):
#     print("you can vote and apply for driving linces.")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 2] (ELEF) this property is used when the first property is not true 
#   and we want to print the another line which is true.
# elif will only check the code (if) property is false.

# age="13"

# if(age>="18"):
#     print("you can vote")

# elif(age<"18"):
#     print("you can't vote.")    

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 3] ELSE this is property which we can write only one time.
#  generally it is written at the end if the code.
# if is used when all other property give us false then then only ELSE is used.

# age=14

# if(age>=18):
#     print("you can vote")
# else:
#     print("you can't vote go home.")

#\\\\\\\\\\PRACTICE PROBLEM\\\\\\\\\\\\\\\\\\\\\\\\\\

marks= int(input('enter your marks:'))

if(marks>=90):
    grade='A'

elif(marks<90 and marks>=80):
    grade='B'

elif(marks<80 and marks>=70):
    grade="C"

elif(marks<70):
    grade='D'
else:
    grade="D"

print("grade of student-->", grade)
