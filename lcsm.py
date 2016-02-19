# Rosalind Bioinformatics Stronghold: 
# 		14. Finding a Shared Motif

# Given: A collection of k (k<=100k<=100) DNA strings of length at most 1 kbp each in FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions exist,
# 		  you may return any single solution.)
##################################################################################################

import sys ,  Bio.SeqIO
# Input File
file = open(sys.argv[1], "rU")

# Create list of strings
sequences = []
for seq in (Bio.SeqIO.parse(file, "fasta")):
	sequences.append(seq.seq)

# Find the shortest to use as base comparison, remove from original list
shortest = min(sequences)
sequences.remove(min(sequences))

def sub_checker(sequences, sub):
	not_in = 0
	for seq in sequences:
		if seq.find(sub) == -1:
			not_in = 1
			break
	if not_in == 1:	
		return False
	else:
		return True

# Use the shortest string, to create substrings and check for longest substring 
longest_sub = ''
for index, x in enumerate(shortest):
	sub = x
	for y in shortest[index+1:]:
		sub += y
		if sub_checker(sequences, sub) != True:
			break
	#	print sub, ' didnt'
		if len(sub) >= len(longest_sub):
				longest_sub = sub 

print >> sys.stdout, longest_sub
