import os
import csv
csvpath2 = "Resources/election_data.csv"
votes = []
candidates = []
totalvotes = 0
totalcharles = 0
totaldiana = 0
totalraymon = 0
candidatevotes = {}
with open (csvpath2) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        votes.append(row[0])
        totalvotes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidatevotes[candidate] = 0
        candidatevotes[candidate] += 1
    charles = candidates[0]
    diana = candidates[1]
    raymon = candidates[2]
for v in candidatevotes.values():
    vlist = list(candidatevotes.values())
totalcharles = vlist[0]
totaldiana = vlist[1]
totalraymon= vlist[2]
percentcharles = round(((totalcharles/totalvotes)*100),3)
percentdiana = round(((totaldiana/totalvotes)*100),3)
percentraymon = round(((totalraymon/totalvotes)*100),3)
winner = max(candidatevotes.items(), key = lambda x: x[1])[0]
print("Election Results")
print("----------------------------")
print(f"Total Votes: {totalvotes}")
print("----------------------------")
print(f"{charles}: {percentcharles}% ({totalcharles})")
print(f"{diana}: {percentdiana}% ({totaldiana})")
print(f"{raymon}: {percentraymon}% ({totalraymon})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

results = f"Election Results\n----------------------------\nTotal Votes: {totalvotes}\n----------------------------\n{charles}: {percentcharles}% ({totalcharles})\n{diana}: {percentdiana}% ({totaldiana})\n{raymon}: {percentraymon}% ({totalraymon})\n----------------------------\nWinner: {winner}\n----------------------------"

csvpath2 = "analysis/results.txt"

f = open (csvpath2, "w")
f.write(results)
f.close()