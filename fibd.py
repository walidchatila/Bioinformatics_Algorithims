# Rosalind Bioinformatics Stronghold: 
# 		11: Mortal Fibonacci Rabbits

# Given: Positive integers n<=100 and m<=20.

# Return:  The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
#######################################################################################################################
import sys

#Input
file = sys.stdin.read().split()
n = int(file[0])
m = int(file[1])

# Create list the number of months the rabit will live. 
# Offspring will be equal to the number of mature rabits (older than one month.)
mo = [0] * m
mo[0] = 1

#Starts on 2nd month
for i in range(n-1): 
	mo[0], mo[1:] = sum(mo[1:]), mo[:-1]
	  
#Output
print >> sys.stdout, sum(mo)
