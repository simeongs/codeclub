#abs() returns the absolute value of a number
print(abs(-1))
print(abs(-100))
print(abs(0))
print(abs(45))

#all() returns True  if all items in an iterable object are True
print(all([True, True, True]))
print(all([True, False, True]))
print(all([False, False, False]))

#any() returns True if at least one item in the iterable object is True
print(any([True, True, True]))
print(any([True, False, True]))
print(any([False, False, False]))

#bin() returns the binary form of a number
print(bin(2))
print(bin(0))
print(bin(5))

#len() returns the length of an object
print(len("#codeclub"))
print(len(["bakerloo", "central", "circle", "district", "hammersmith", "jubilee", "metropolitan", "nothern", "picadilly", "victoria", "waterloo and city"]))
print(len({1, 2, 3}))
print(len(""))
print(len([]))
print(len({}))

#isinstance() returns True if a speficied object is an instance of a of specified object
print(isinstance("codeclub", str))
print(isinstance("codeclub", int))

#sum() sums items in iterator
print(sum([1,2,3]))
print(sum([-1,2,-3,4]))
print(sum([10,20,30,40,50]))

#min() returns smallest value in iterable
print(min([1,2,3]))
print(min([-1,2,-3,4]))
print(min([10,20,30,40,50]))

#max() returns greatest value in iterable
print(max([1,2,3]))
print(max([-1,2,-3,4]))
print(max([10,20,30,40,50]))

