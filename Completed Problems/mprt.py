# Rosalind Bioinformatics Stronghold: 
# 		16. Finding a Protein Motif

# Given: At most 15 UniProt Protein Database access IDs.
#		 
# 
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed 
#          by a list of locations in the protein string where the motif can be found. 

#############################################################################################
import sys, urllib, Bio.SeqIO



# Create list of tuples with ID and URLS
def url_list_creater(file):
	url_list = []
	for u_id in file:
		url = 'http://www.uniprot.org/uniprot/'+u_id+'.fasta'
		url_list.append((u_id, url))
	return url_list

# Return Motif postions
def motif_checker(url_list):
	motif_pos = []
	for url in (url_list):
		handle = urllib.urlopen(url[1])
		prot = Bio.SeqIO.read(handle,"fasta").seq
		handle.close()
		positions = []
		for idx, nuc in enumerate(prot):
			motif = prot[idx:idx+4]
			if (len(motif) == 4) and (motif[0] == "N") and (motif[1] != "P") and \
				(motif[2] == "S" or motif[2] == "T") and (motif[3] != "P"):
					positions.append(idx + 1)

		motif_pos.append((url[0] , positions))
			
	return motif_pos



### input ### 
file =  sys.stdin.read().split()
url_list = url_list_creater(file)
motifs = motif_checker(url_list)

### output ###
for i in motifs:
	if i[1] != []:
		print >> sys.stdout, i[0]
		print >> sys.stdout, " ".join([str(m) for m in i[1]])  
		