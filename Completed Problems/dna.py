# Rosalind Bioinformatics Stronghold: 
# 		1. Counding DNA Nucleotides

# Given: A DNA string s of length at most 1000nt.

# Return: Four integers (seperated by spaces) coudnting the respective number of times
#         that the symbols "A", "C", "G", and "T" occur in s. 
#######################################################################################

import sys

seq = sys.stdin.readline()

print seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")
