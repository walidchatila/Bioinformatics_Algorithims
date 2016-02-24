# Rosalind Bioinformatics Stronghold: 
# 		26. Introduction to RNA Folding

# Given: An RNA string s of length at most 80 bp having the same number of occurrences of 
#       'A' as 'U' and the same number of occurrences of 'C' as 'G'.

# Return:  The total possible number of perfect matchings of basepair edges in the bonding graph of s.
##################################################################################################
from math import factorial as fact
import Bio.SeqIO, sys 

### Input ###
seq = list(Bio.SeqIO.parse(sys.argv[1], "fasta"))[0].seq

# Since the numbers of A-U and C-G are the same, we only need to count for one of them
num_A = seq.count("A")
num_G = seq.count("G")

# the factorial represents the numbers of combinations that you can pair A-U, or G-C
# the two numbers are multiplied to come up with all possible combinations
perfect_match = fact(num_A) * fact(num_G)

print >> sys.stdout, perfect_match
