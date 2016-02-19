# Rosalind Bioinformatics Stronghold: 
# 		25. Genome Assembly As Shortest Superstring

# Given:  At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format
#	     (which represent reads deriving from the same strand of a single linear chromosome)

# Return:  A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

##################################################################################################
import sys, Bio.SeqIO
import numpy as np

### INPUT ###
input_seq = list(Bio.SeqIO.parse(sys.argv[1], "fasta"))


### METHOD### 
def longest_common_substring(seq1, seq2):
	i = len(seq1)
	j = len(seq2)

	finder = np.zeros((j+1, i+1))

	for idxi, i in enumerate(seq2):
		for idxj, j in enumerate(seq1):
			if i == j:
				finder[idxi+1][idxj+1] = finder[idxi][idxj]+1
				
	max_sub = np.unravel_index(finder.argmax(), finder.shape)
	x, y = max_sub[0], max_sub[1]
	sub = ''

	while max_sub > 0.0:
		value = seq1[y-1]
		sub = value + sub
		x = x-1
		y = y-1
		max_sub = finder[x][y]
	
	new1 = seq1.replace(sub, "")
	new2 =  seq2.replace(sub, "")  
	#print seq1, seq2
	#print new1
	#print sub
	#print new2
	combined = new1 + sub + new2 

	return combined


### OUTPUT ###
for idx, i in enumerate(input_seq):
	if idx == 0:
		continue
		#lcs = longest_common_substring(" ", str(i.seq))
	elif idx == 1:
		lcs = longest_common_substring(str(input_seq[idx-1].seq), str(i.seq))
	else: 
		if str(i.seq) not in lcs:
			lcs = longest_common_substring(lcs, str(i.seq))

print >> sys.stdout, lcs 

