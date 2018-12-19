#can you guess all the outputs of the print statements?

#vairable assignment

x = 20 
y = 50

print(x + y)
print(y - x)
print(x * y)
print(y / x)
print(y // x)
print(y % x )

print()

#data structrues
hobbies = ["coding", "clubbing", "codeclubbing", "crosswords", "climbing", "cooking"]

print(hobbies[2])
print(hobbies[-3])
print(hobbies[1:4])
print(hobbies[1:4:-1])

print()

student = {"id": 24, "name": "Simeon", "age":16, "favourite subjects": ["maths", "physics", "PE"]}

print(student["age"])
print(student["age"] + student["id"])
print(student["favourite subjects"])
print(student["favourite subjects"][0])

nums = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5]
print(set(nums))

print()

#conditionals 
print(True)
print(not True)
print(False or True)
print(not False and True)
print(not False and not True and True)
print(not not True)

print()

#loopa

for i in range(1, 10):
	print(i)

print()

for j in range(10, 0, -1):
	print(j)

print() 

for a in range(1, 11):
	print(str(a) + " times table\n")
	for b in range(1, 11):
		print(a * b)
	print

