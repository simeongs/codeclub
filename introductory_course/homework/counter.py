'''given a list of items, print a dictionary of the item and how many times it occurs'''

arr = ["a", "b", "b", "b", "c", "c"] 
counter = {}

for item in arr:
	if counter.get(item) == None:
		counter[item] = 1
	else:
		counter[item] += 1

print(counter)
print()

from collections import Counter
counter = Counter(arr)
print(counter)