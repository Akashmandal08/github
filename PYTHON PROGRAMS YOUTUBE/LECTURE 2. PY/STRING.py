# TOPIC:-STRINGS AND ITS OPERATION.

#str1= "this is second leacture. \n i am loving it."
#print(str1)

#\n and \t is called as sequence character. 
   # \n is used for next line and \t is use or 1inch space.
# this is used whe we want big paragraph in code.

##################################################

# property applied in string.

#  1} CANCATENATION. (+)sigh is used to add two string.
# # THIS IS USED WHEN WE WANT TO ADD TWO STRINGS.

# str1="akash"
# len1=len(str1)     #to print how many letter are there in a word
# print(len1)        #we use the function len()  
# #                  # space is also count in len() function.

# str2="mandal"
# len2=len(str2)
# print(len2)

# final_str=(str1+str2)
# print(final_str)
###########################################################
# 2}INDEXING.
#when we want to find at what no whish letter is present then we can use indexing.

# str="i ama a boy."
# ch= str[4]
# print(ch)

# REVWRSE INDEXING. in reverse indexing it counts from the backside.

# str='this is PP clss.'
# ch=str[-3]
# print(ch)

#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##@@#@#@#@#@

# 3]SLICING (it is mainly use in machine learning.)
# accessing part of a string. this is used when we want to print a particular part off string.
# in this the ending is not counted
# one more feature if we dont write the end of the string python automatically understand it and takes the end.


# str="akash mandal"
# print(str[:6])  #[0:4]
# print(str[6:len(str)])  #[5:len(str)]


# str='you are late in the class'
# print(str[16:19])

# #  --> REVERSE SLICING  

# str="you are late in the class"
# print(str[-12:])





#$@#$@#$#@#$@#$@#$@#$@#$@#$@#$@#$@#$@#$#@#$@#$@#$@$#

# FROM HERE THE FUNCTIN OF STRING STARTS.
 
# 1] str.endwith("er.") RETURNS TRUE IF STRING ENDS WITH SUBSTR

# str=" my name is akash"
# print(str.endswith("sh"))  #IT WILL GIVE TRUE VALUE IF IT ENDS.
# print(str.endswith("ak"))  #IT WILL GIVE FALSE VALUE IF IT NOT ENDS.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 2]str.capitalize( )  capitalizes 1st character

# str="i am studing python"
# print(str.capitalize()) #this function is used when yo
#                         want to make the first letter capital.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 3] str.replace (old,new) replaces all occurance of old with new.
# str1= "i love to eat mangos"
# print(str1.replace("mangos","apple")) #this function is used when we want to replace any leatter or word with another .

str='you are late in the class'
print(str.replace("you are","they are"))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 4] str.find(word)  this function is used to find weather that word is present in our string.
#   it will will tell you at what index no it is present.


# str="i am learning python from youtube"
# print(str.find("youtube"))
# print(str.find('java'))  # if it is not present it will give you -1 index no.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 5] str.count("am") this function will tell you how many times the word occured.

# str= "I am learning python. \n python is a intepreator language. \n python is eassy to learn."
# print(str.count("python"))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# PRACTICE PROBLEM.

#1]WAP to input users first name and print its leangth.

# name= input("enter your nme:")
# print(len(name))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#2] WAP to find the occurance of "s" in a string.

# str="sun is big. sun have high tempurature. sun is very big."
# print(str.count("s"))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\