#given a list of integers, create a function to return the total of the list 
#[1,2,3] >>> 6 (1+2+3) = 6

def make_total(list_of_numbers):
	total = 0
	for number in list_of_numbers:
		total += number
	return total

#test cases
print(make_total([1,2,3]))
print(make_total([-1,2,-3,4]))
print(make_total([10,20,30,40,50]))