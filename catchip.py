import re
a=['123']
print(a)
with open("10.234.235.txt", "r") as f:
    for line in f.readlines():
        result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
        if result:
            print(result[0])

