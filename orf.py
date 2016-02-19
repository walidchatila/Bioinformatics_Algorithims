# Rosalind Bioinformatics Stronghold: 
#       18. Computing GC Content

# Given: A DNA string s of length at most 1kbp in FASTA format.

# Return: Every distinct candidate protein string that can be translated from ORFs of s.
#         Strings can be returned in any order.

#######################################################################################

import sys, Bio.SeqIO

### Input ###
input_table = sys.argv[1]
input_seq = list(Bio.SeqIO.parse(sys.argv[2], "fasta"))[0].seq

###METHOD###

# Open the codon table file and read into a dictionary
# Create tuples for each codon including if it is a start codon.
# Stop codons are the "*"
def create_table(table):
    table = open(table)
    data = {}
    for column in table:
        split_column = column.split()
        key = split_column[0]
        value = split_column[2]
        data[key] = value    
    table.close()
    
    b1 = data['Base1']
    b2 = data['Base2']
    b3 = data['Base3']
    aa = data['AAs']
    st = data['Starts']

    codons = {}
    init = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        isInit = (st[i] == 'M')
        codons[codon] = (aa[i], isInit)
    return codons

# Find the reverse complement of a sequence 
def rev_complement(seq):
    return "".join(map(lambda nuc: dict(T = "A", A = 'T', C = 'G', G = 'C').get(nuc,nuc), reversed(seq.upper())))
  


# Find all open reading frame sequences for a given frame 
def amino_acid_seq(seq, frame, codons):    
    seqlen = len(seq)
    seq_list=[]
    all_seq = []
    new = 0
    for i in range(frame-1,seqlen,3):
        if len(seq[i:i+3]) == 3:
            codon = seq[i:i+3]
            if codons[codon][1]:
                new += 1
                seq_list.append([])
            if new != 0 and codons[codon][0] != "*" and seq_list != []:
                for i in seq_list:
                    i.append(codons[codon][0])               
            
            if codons[codon][0] == "*":
                for i in seq_list:
                    aa_seq = ''.join(i)
                    if len(aa_seq) > 0:
                        all_seq.append(aa_seq)
                seq_list = []
                new = 0 
    return all_seq


# Find the postive open reading frames
def pos_frames(seq_set, seq, codons): 
    for frame in [1,2,3]:
        for i in amino_acid_seq(seq, frame, codons):
            seq_set.add(i)
    return seq_set
# Find the negative open reading frames
def neg_frames(seq_set, reverse_complement, codons): 
    for frame in [-1,-2,-3]:
        for i in amino_acid_seq(reverse_complement, frame, codons):
            seq_set.add(i)
    return seq_set
  
###OUTPUT###
tables = create_table(input_table)
rev_comp_seq = rev_complement(input_seq)
seq_set = set()
seq_set = pos_frames(seq_set, input_seq, tables)
seq_set = neg_frames(seq_set, rev_comp_seq, tables)

for i in seq_set:
    print >> sys.stdout, i