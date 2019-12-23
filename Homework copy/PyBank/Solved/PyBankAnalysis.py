#Module 
import os
import csv

#file path to read and write
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
pathout = os.path.join('..', 'Resources', 'Budget Analysis')

#Create conditional logic for comprehension of list
total_months = 0
total_revenue = 0
initial_revenue = 0
change_in_revenue = 0
revenue_list =[]
months_change = []
GreatestIncrease = ["", 0]
GreatestDecrease = ["", 99999999999]

#Read in the data file 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Read the header and create a variable to omitt intial calculations 
    csv_header = next(csvfile)
    omitt = next(csvreader)
    initial_revenue = int(omitt[1])
    total_months = total_months + 1 
    total_revenue = total_revenue + int(omitt[1])

    #To loop through the data and collect 
    for row in csvreader:
        print(row)
        total_months = total_months + 1 
        total_revenue = total_revenue + int(row[1])


        #Calculate the changes in revenue 
        change_in_revenue = int(row[1]) - initial_revenue
        initial_revenue = int(row[1])
        revenue_list.append(change_in_revenue)
        months_change = months_change + [row[0]]

        #Calculate the greatest increase or decrease in revenue 
        if (change_in_revenue > GreatestIncrease[1]):
            GreatestIncrease[1] = change_in_revenue
            GreatestIncrease[0] = row[0]
        
        if (change_in_revenue < GreatestDecrease[1]):
            GreatestDecrease[0] = row[0]
            GreatestDecrease[1] = change_in_revenue
#Now calculate the average revenue 
avg_revenue = sum(revenue_list) / len(revenue_list)

#Show result in the a new text file 
Result = (
    f"Total Months: {total_months}\n"
    f"Total Revenue: {total_revenue}\n"
    f"Greatest Increase in Revenue: {GreatestIncrease[0]} ${GreatestIncrease[1]}\n"
    f"Greatest Decrease in Revenue: {GreatestDecrease[0]} ${GreatestDecrease[1]}\n"
    f"Average Change in Revenue: ${avg_revenue}\n"
)

print(Result)


