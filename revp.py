# Rosalind Bioinformatics Stronghold: 
#       21: Loading Restriction Sites

# Given: A DNA string s of length at most 1kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the string having length 
#         between 4 and 12. You may return these pairs in any order.
######################################################################################
import sys, Bio.SeqIO

# Input 
seq = list(Bio.SeqIO.parse(sys.argv[1], "fasta"))[0].seq

# Will Split the sequence in half and return two sequences, also chacks for even/odd
def split_seq(seq):
	half_seq_len = len(seq)/2
	if len(seq) % 2 == 0:
		seq1 = seq[:half_seq_len]
		seq2 = seq[half_seq_len:]
	else:
		seq1 = seq[:half_seq_len]
		seq2 = seq[half_seq_len + 1:]
	return seq1, seq2 

# Returns a reverse complement 
def rev_complement(seq):
    return "".join(map(lambda nuc: dict(T = "A", A = 'T', C = 'G', G = 'C').get(nuc,nuc), reversed(seq.upper())))

# Will check if it is a reverse palindrome
def check_rev_comp_palindrome(seq):
		seq1, seq2 = split_seq(seq)
		reverse_comp_seq2 = rev_complement(seq2)
		if seq1 == reverse_comp_seq2:
			return True
		else:
			return False 

# Checks all chunks of 4, 6, 8, 10, 12 for reverse palindormes 
def checker(seq, idx):
	rev_pal = []
	for num in [4,6,8,10,12]:
		chunk = seq[idx:idx+num]
		if check_rev_comp_palindrome(chunk) == True and len(chunk) == num:
			rev_pal.append((idx+1, num))
	return rev_pal

all_rev = []
for idx, nuc in enumerate(seq):
	all_rev += checker(seq, idx)
	
# Output 
for i in all_rev:
	print >> sys.stdout, i[0], i[1]

