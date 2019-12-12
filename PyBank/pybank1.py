#[In this challenge, you are tasked with creating a Python script for analyzing 
# the financial records of your company. You will give a set of financial data 
# called budget_data.csv. The dataset is composed of two columns: Date and 
# Profit/Losses. (Thankfully, your company has rather lax standards for 
# accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period]


import os
import csv

total_months = 0
total_net = 0
avg_lst = []
greatest_inc = ["",0]
greatest_dec = ["",599999999]



os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_data = os.path.join("", "Resources", "budget_data.csv")



with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    first_row = next(csvreader)
    prev_value = int(first_row[1])
    print(header)
    total_months += 1 
    total_net = total_net + int(first_row[1])

    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        monthly_change = int(row[1]) - prev_value
        prev_value = int(row[1])
        avg_lst.append(monthly_change) 
        
        if monthly_change > greatest_inc[1] :
            greatest_inc[0] = row[0]
            greatest_inc[1] = monthly_change

        if monthly_change < greatest_dec[1] :
            greatest_dec[0] = row[0]
            greatest_dec[1] = monthly_change


        
        #avg_change = avg_change + total_avg
        #avg_change = total_avg
av_change = sum(avg_lst) / len(avg_lst)


# print(total_months)
# print(total_net)
# #print(avg_lst)
# print(av_change)
# print(greatest_inc)
# print(greatest_dec)
print("Financial Analysis")           
print("----------------------------------------------")       
print("Total Months : " +str(total_months))     
print ("Total : "+"$ " + str(total_net))     
print ("Average Change: " + str(round((av_change),2) ))
print("Greatest Increase in Profits : " + str(greatest_inc))
print("Greatest Decrease in Profits : " + str(greatest_dec))


os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_data_results = os.path.join("", "Resources", "budget_data_results.csv")



# Open the file using "write" mode. Specify the variable to hold the contents
with open(budget_data_results, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------------------------"])       
    csvwriter.writerow(["Total Months : " +str(total_months)])  
    csvwriter.writerow(["Total : "+"$ " + str(total_net)])   
    csvwriter.writerow(["Average Change: " + str(round((av_change),2) )])
    csvwriter.writerow(["Greatest Increase in Profits : " + str(greatest_inc)])
    csvwriter.writerow(["Greatest Decrease in Profits : " + str(greatest_dec)])

   
   