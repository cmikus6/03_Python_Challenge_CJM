import os
import csv

cereal_csv = os.path.join("Resources", "cereal.csv")

with open(cereal_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    #print(csv_reader)

    # Skip the header row
    next(csv_reader, None)
    
    # Read each row of data and find the cereals with at least 5g of fiber
    for row in csv_reader:
        if float(row[7]) >= 5:
            #print(row)
            #Pulling out only the data from the columns we need
            print(f"{row[0]} has {row[7]} grams of fiber.")