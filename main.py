# Imports necesary functions
import csv
import os
import operator
os.chdir(os.path.dirname(os.path.abspath(__file__))) # sets current directory

# Part 1
csvpath = os.path.join(".", "Resources", "budget_data.csv") # finds the budget data

# initilize varialbes for storing months and profits as a list
months = [] 
profits = []

# opens the file
with open(csvpath) as csvfile:
        bank_info = csv.reader(csvfile, delimiter=',')
        header = next(bank_info) # sets the header
        # loops throught the documents storing the months and profits in their respective lists 
        for row in bank_info:
            months.append(row[0])
            profits.append(int(row[1]))

# prints requested information 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${round(sum(profits)/len(months), 2)}")
print(f"Greatest increase in profits: {months[profits.index(max(profits))]} (${max(profits)}) ")
print(f"Greatest decrease in profits: {months[profits.index(min(profits))]} (${min(profits)}) ")
print()
output_path = os.path.join(".", "analysis", "Financial_Analysis.txt") # sets path for exporting the data

# writes information to above file
with open(output_path, 'w') as text:
    text.write("Financial Analysis \n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {len(months)}\n")
    text.write(f"Total: ${sum(profits)}\n")
    text.write(f"Average Change: ${round(sum(profits)/len(months), 2)}\n")
    text.write(f"Greatest increase in profits: {months[profits.index(max(profits))]} (${max(profits)})\n")
    text.write(f"Greatest decrease in profits: {months[profits.index(min(profits))]} (${min(profits)})\n")

# Part 2
votes = dict() # dictionary that stores candiates names as keys and the number of votes as values 

csvpath = os.path.join(".", "Resources", "election_data.csv")

# opens the file
with open(csvpath) as csvfile:
        poll_info = csv.reader(csvfile, delimiter=',')
        header = next(poll_info) # sets header
        
        for row in poll_info: # iterates through rows
           if row[2] in votes.keys(): # if name of a candite is in the dictionary increments the number votes
                   votes[row[2]] += 1
           else: # if name of candiates is not yet in the dictionary it is added 
                   votes[row[2]] = 1

# prints requested info       
print("Election Results")
print("-------------------------")
print(f"Total Votes: {sum(votes.values())}")
print("-------------------------")
for people in votes.keys():
        print(f"{people}: {round(100 *(votes[people]/sum(votes.values())), 4)}% ({votes[people]})")
print("-------------------------")
print(f"Winner: {max(votes.items(), key=operator.itemgetter(1))[0]}")

output_path2 = os.path.join(".", "analysis", "Election_Results.txt") # opens file for storing data

# writes information to above file
with open(output_path2, 'w') as text:
        text.write("Election Results \n")
        text.write("-------------------------\n")
        text.write(f"Total Votes: {sum(votes.values())}\n")
        text.write("-------------------------")
        for people in votes.keys():
                text.write(f"{people}: {round(100 *(votes[people]/sum(votes.values())), 4)}% ({votes[people]})\n")
        text.write("-------------------------\n")
        text.write(f"Winner: {max(votes.items(), key=operator.itemgetter(1))[0]}\n")   