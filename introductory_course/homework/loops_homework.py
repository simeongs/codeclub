#Given a postive integer N (greater than 0)
#for i < N print i squared
#eg N = 5 >>> 0, 1, 4, 9, 16, 25
#hint: think loops

N = int(input())

for i in range(0, N + 1):
	print(i * i)