import re

text = """
Mrs. Johnson
Mr Edward
Ms Jane
Master Josepsh
Mr Simeon
Mrs Jones
Ms. Doe
rsM sim
cat mat sat
trlolololololol
"""

pattern_1 = re.compile (r"Mrs. Johnson")
print(re.findall(pattern_1, text))

#can do this for each one

pattern_2 = re.compile(r"Mr [A-Z][a-z]+")
print(re.findall(pattern_2, text))

pattern_3 = re.compile(r"[Mrs\.|Mr\.|Ms\.|Master]+ [A-Z][a-z]+")
print(re.findall(pattern_3, text))
