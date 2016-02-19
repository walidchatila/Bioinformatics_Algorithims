# Walid Chatila
# Rosalind Bioinformatics Stronghold: 
# 		3. Complementing a Strand of DNA
# 
# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement of s. 
###############################################################################################################

import sys

DNA_seq = sys.stdin.read()

def reverse_complement(seq): 
	return "".join(map(lambda nuc: dict(T = "A", A = 'T', C = 'G', G = 'C').get(nuc,nuc), reversed(seq.upper())))

rev_comp = reverse_complement(DNA_seq)

print >> sys.stdout, rev_comp