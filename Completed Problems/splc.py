# Rosalind Bioinformatics Stronghold: 
#       18. Computing GC Content

# Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings of s
#        acting as introns. All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s.
#         (Note: Only one solution will exist for the dataset provided.)

#######################################################################################

import sys, Bio.SeqIO

### Input ###
input_table = sys.argv[1]
input_introns = list(Bio.SeqIO.parse(sys.argv[2], "fasta"))[1:]
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

# Returns list of sorted intron positions 
def intron_finder(input_seq, input_introns):
    seq, st, lt, introns = str(input_seq), 0, 0, []
    for i in input_introns:
        intron = str(i.seq)
        st = seq.find(intron)
        lt = st + len(intron)
        introns.append([st,lt])
    introns.append([st,lt])
    return sorted(introns, key = lambda x: x[0])
    
# Removes introns and returns untranslated exon only string
def intron_remover(input_seq, introns):
    seq, st, lt, exons = str(input_seq), 0, 0, []
    for i in introns:
        #print i
        st = i[0]
        exons.append(seq[lt:st])
        lt = i[1] 
    exons.append(seq[lt:])
    return "".join(exons)
 
# Translates into protein sequence
def translate(seq):
    protein = []
    for i in range (0, len(seq), 3):
        codon = seq[i:i+3]
        if codons_table[codon][0] == "*":
            break
        else:
            protein.append(codons_table[codon][0])
    return "".join(protein)


### OUTPUT ###

codons_table = create_table(input_table)
introns = intron_finder(input_seq, input_introns)
exon_seq = intron_remover(input_seq, introns)
protein_seq = translate(exon_seq)

print >> sys.stdout, protein_seq
