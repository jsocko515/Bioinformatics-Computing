# Exercise 19.1 
# Walid Chatila, 11/16/15

#Write a program using NCBI's E-Utilities to retrieve the ids of RefSeq human BRCA1 proteins from NCBI.
# 	- Use the query: "Homo sapiens"[Organism] AND BRCA1[Gene Name] AND REFSEQ

#Extend your program to search these protein ids (one at a time) vs RefSeq proteins 
# (refseq_protein) using the NCBI blast web-service

# Further extend your program to filter the results for significance (E-value < 1.0e-5) 
# and to extract mouse sequences (match "Mus musculus" in the description).

#########################################################################################################################
import os.path
from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML


###METHOD###

# Use Esearch to query NCBI protein database and retreive a list of the GI IDs
def search_NCBI(email, db, term):
	Entrez.email = email
	handle = Entrez.esearch(db=db, term=term)
	result = Entrez.read(handle)
	handle.close()
	idlist = (result["IdList"])
	return idlist 


# Blast the IDs from the above search and retreive the Alignments
#  	- You can specify database, the e-value threshold, and the organism as paramters/
def blast(blast_type, db, id_list, e_value, organism_txid):
	for y in id_list:
		if not os.path.exists(y+".xml"):
			result_handle = NCBIWWW.qblast(blast_type, db, y, expect=e_value, entrez_query="txid"+organism_txid+"[Orgn]")
			blast_results = result_handle.read()
			result_handle.close()
			file_name = y + ".xml"
			save_file = open(file_name, "w")
			save_file.write(blast_results)
			save_file.close()

# Parse the blast XML files
# Print out the Sequence description (Title) and e-value 
def blast_parser(id_list):
	for i in id_list:
		print "Query protein gi:", 	i
		result_handle = open(i+".xml")
		for blast_result in NCBIXML.parse(result_handle):
			for desc in blast_result.descriptions:
				print '****Alignment****'
				print 'sequence:', desc.title
				print "e value:", desc.e
				print 



###INPUT/OUTPUT###

# Provide and email, the database to searc, and the query 
id_list = search_NCBI("wc636@georgetown.edu", "protein", "Homo sapiens[Orgn] AND BRCA1[Gene] AND REFSEQ")

# Provide the type of blast query, the database, the sequence(s), the e-value threshold, and the organsim 
blast("blastp", "refseq_protein", id_list, 1e-5, "10090")

# provide the blast file(s)
blast_parser(id_list)
