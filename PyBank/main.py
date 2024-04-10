import os
import csv

filepath = os.path.join('Resources', 'budget_data.csv')

months = 0
totalprofitlosses = 0
previousprofitlosses = 0
changes = [] 
greatestincrease = ['', 0] 
greatestdecrease = ['', 0] 
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)

    for line in csvreader:
        months += 1
        totalprofitlosses += int(line[1])

        if months > 1:
            change = int(line[1]) - previousprofitlosses
            changes.append(change) 

            if change > greatestincrease[1]:
                greatestincrease = [line[0], change]

            if change < greatestdecrease[1]:
                greatestdecrease = [line[0], change]
        
        previousprofitlosses = int(line[1])

average_change = sum(changes) / len(changes)

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${totalprofitlosses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})")
print(f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})")

output = os.path.join('.', 'analysis')

outputfile = os.path.join(output, 'financial_analysis.txt')

with open(outputfile, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${totalprofitlosses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})\n")