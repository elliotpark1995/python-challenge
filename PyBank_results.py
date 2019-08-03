import os
import csv

#initial variables
total_months=0
total_revenue=0
current_month_revenue=0
previous_month_revenue=0
rev_change=0
revenue_change=[]
number_of_months=[]

#load csv file
csvpath=os.path.join("PyBank","Resources","budget_data.csv")

#read csv file
with open (csvpath,newline="") as csvfile:
    csvreader =csv.reader(csvfile,delimiter=",")
    next(csvreader)
#Set variables & monthly changes in profit/losses
    for row in csvreader:
        total_months=total_months+1
        number_of_months.append(row[0])
        current_month_revenue=int(row[1])
        total_revenue=total_revenue + current_month_revenue
        if total_months > 1:
            rev_change = current_month_revenue - previous_month_revenue
            revenue_change.append(rev_change)
        previous_month_revenue=current_month_revenue
        
#calculate monthly changes in profit/losses
monthly_revenue_sum=sum(revenue_change)
avg_change=monthly_revenue_sum/(total_months-1)
greatest_change=max(revenue_change)
least_change=min(revenue_change)
greatest_change_month = revenue_change.index(greatest_change)
least_change_month=revenue_change.index(least_change)
most_profitable_month=number_of_months[greatest_change_month+1]
least_profitable_month=number_of_months[least_change_month+1]

#summary
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Profit or Loss: ${total_revenue}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {most_profitable_month} (${greatest_change})")
print(f"Greatest Decrease in Profits: {least_profitable_month} (${least_change})")

#printing the analysis to terminal
textpath = os.path.join("PyBank_Script_and_Output","PyBank_results.csv")
with open(textpath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("---------------------------" + "\n")
    text.write(f"Total Months: {total_months}" + "\n")
    text.write(f"Profit or Loss: ${total_revenue}" + "\n")
    text.write(f"Average Change: ${avg_change}" + "\n")
    text.write(f"Greatest Increase in Profits: {most_profitable_month} (${greatest_change})" + "\n")
    text.write(f"Greatest Decrease in Profits: {least_profitable_month} (${least_change})" + "\n")
