import os
import csv

# Lists
voter_id_ls = []
candidate_ls = []
summ_cand_ls = []
summ_vote_ls = []
perc_vote_ls = []

total_votes = 0
    
# Function to export results to a text file
def export_results_to_text_file():
    # Set file path
    file_path = os.path.join("Analysis", "election_results.txt")

    # Write text file
    text_file = open(file_path,"w")

    # Write the header row
    text_file.write("Election Results \n")
    text_file.write("______________________________ \n \n")

    # Write Total votes
    text_file.write(f'Total Votes: {total_votes} \n')
    text_file.write("______________________________ \n \n")

    # Write summary by candidate
    for i in range(len(summ_cand_ls)):
        text_file.write(f'{summ_cand_ls[i]}: {perc_vote_ls[i]}% ({summ_vote_ls[i]}) \n')

    # Write winner
    text_file.write("______________________________ \n \n")
    text_file.write(f'Winner: {winner} \n')
    text_file.write("______________________________ \n")

    # Close file
    text_file.close()
    return
    
# Function to print results to terminal
def print_results_to_terminal():

    # Print the header row
    print("Election Results")
    print("______________________________ \n")

    # Print Total votes
    print(f'Total Votes: {total_votes}')
    print("______________________________ \n")

    # Print summary by candidate
    for i in range(len(summ_cand_ls)):
        print(f'{summ_cand_ls[i]}: {perc_vote_ls[i]}% ({summ_vote_ls[i]})')

    # Print winner
    print("______________________________ \n")
    print(f'Winner: {winner}')
    print("______________________________ \n")
    
    return
    
# Main
# File path
file_path = os.path.join("Resources", "election_data.csv")

# Open budget_csv as csvfile:
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Save and skip row of header
    csv_header = next(csvreader)

    for row in csvreader:
        # Total number of votes
        total_votes += 1

        # Voter id list
        voter_id_ls.append(int(row[0]))

        # Candidate list
        candidate_ls.append(row[2])

# Count number of votes by candidate
for i in range(len(candidate_ls)):
    # Candidate found
    cand_found = False
    # Seek for candidate within summary list to add vote
    for j in range(len(summ_cand_ls)):
        if candidate_ls[i] == summ_cand_ls[j]:
            summ_vote_ls[j] += 1
            cand_found = True
            break
    
    # Add candidate to summary lists if not found
    if cand_found == False:
        summ_cand_ls.append(candidate_ls[i])
        summ_vote_ls.append(1)

max_votes = 0
for i in range(len(summ_vote_ls)):
    # Calculate percentage of votes each candidate won
    perc_vote_ls.append(round((summ_vote_ls[i]/total_votes) * 100,0))
    
    # Determine winner
    if summ_vote_ls[i] > max_votes:
        max_votes = summ_vote_ls[i]
        winner = summ_cand_ls[i]

# Export text file with results
export_results_to_text_file()

# Print results to terminal
print_results_to_terminal()

