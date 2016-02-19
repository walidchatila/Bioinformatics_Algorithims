# Rosalind Bioinformatics Stronghold: 
# 		4. Computing GC Content

# Given: At most 10 DNA string in FASTA format (of length at ost 1kbp each).

# Return: The ID of the string having the highest GC-content, 
#         followed by the GC-content of that string. Rosalind allows for a default error
#         of 0.001 in all decimal answers unless otherwise stated; please see the note on 
#		  absolute error below.
#######################################################################################

import sys, Bio.SeqIO 

seq_file = sys.argv[1]

file = open(seq_file)

GC = 0.0
seq_id = ""
for seq_record in Bio.SeqIO.parse(file, "fasta"):
	percent_of_GC = (float(seq_record.seq.count('G')+seq_record.seq.count('C'))) / len(seq_record.seq)* 100
	if percent_of_GC > GC:
		GC = percent_of_GC
		seq_id = seq_record.id 

print seq_id
print '%.6f' % GC