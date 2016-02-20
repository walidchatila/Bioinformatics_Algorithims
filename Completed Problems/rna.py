# Walid Chatila
# Rosalind Bioinformatics Stronghold
# 2. Transcribing DNA into RNA

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t. 
#############################################################################

import sys

DNA_seq = sys.stdin.read()

RNA_seq = DNA_seq.replace("T", "U")

print >> sys.stdout, RNA_seq
