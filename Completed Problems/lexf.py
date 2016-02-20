
# Rosalind Bioinformatics Stronghold: 
# 		23. Enumerating k-mers Lexicographically

# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n<=10)

# Return:  All strings of length n that can be formed from the alphabet, ordered lexicographically.

##################################################################################################
import sys 

### INPUT ###
input_file = sys.stdin.read().split()
seq = "".join(input_file[:-1])
n = int(input_file[-1])


### Method ###
# Recursive method to create repeating lexographic combinations.
def lex_combo(seq, n, string = '', combos = []):
	if n == 0:
		combos.append(string)
	else:
		for nuc in seq:
			n_minus = n - 1
			str_combo = string + nuc
			lex_combo(seq, n_minus, str_combo, combos)
	return combos

### OUTPUT ###
for i in lex_combo(seq, n):
	print >> sys.stdout, i