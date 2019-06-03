f = open("дробные числа.txt")


for line in f:
    print(line,end='')

l = list(range(1,5))
li = l.__iter__()

while li.__next__():
    print(li)