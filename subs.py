# Rosalind Bioinformatics Stronghold: 
# 		8. Finding a Motif in DNA

# Given:  Two DNA strings s and t (each of length at most 1kbp)

# Return: All locations of t as a substring of s. 
##################################################################################################
import sys
# Input
file = sys.stdin.read().split() 
orig_seq = file[0]
sub = file[1]

# Recursive substring finder
def find_sub(orig_seq, seq, sub, positions):
	if seq.find(sub) != -1:
		pos = seq.find(sub) + 1
		new_seq = seq[pos + 1:]
		diff = len(orig_seq)-len(seq)
		pos = pos + diff
		positions.append(pos)
		find_sub(orig_seq,new_seq,sub, positions)
	return positions

# Output
for i in find_sub(orig_seq, orig_seq, sub, positions = []):
	print >> sys.stdout, i,

	