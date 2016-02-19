# Rosalind Bioinformatics Stronghold: 
# 		19. Enumerating Gene Orders

# Given: A positive integer n<=7.

# Return: The total number of permutations of length nn, followed by a list of all such permutations (in any order).

##################################################################################################

import sys 
# Create a string of all numbers leading up to inputted number
seq = "".join(([str(i) for i in range(int(sys.stdin.readline()) + 1)][1:]))

# Recursive function that will find all permuatiaons
def permutation(seq):
	result = [] 
	if len(seq)  <= 1:
		result.append(seq)
		return result
	else: 
		for i, j in enumerate(seq):
			rest = seq[:i] + seq[i+1:]
			perm = permutation(rest)
			for p in perm:
				result.append(j+p)	
	return result

# Output 
perms = permutation(seq)

print >> sys.stdout, len(perms)
for i in perms:
	print >> sys.stdout, " ".join(i)

# An alternative soulution would be to use Python's itertools and use the permuation method