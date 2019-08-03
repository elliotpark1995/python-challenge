import os
import csv

#load csv file
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

#variables
candidates = []
vote_count = []
percent_votes = []
total_votes = 0

#read csv file
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    
#loop
    for row in csvreader:
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_count.append(1)
        else:
            index = candidates.index(row[2])
            vote_count[index] += 1

#set percent_votes list
    for votes in vote_count:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

#results
    winner = max(vote_count)
    index = vote_count.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(vote_count[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

#printing the analysis to the terminal
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(vote_count[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))