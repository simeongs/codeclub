 
def make_plural(string):
	if string[-1] != "s":
		string += "s"
	else:
		return "already plural"

	return string


list_of_words = ["cat", "dogs", "cakes", "forks", "sock" ," shoe"]

for word in list_of_words:
	print(make_plural(word))