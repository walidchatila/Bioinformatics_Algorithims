# Rosalind Bioinformatics Stronghold: 
# 		23. Longest Increasing Subsequence

# Given:  A positive integer n<+10000 followed by a permutation p of length n.

# Return:  A longest increasing subsequence of p, followed by a longest decreasing subsequence of p.

##################################################################################################
import sys 

input_file = sys.stdin.read().split()
seq= map(int, input_file[1:])
length = int(input_file[0])

def longest_increasing_sub(seq, length):
	lis = [1]*length
	pos = range(length)

	for i in xrange(length):
		for j in xrange(i):
			if seq[j] < seq[i] and lis[j] + 1 > lis[i]:
				lis[i] =  lis[j] + 1
				pos[i] = j


	max_lis = max(lis)
	new_seq = []
	idx = lis.index(max_lis)
	while len(new_seq) != max_lis:
		new_seq = [seq[idx]] + new_seq
		idx = pos[idx]
	return new_seq

def longest_decreasing_sub(seq, length):
	lds = [1]*length
	pos = range(length)

	for i in xrange(length):
		for j in xrange(i):
			if seq[j] > seq[i] and lds[j] + 1 > lds[i]:
				lds[i] =  lds[j] + 1
				pos[i] = j


	max_lis = max(lds)
	new_seq = []
	idx = lds.index(max_lis)
	while len(new_seq) != max_lis:
		new_seq = [seq[idx]] + new_seq
		idx = pos[idx]
	return new_seq

print >> sys.stdout, ' '.join(map(str, longest_increasing_sub(seq, length)))
print >> sys.stdout, ' '.join(map(str, longest_decreasing_sub(seq, length)))