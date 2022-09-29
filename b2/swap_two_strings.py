str1 = input("Enter First String :")
str2 = input("Enter Second String :")  
   
print("Strings before swapping: " + str1 + " " + str2)
   
str1 = str1 + str2 
 
str2 = str1[0 : (len(str1) - len(str2))]
  
str1 = str1[len(str2):]
   
print("Strings after swapping: " + str1 + " " + str2)
