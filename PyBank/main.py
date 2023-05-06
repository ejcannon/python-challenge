import os
import csv
csvpath = "Resources/budget_data.csv"
totalmonths = 0
total = 0
months = []
changes = []
profits = []
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        totalmonths += 1
        total += int(row[1])
        profits.append(int(row[1]))
    for i in range (1,len(profits)):
        changes.append(profits[i] - profits[i-1])
    averagechange = sum(changes) / len(changes)
    maxchange = max(changes)
    minchange = min(changes)
    maxchangedate = months[changes.index(maxchange) + 1]
    minchangedate = months[changes.index(minchange) + 1]
    
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(averagechange, 2)}")
    print(f"Greatest Increase in Profits: {maxchangedate} (${maxchange})")
    print(f"Greatest Decrease in Profits: {minchangedate} (${minchange})")
    
    results = f"Financial Analysis \n----------------------------\nTotal Months: {totalmonths}\nTotal: ${total}\nAverage Change: ${round(averagechange, 2)}\nGreatest Increase in Profits: {maxchangedate} (${maxchange})\nGreatest Decrease in Profits: {minchangedate} (${minchange})"
    
    csvpath2 = "analysis/results.txt"

    f = open (csvpath2, "w")
    f.write(results)