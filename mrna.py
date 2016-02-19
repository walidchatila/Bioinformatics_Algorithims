# Rosalind Bioinformatics Stronghold: 
# 		17. Inferring mRNA from Protein

# Given: A protein string of length at most 1000 aa.


# Return: The total number of different RNA strings from which the protein could have been translated,
#         modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

##################################################################################################
import sys

# Input protein sequence
seq = sys.stdin.read().strip()

#Create the Amino Acid Frequency Table, * stands for stop codon
AAs    = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
Starts = '---M---------------M---------------M----------------------------'
Base1  = 'UUUUUUUUUUUUUUUUCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2  = 'UUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGG'
Base3  = 'UCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAG'

aa_freq = {}
for i in AAs:
	if not aa_freq.has_key(i):
		aa_freq[i] = 0
	aa_freq[i] += 1

# Number of Stop Codons
variations = aa_freq['*']

# Determin the number of varying mRNA sequences
for prot in seq:
	variations *= aa_freq[prot]

# Retun Number of vaiations modulo 1,000,000
print >> sys.stdout, variations % 1000000 