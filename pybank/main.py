import os
import csv
from numpy import mean

csvpath=os.path.join('Resources','budget_data.csv')

with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    headers=next(csvreader)
    total=0
    lastrow=0
    change=[]
    minc=0
    maxc=0
    for row in csvreader:
        total=total+float(row[1])
        change1=float(row[1])-lastrow
        change.append(change1)
        lastrow=float(row[1])
        if change1>maxc:
            maxmonth=row[0]
            maxc=change1
        if change1<minc:
            minmonth=row[0]
            minc=change1
    months=len(change)
    change.pop((0))
    avc=mean(change)
    avc=-round(avc,2)

final=f"Financial Analysis\n---------------------------- \nTotal Months: {months}\nTotal: ${total}\nAverage  Change: ${avc}\nGreatest Increase in Profits: {maxmonth} ${maxc}\nGreatest Decrease in Profits: {minmonth} ${minc}\n"
print(final)
File= open("final.txt","w+")
File.write(final)