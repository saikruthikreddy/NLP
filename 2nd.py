import re

s = "apple, mango, orange, banana"

words = re.findall(r"[A-Za-z]+", s)
separators = re.findall(r"[^A-Za-z]+", s)

print("Words:", words)
print("Separators:", separators)
