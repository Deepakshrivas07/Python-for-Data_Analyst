# int ,float,tuple,string are immmutable
# list ,dictionary are  mutable
a = [1,2,3]
# refers to same memory location so if b changes a will also change as a and b refers to same memory.
b=a
#tooo avoid it we have .copy() methord
b= a.copy()
print(a)

def add_item(data):
    data.append(10)

data = [1,34,53]
add_item(data.copy())
print(data)