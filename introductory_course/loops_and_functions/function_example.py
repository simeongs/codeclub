 
def make_plural(string):
	if string[-1] != "s":
		string += "s"
	else:
		return "already plural"

	return string

print(make_plural("cats"))