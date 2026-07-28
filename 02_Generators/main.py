# 1. What is a generator?

# A generator is a special type of iterator that produces values one at a time using the yield keyword, making it memory-efficient.

# 2. Difference between yield and return?

# return ends the function permanently.
# yield returns a value temporarily and pauses the function so it can resume later.

# 3. Why are generators memory efficient?

# Because they generate values on demand instead of storing the entire sequence in memory.

# 4. Can a generator be reused?

# No. Once a generator is exhausted, you must create a new one to iterate again.

#01 : Create a generator that yields numbers from 1 to 10.
def range1to10 ():
    for i in range(10):
        yield i

num = range1to10()
# we have to write next to generate a next value 
# print(next(num)) # output: 0
# print(next(num)) # output: 1

# 02: Create a generator that yields only even numbers from 1 to 20.
def evenNumber ():
    for i in range(10):
        if(i%2 == 0):
            yield i

evenNo = evenNumber()
# print(next(evenNo)) # output: 0
# print(next(evenNo)) # output: 2
# print(next(evenNo)) # output: 4
# print(next(evenNo)) # output: 6
# print(next(evenNo)) # output: 8

#03 : Create an infinite generator for odd numbers.
def  infiniteLoop():
    num = 1
    while True:
        if(num%2!=0):
            yield(num)
            num+=2
        

oddNo = infiniteLoop()
# print(next(oddNo))
# print(next(oddNo))
# print(next(oddNo))
# print(next(oddNo))
# print(next(oddNo))
# print(next(oddNo))

#04 Read a text file line by line using a generator.
def readFile():
    with open("02_Generators/readme.txt","r") as file:
        for line in file:
            yield line.strip()

readingFile = readFile()
# print(next(readingFile))
# print(next(readingFile))


#05 comprehensions in generator

gen = (x*x for x in range(10)) 
print(next(gen))