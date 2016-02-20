# Rosalind Bioinformatics Stronghold: 
# 		7. Translating RNA into Protein

# Given:  An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

# Return: The protein string encoded by s. 
##################################################################################################

import sys 

seq = sys.stdin.readline()
# Input this table as a text file:
"""
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M---------------M---------------M----------------------------
  Base1  = UUUUUUUUUUUUUUUUCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = UUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGG
  Base3  = UCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAG
"""
input_table = sys.argv[1]

# Function that creates a dictionary of amino acids and codon pairs
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

    codons_table = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        codons_table[codon] = aa[i]
    return codons_table


codons_table = create_table(input_table)

protein = []
for i in range (0, len(seq), 3):
	codon = seq[i:i+3]
	if codons_table[codon] == "*":
		break
	else:
		protein.append(codons_table[codon])
protein = ''.join(protein)

print >> sys.stdout, protein

