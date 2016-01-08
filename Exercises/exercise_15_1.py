# Exercise 15.1
# Walid Chatila, 11/2/15
# Create MyDNAStuff module
# Create codon_table module
# Demonstrate the use of these modules to translate an amino-acid sequence in all six-frames with just a few lines of code.
##################################################################################################################################

import MyDNAStuff, codon_table, sys

###INPUT###
if len(sys.argv) < 3:
	print "Require codon table and DNA sequence on the command-line."
	sys.exit(1)

table = codon_table.read_codons_from_filename(sys.argv[1])
seq = MyDNAStuff.read_seq_from_file(sys.argv[2])

###METHOD###
frames = codon_table.frames(seq, MyDNAStuff.reverse_comp(seq), table)


###OUTPUT###
print "The original sequence:", seq, "."
print 
for i in frames:
	print " The amino acid sequence of frame", i,":", frames[i]["aa_seq"], "."
	print " Is the first codon of the frame", i, "sequce a valid start codon?", frames[i]["start_codon"]
	print
