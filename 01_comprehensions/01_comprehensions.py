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

#3rd making dictionary by combining to list

fruits = ["apple","banana","graps"]
prices = [100,60,40]

fruit_price = {key:value for key,value in zip(fruits,prices)}
#or
fruit_price = {fruits[i]:prices[i] for i in range(len(fruits))}
print(fruit_price)

#3rd filtering dictionary

scores = {"maths":40,"science":50,"hindi":70,"sst":66}

result = {key:value for key,value in scores.items() if value >= 50}
print(result)

# 4th nesting in comprehension

pairs = [[i,j] for i in [1,2] for j in [3,4] ] # nested list
print(pairs)
# above is same as
for i in [1,2]:
    for  j in [3,4]:
        pairs.append(i,j)

print(pairs)