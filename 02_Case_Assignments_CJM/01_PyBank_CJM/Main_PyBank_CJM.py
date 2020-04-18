#import dependencies
import os
import csv

#initialize variables
total_months = 0
net_total = 0
last_month = 0
net_change = 0
greatest_increase = None
increase_month = "Placeholder"
greatest_decrease = None
decrease_month = "Placeholder"

#locate csv file from Resources folder
PyBank_csv = os.path.join("Resources", "budget_data.csv")

#read the csv file
with open(PyBank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

#skip header row
    csv_header = next(csv_reader)

#iterate row by row through the file    
    for row in csv_reader:
        
    #set the value of profits/losses to the value of the current row
        this_month = int(row[1])
    #keeps track of number the months in the dataset
        total_months += 1
    #keeps track of the span of months (to be used for the average)
        month_span = total_months - 1
    #adds the profits/losses to the net total
        net_total += this_month
    #compares this month's value to last month's value
        month_change = this_month - last_month
    #adds the monthly change to the net change
        net_change += month_change 
    
    #Sets the values in the first row as the initial greatest increases 
    #and decreases for the dataset, and makes sure the first month is 
    #considered with the net total, but not with the net change
    #Note: this if statement only returns "True" for the first row.
        if greatest_increase == None and greatest_decrease == None:
            greatest_increase = this_month
            increase_month = row[0]
            greatest_decrease = this_month
            decrease_month = row[0]
            net_change = 0
    
    #Compares the value in this row to the current record-holder for monthly 
    #increase/decrease. If this value is higher than the current greatest 
    #increase or lower than the current greatest decrease, the value (and 
    #month) is replaced with values from this row.
        if month_change > greatest_increase:
            greatest_increase = month_change
            increase_month = row[0]
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            decrease_month = row[0]
    
    #reassigns the row value for this month as the new value for last month    
        last_month = this_month

#calculates the average change in profits/losses over the course of the data
    average_change = (net_change / month_span)           

#specify a file path for the output file
output_path = os.path.join("Analysis","MyBank_Output_CJM.txt")

#open file in write mode
with open(output_path, 'w') as txt_file:
    
#variable for the desired results and enters data with f-strings    
    results = (f"Financial Analysis\n"
               f"----------------------------\n"
               f"Total Months: {total_months}\n"
               f"Total: ${net_total}\n"
               f"Average Change: ${average_change:.2f}\n"
               f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n"
               f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

#prints the data to the terminal and exports the data to a .txt file   
    print(results)
    txt_file.write(results)
