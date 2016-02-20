# Rosalind Bioinformatics Stronghold: 
# 		10. Consensus and Profile

# Given:  A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection.
#         (If several possible consensus strings exist, then you may return any one of them.). 
##################################################################################################
import sys, Bio.SeqIO 

# Input
seq_file = sys.argv[1]

# Create empty lists of zeros
file = open(seq_file)
for seq_record in Bio.SeqIO.parse(file, "fasta"):
	len_seq = len(seq_record.seq)
	break
file.close()

A = [0] * len_seq
C = [0] * len_seq
G = [0] * len_seq
T = [0] * len_seq


# Populate the lists based nucleotides
file = open(seq_file)
for seq_record in Bio.SeqIO.parse(file, "fasta"):
	#print seq_record.seq, seq_record.id
	for index, nuc in enumerate(seq_record.seq):
		#print nuc 
		if nuc == "A":
			A[index] += 1
		elif nuc == "C":
			C[index] += 1
		elif nuc == "G":
			G[index] += 1
		else: 
			T[index] += 1
file.close()

# Create Consenus Sequence
consensus_seq = ""
for i in range(len_seq): 
	consensus_checker = ("A", A[i])
	if C[i] > consensus_checker[1]:
		consensus_checker = ("C", C[i])
	if G[i] > consensus_checker[1]:
		consensus_checker = ("G", G[i])
	if T[i] > consensus_checker[1]:
		consensus_checker = ("T", T[i])
	consensus_seq += consensus_checker[0]

print consensus_seq
print "A:",  ' '.join(map(str, A))
print "C:", ' '.join(map(str, C))
print "G:", ' '.join(map(str, G))
print "T:", ' '.join(map(str, T))