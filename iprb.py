# Rosalind Bioinformatics Stronghold: 
# 		6. Mendel's First Law

# Given: Three positive integers k, m, and n, representing a population containing
#        k+m+n organisms: k individuals are homozygous dominant for a factor,
#        m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce
#         an individual possessing a dominant allele (and thus displaying the dominant phenotype).
#         Assume that any two organisms can mate.
##################################################################################################

import sys

file = sys.stdin.readline().split()

k = float(file[0]) # Homozygous Dominant Population
m = float(file[1]) # Heterozygous Population
n = float(file[2]) # Homozygous Recessive Population

# Total Population(and minus 1)
pop = k + m + n 
pop_neg_1 = pop - 1

# homozygous dominant first 
homd = (k/pop)

# heterozygous first
het_homd = (m/pop)*(k/pop_neg_1)
het_het = (m/pop)*((m-1)/pop_neg_1)*(.75)
het_homr = (m/pop)*(n/pop_neg_1)*(.5)
total_het = het_homd + het_het + het_homr

# homozygous recessive first
homr_homd = (n/pop)*(k/pop_neg_1)
homr_het = (n/pop)*(m/pop_neg_1)*(.5)
total_homr = homr_homd + homr_het 


# probability of dominant phenotype
probablity = homd + total_het + total_homr 

print >> sys.stdout, '%.5f' % probablity