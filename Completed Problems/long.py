# Rosalind Bioinformatics Stronghold: 
# 		25. Genome Assembly As Shortest Superstring

# Given:  At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format
#	     (which represent reads deriving from the same strand of a single linear chromosome)

# Return:  A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

##################################################################################################
import sys, Bio.SeqIO

### Input ###
input_seq = list(Bio.SeqIO.parse(sys.argv[1], "fasta"))
seq_list = [str(x.seq) for x in input_seq]


### Method ###
sub = seq_list[0]
length  = len(sub)
del seq_list[0]


while seq_list != []:
    for idx, seq in enumerate(seq_list):
        for sub_len in range (length, length/2, -1):
            if seq.endswith(sub[:sub_len]):
                sub = seq + sub[sub_len:] 
                del seq_list[idx]
                break
            if sub.endswith(seq[:sub_len]):
                sub = sub + seq[sub_len:] 
                del seq_list[idx]
                break

### OUTPUT ###
print >> sys.stdout,  sub 
