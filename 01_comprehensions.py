# comprehension are used to decrease the no.of lines
# but sometimes :
#       logic becomes hard to read
#       debugging becomes difficult

# 1st loops
nums = [1,2,3,4,5]
a = [i for i in nums]
print(a)

#the above line means
for i in nums:
    a.append(i)

#print(a)    

#2nd logics

even_no = [i for i in nums if i%2==0]
print(even_no)