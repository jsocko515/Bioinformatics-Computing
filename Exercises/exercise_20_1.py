# Exercise 20.1
# Walid Chatila  11/23/15

#Find potential fruit fly / yeast orthologs
	#download the files and uncompress them
	#serach fruit fly ribosomal proteins against yeast ribosomal proteins
	#for each fruit fly query, ooutput the best yeast protein if it has a significant E-Value.
		#What ribosomal protein is most highly conserved between fruity fly and yeast. 
#################################################################################################
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIXML
import os, os.path, sys
###Input and Method###
#blast_prog = os.path.join("C:\\", "progra~1", "NCBI", "blast-2.2.31+", "bin", "blastp") #windows
blast_prog = '/usr/bin/blastp' #linux
blast_query = "drosoph-ribosome.fasta"
blast_db = 'blastdb/yeast-ribosome.fasta'

cmdline = NcbiblastpCommandline(cmd=blast_prog,
								query=blast_query,
								db=blast_db,
								outfmt=5,
								out ="results.xml")

stdout, stderr = cmdline()
result_handle = open("results.xml")

significant = {}
for blast_result in NCBIXML.parse(result_handle):
	top_alignmenet = blast_result.alignments[0]
	top_hsp = top_alignmenet.hsps[0]	
	if top_hsp.expect < 1e-10:
		significant[blast_result.query] = [top_alignmenet.title, top_hsp.expect, top_hsp.identities]
		print "Query Protein:", blast_result.query
		print "Alignment:"
		print top_alignmenet.title
		print top_hsp.expect
		print 
	
best_e = min([y[1] for x, y in significant.items()])
best_score =  [(x, y) for x, y in significant.items() if y[1] == best_e]
top_hit = 0
best_query =''
best_alignment=''
for i in best_score: 
	if (i[1][2]) > top_hit:
		top_hit = (i[1][2])
		best_query = (i[0])
		best_alignment = (i[1][0])


###OOUTPUT###
print "The most highly conserved:"
print "The query protein: ", best_query
print "The alignment protein:",best_alignment