# Rosalind Bioinformatics Stronghold: 
# 		15. Independent Alleles

# Given: Two positive integers k (k<=7k<=7) and N(N<=2^k). In this problem, we begin with Tom, 
#		 who in the 0th generation has genotype AaBb. Tom has two children in the 1st generation, 
#		 each of whom has two children, and so on. Each organism always mates with an organism having 
#		 genotype AaBb.
# 
# Return: The probability that at least N AaBb organisms will belong to the k-th generation 
#         of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's 
#         second law holds for the factors
#############################################################################################
import sys
from math import factorial

#Input File
file = sys.stdin.readline().split()
k = int(file[0]) # generation
N = int(file[1]) # min number of organims with heterozygous 

# Calculate probablity for heterozygous using the binomial formula.
def binomial_prob(n, k):
	return (factorial(k)/(factorial(n)*factorial(k-n))) * (0.25**n) * (0.75**(k-n)) 

# Get the number of children and then add up the sum of probablities from minimum number until
# the number of children(determined by the generation)
def main(k, N):
	children = 2**k
	return sum([binomial_prob(n, children) for n in range(N, children+1)])

print >> sys.stdout, '%.3f' % main(k, N)