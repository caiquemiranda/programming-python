list1 = [50, 20, 51, 50, 17, 45, 48, 19, 50]
print("Given List:\n",list1)
res = max(set(list1), key = list1.count)
print("Most Ocuured Element:\n",res)