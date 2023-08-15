import os
import csv

# Define the path to the CSV file
csvpath = os.path.join("C:/Users/minak/Git_Repos/Python-Challenge/PyPoll/Resources/election_data.csv")

# Create an empty list to store the data
election_data = []

# Read the CSV file and store its contents in the list
with open(csvpath, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        election_data.append(row)

total_votes = len(election_data)

candidates = []
for row in election_data:
    candidate = row["Candidate"]
    if candidate not in candidates:
        candidates.append(candidate)

votes_per_candidate = {}
for row in election_data:
    candidate = row["Candidate"]
    if candidate in votes_per_candidate:
        votes_per_candidate[candidate] += 1
    else:
        votes_per_candidate[candidate] = 1

percentage_per_candidate = {}
for candidate, votes in votes_per_candidate.items():
    percentage = (votes / total_votes) * 100
    percentage_per_candidate[candidate] = percentage

winner = max(votes_per_candidate, key=votes_per_candidate.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")