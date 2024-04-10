import csv
import os

filepath =  os.path.join('Resources' , 'election_data.csv')

totalvotes = 0
candidatevotes = {}

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)

    for line in csvreader:
        totalvotes += 1
        candidate_name = line[2]

        if candidate_name in candidatevotes:
            candidatevotes[candidate_name] += 1
        else:
            candidatevotes[candidate_name] = 1

percentagevotes = {candidate: round((votes / totalvotes) * 100, 3) for candidate, votes in candidatevotes.items()}

winner = max(candidatevotes, key=candidatevotes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
for candidate, votes in candidatevotes.items():
    print(f"{candidate}: {percentagevotes[candidate]}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output = 'analysis'
outputfile = os.path.join(output, 'election_results.txt')

with open(outputfile, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {totalvotes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidatevotes.items():
        file.write(f"{candidate}: {percentagevotes[candidate]}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")