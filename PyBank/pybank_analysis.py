import csv
import os

csvpath = os.path.join("C:/Users/minak/Git_Repos/Python-Challenge/PyBank/Resources/budget_data.csv")

total_months = 0
total_profit = 0
previous_profit = 0
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

with open(csvpath, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        total_months += 1

        profit = int(row[1])

        total_profit += profit

        change = profit - previous_profit

        profit_change_list.append(change)

        previous_profit = profit

        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
            
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

average_change = sum(profit_change_list) / len(profit_change_list)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
