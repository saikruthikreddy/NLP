import re

with open("1st.txt", "r") as f:
    data = f.read()

phones = re.findall(r"\d{10}", data)
print("Phone numbers:", phones)
