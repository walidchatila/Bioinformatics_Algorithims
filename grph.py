# Rosalind Bioinformatics Stronghold: 
# 		12. Overlap Graphs

# Given: A collection of DNA string in FASTA format having total length at most 10 kbp.

# Return: The adjacency list corresponding to O3. You may return edges in any order. 
#######################################################################################
import sys ,  Bio.SeqIO
file = open(sys.argv[1], "rU")

records =  Bio.SeqIO.to_dict(Bio.SeqIO.parse(file, "fasta"))
adjacency_list = []
for rec, attrib in records.items():
	# Check pottential overalapping sequences and add to list
	list_overlap = [(seq.id, seq.seq) for seq in records.values() if attrib.seq[-3:] in seq.seq[0:3]]
	for i in list_overlap:
		# Make sure there are no directed loops
		if i[0] != rec: 
			adjacency_list.append((rec, i[0]))

for edges in adjacency_list:
	print >> sys.stdout, edges[0], edges[1]