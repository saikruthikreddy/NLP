import re

with open("nums.txt") as f:
    text = f.read()

nums = re.findall(r"\d+", text)
nums = list(map(int, nums))

print("Numbers:", nums)
print("Sum =", sum(nums))
