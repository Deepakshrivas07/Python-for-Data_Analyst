#NumPy stands for Numerical Python.
# Python lists store references to objects, and each integer is a separate Python object.
#A NumPy array stores values of the same type together in a contiguous block of memory:
# Less memory is used.
# Calculations are much faster.

import numpy as np

# Using a Python list
marks = [75, 80, 92, 65, 88]

new_marks = []

for mark in marks:
    new_marks.append(mark + 5)

#using numpy
marks = np.array([1,2,3,4,5])
print(marks + 5) # will put values at once

# all the arithmatics operation we can do at once without loops

# a,b,c,d,e all are different arrays
a =np.array([1,2,3,4])
b = np.zeros(5) # 5 is the length of array of zeros
c = np.ones(5)
d = np.arange(1,6) #will arange array from 1 to 5 excluding 6 
e = np.arange(1,10,2) # 1stt argument tell start , 2nd top ,3rd difference 

# vactorized Operations

num = np.array([1,2,3])
num + 10
num *  2
num > 40

print(num) #expected combined results but numpy always creates new array for each 

result1 = num + 10
result2 = num *  2
result3 = num > 40

print(result1)
print(result2)
print(result3)

# Statistics    

revanue = np.array([2344,4543,63456])

total_revanue = revanue.sum()
print(total_revanue)
avg_revanue = revanue.mean()
print(avg_revanue)
max_revanue = revanue.max()
print(max_revanue)
min_revanue = revanue.min()
print(min_revanue)


# 2D and 3D matrix

twoD_matrix = np.array([[1,2],[3,4]])
twoD_matrix = np.eye(3) # row and colums as arguement as it gives a identity matrix
print(twoD_matrix)
threeD_matrix = np.array([[[1,2]],[[3,4]]])
print(threeD_matrix)
