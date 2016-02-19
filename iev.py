# Rosalind Bioinformatics Stronghold: 
# 		13. Calculating Expected Offspring

# Given: Six positive integers, each of which does not exceed 20,000. 
# 	 	 The integers correspond to the number of couples in a population possessing each
#        genotype pairing for a given factor. In order, the six given integers represent 
#        the number of couples having the following genotypes:
#																AA-AA
#																AA-Aa
#																AA-aa
#																Aa-Aa
#																Aa-aa
#																aa-aa

# Return: The expected number of offspring displaying the dominant phenotype in the next generation,
#         under the assumption that every couple has exactly two offspring.
#######################################################################################
import sys

# Input File
file = sys.stdin.readline().split()


# Numbers of Couples wiht phenotypes:
couples = {}
for index, coup in enumerate(file):
	couples[index] = float(coup)


# Number of Dominant phenotype with 2 offspring 
dom_dom = 1 * 2
dom_het = 1 * 2
dom_rec = 1 * 2
het_het = 0.75 * 2
het_rec = 0.5 * 2
rec_rec = 0 * 2 

# The otal number of dominant phenotype offspring
total = ((couples[0] * dom_dom) + (couples[1] * dom_het) + 
		 (couples[2] * dom_rec) + (couples[3] * het_het) +
		 (couples[4] * het_rec) + (couples[5] * rec_rec))

# Output to File 
print >> sys.stdout, total 