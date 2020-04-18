#import dependencies
import os
import csv

#locate csv file from Resources folder
PyPoll_csv = os.path.join("Resources", "election_data.csv")

#intialize variables
total_votes = 0
current_winner_count = 0
current_winner = None
vote_row = None
candidates = []
candidate_votes = []
percentage_votes = []

#read the csv file
with open(PyPoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

#skip header row
    csv_header = next(csv_reader)

#iterate row by row through the file, using row[2] (the candidate) to represent the voter's choice
    for row in csv_reader:
        vote_row = row[2]

#ticker to tally the number of votes 
        total_votes += 1

#if the voter's choice is not already in the list of candidates, this condition adds the name to the list and adds a section to the candidate tally list    
        if vote_row not in candidates:
            candidates.append(vote_row)
            candidate_votes.append(0)

#finds the index of the voter's choice in the candidate list, and adds a point to that index of the candidate votes tally list          
        vote = candidates.index(vote_row)
        candidate_votes[vote] += 1

#once all lines of the csv have been read, iterates through the candidate_votes list    
    for count in candidate_votes:    

#if a candidate's vote count is greater than the current vote count record, both the current winner count and winner name are updated
        if count > current_winner_count:
            current_winner_count = count
            current_winner = candidates[candidate_votes.index(count)]

#calculates the percentage of votes won by the candidate and appends the percentage to a new list
        percent_won = (count / total_votes)*100
        percentage_votes.append(percent_won)

#zips the values from all three populated lists for analytical purposes
output = zip(candidates, percentage_votes, candidate_votes)

#develops the election summary for printing and exporting (by repeatedly adding to the results with f-strings)
summary = (f"Election Results\n"
           f"----------------------------\n"
           f"Total Votes: {total_votes}\n"
           f"----------------------------\n")

#reads through the zipped values and prints the information for each candidate on the same line
for c, pv, cv in output:
    summary += "{0}: {1:.4f}% ({2})\n".format(c, pv, cv)
summary += (f"----------------------------\n"
            f"Winner: {current_winner}\n"
            f"----------------------------\n")

#prints the final chain of strings
print(summary)

#specify a file path for the output file
output_path = os.path.join("Analysis","MyPoll_Output_CJM.txt")

#open file in write mode and export to a .txt file
with open(output_path, 'w') as txt_file:
    txt_file.write(summary)