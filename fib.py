# Rosalind Bioinformatics Stronghold: 
# 		4. Rabbits and Recurrence Relations

# Given: Positive integers n<=40 and k<=5

# Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation,
#         every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)
#######################################################################################
import sys

file = sys.stdin.read()

n = file.split(" ")[0]
k = file.split(" ")[1] 

f1 = 1
f2 = 1
for i in range(int(n)): 
	if i < 2:
		continue 
	fn = (f1*int(k)) + f2
	f1 = f2 
	f2 = fn

	

print fn 