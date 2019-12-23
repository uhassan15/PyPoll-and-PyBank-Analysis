#Module 
import os
import csv

#To join the file 
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
pathout = os.path.join('..', 'Resources', 'Electoral outcome')


#Reading of the data using CSV mode
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

    #Read the header in your data file 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #To read each row of the data in the file use
    for row in csvreader:
        print(row)

