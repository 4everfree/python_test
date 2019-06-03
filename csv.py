import csv

with open("new.csv","w") as f:
    w = csv.writer(f,delimiter=',')
    w.writerow([1,2,3])
    w.writerow([4,5,6])

