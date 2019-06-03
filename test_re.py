import re

l = []

with open('zen.txt','r') as f:
    l = f.read()
matches = re.findall('ugly',l)

print(matches)