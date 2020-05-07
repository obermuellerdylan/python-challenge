import os
import csv

# Path to CSV file
election_data = os.path.join('Resources', 'election_data.csv')

# Defining function
def election_results():

    # Creating list of votes and variable counts
    totalvotes = []
    candidates = []
    cand_votes = []
    cand_perc = []

    for row in csvreader:
         totalvotes.append(row[2])

    for name in totalvotes:

        if name not in candidates:
            candidates.append(name)
            cand_votes.append(0)
            cand_perc.append(0)

        for i in range(len(candidates)):
             if candidates[i] == name:
                 cand_votes[i] += 1
                 
    for i in range(len(cand_perc)):
        cand_perc[i] = (round((cand_votes[i]/len(totalvotes)*100),3))

        if max(cand_votes) == cand_votes[i]:
            winner = candidates[i]
    
    #Print results
    print('Election Resutls')
    print('-----------------------')
    print(f'Total Votes: {len(totalvotes)}')
    print('-----------------------')
    for i in range(len(candidates)):
        print(f'{candidates[i]}: {cand_perc[i]}% ({cand_votes[i]})')
    print('-----------------------')
    print(f'Winner: {winner}')
    print('-----------------------')
    
    # #Write results to text file
    # # Specify the file to write to
    output_path = os.path.join("Resources", "main.txt")

    # # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as txtfile:
    

    #     # Write the first row (column headers)
         txtfile.write('Election Resutls\n')
         txtfile.write('-----------------------\n')
         txtfile.write(f'Total Votes: {len(totalvotes)}\n')
         txtfile.write('-----------------------\n')
         for i in range(len(candidates)):
            txtfile.write(f'{candidates[i]}: {cand_perc[i]}% ({cand_votes[i]})\n')
         txtfile.write('-----------------------\n')
         txtfile.write(f'Winner: {winner}\n')
         txtfile.write('-----------------------')

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvfile)

    #RUN FUNCTION
    election_results() 