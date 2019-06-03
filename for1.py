j = 0
word = "sbdkfbsdkjbfe3f4kawowqfk"

for char in word:
    if char in "word":
        j += 1
print(j)        


d = {1:"name",2:"surname",3:"middle name"}

#перебор по ассоциированному массиву
for key,value in d.items():
    print(key,value)

#перебор по диапазону с условием начала 1, окончания 11 и шага 2
for number in range(1,11,2):
    print(number)

l = list(range(10))
print(l)