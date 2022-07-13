
from collections import deque 
      
#Source: https://www.geeksforgeeks.org/deque-in-python/
      
# Declaring deque 
queue = deque(['name','age','DOB'])  
      
print(queue)
print (type(queue))


de = deque([1, 2, 3])

de.append(4)
print("1 - The deque after appending at right is : ")
print(de)

de.appendleft(6)
print("2 - The deque after appending at left is : ")
print(de)

de.pop()
print("3 - The deque after deleting from right is : ")
print(de)

de.popleft()
print("4 - The deque after deleting from left is : ")
print(de)


# initializing deque
de = deque([1, 2, 3, 3, 4, 2, 4])
  
# using index() to print the first occurrence of 4
print ("5 - The number 4 first occurs at a position : ", de.index(4))


  
# using insert() to insert the value 3 at 5th position
de.insert(3, 10)
print ("6 - The deque after inserting 3 at 5th position is : ", de)


  
# using count() to count the occurrences of 3
print ("7 - The count of 3 in deque is : ", de.count(3))

  
# using remove() to remove the first occurrence of 3
de.remove(3)
print ("8 - The deque after deleting first occurrence of 3 is : ", de)

