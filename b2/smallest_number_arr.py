arr1 = [36, 91, 70, 75, 56, 65];     
    
min = arr1[0];    
     
for i in range(0, len(arr1)):    
   if(arr1[i] < min):    
       min = arr1[i];    
     
print("Smallest element present in given array: " + str(min));