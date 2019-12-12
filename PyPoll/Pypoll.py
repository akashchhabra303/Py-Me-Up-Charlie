# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration 
# isn't what it used to be.)

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: 
# Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and 
# calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.





import os
import csv

total_votes = 0
# total_net = 0
votes = []
khan= 0
correy = 0
li = 0
otooley = 0
# greatest_inc = ["",0]
# greatest_dec = ["",599999999]



os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_data = os.path.join("", "Resources", "election_data.csv")


with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    first_row = next(csvreader)
    # prev_value = int(first_row[2])
    # print(header)
    total_votes += 1 


    for row in csvreader:
        total_votes = total_votes + 1
        candidate = str(row[2])
        # total_net = total_net + int(row[1])
        # monthly_change = int(row[1]) - prev_value
        # prev_value = int(row[1])
        # avg_lst.append(monthly_change) 
        
        if candidate == ("Khan"):
            khan = khan + 1

        if candidate == ("Correy"):
            correy = correy + 1
        
        if candidate == ("Li"):
            li = li + 1

        if candidate == ("O'Tooley"):
            otooley = otooley + 1


   


khan_per = (khan / total_votes) * 100
correy_per = (correy / total_votes) * 100
li_per = (li / total_votes) * 100
otooley_per = (otooley / total_votes) * 100
 
# winner_lst = [khan_per, correy_per, li_per, otooley_per]

# print ([winner])

if khan > correy and khan > li and khan > otooley :
    winner = "Khan"
  
if correy > khan and correy > li and correy > otooley :
    winner = "Correy"

if li > khan and li > correy and li > otooley:
    winner = "Li"

if otooley > khan and otooley > correy and otooley > li :
    winner = "O'Tooley"




# print(total_votes)
# print(khan_per) 
# print(khan)

# print (correy) 
# print(li)
# print(otooley)

print("Election Results")
print("----------------------------------------------")       
print("Total Votes: " + str(total_votes))  
print("----------------------------------------------")   
print("Khan : " + str(round((khan_per),3)) +"% "+ "" + "(" + str(khan)+ ")")
print("Correy : " + str(round((correy_per),3)) +"% "+ "" + "(" + str(correy)+ ")")
print("Li : " + str(round((li_per),3)) +"% "+ "" + "(" + str(li)+ ")")
print("O'Tooley : " + str(round((otooley_per),3)) +"% "+ "" + "(" + str(otooley)+ ")")
print("----------------------------------------------")   
print("Winner: " + str(winner))



os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_data_results = os.path.join("", "Resources", "election_data_results.csv")



# Open the file using "write" mode. Specify the variable to hold the contents
with open(election_data_results, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------------------"])       
    csvwriter.writerow(["Total Votes: " + str(total_votes)])  
    csvwriter.writerow(["----------------------------------------------"])   
    csvwriter.writerow(["Khan : " + str(round((khan_per),3)) +"% "+ "" + "(" + str(khan)+ ")"])
    csvwriter.writerow(["Correy : " + str(round((correy_per),3)) +"% "+ "" + "(" + str(correy)+ ")"])
    csvwriter.writerow(["Li : " + str(round((li_per),3)) +"% "+ "" + "(" + str(li)+ ")"])
    csvwriter.writerow(["O'Tooley : " + str(round((otooley_per),3)) +"% "+ "" + "(" + str(otooley)+ ")"])
    csvwriter.writerow(["----------------------------------------------"])   
    csvwriter.writerow(["Winner: " + str(winner)])