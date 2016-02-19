# Rosalind Bioinformatics Stronghold: 
# 		5. 

# Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).
#######################################################################################

import sys 

file = sys.stdin.read().split()
seq1 = file[0]
seq2 = file[1]

mutation = 0 

for index, nuc in enumerate(seq1):
	if nuc != seq2[index]:
		mutation +=1 
print >> sys.stdout, mutation