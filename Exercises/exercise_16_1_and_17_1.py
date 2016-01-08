# Exercise 16.1/17.1
# Walid Chatila, 11/9/15

# 16.1:
# Add some try/except blocks in your DNA and codon_table modules from Lecture 15.

# 17.1:
# Convert your modules for DNA sequence and codons to a codon_table and DNASeq class.
# Demonstrate the use of this module and the codon table module to translate an amino-acid
# sequence in all six-frames with just a few lines of code.

##################################################################################################################################

import sys
from codon_table_class import codon_table
from DNASeq import DNAseq



###INPUT###
codons = codon_table()
sequence = DNAseq()

try:
	table = codons.read_codons_from_filename(sys.argv[1])
except IndexError:
	print "Please provide a codon table file on the command-line"
	sys.exit(1)
except IOError:
	print "Cant find the codon table file."
	sys.exit(1)


try:
	seq = sequence.read_seq_from_file(sys.argv[2])
except IndexError:
	print "Please provide a DNA sequence file on the command-line"
	sys.exit(1)
except IOError:
	print "Cant find the sequence file."
	sys.exit(1)






###METHOD and OUTPUT###
if codons.is_init(seq[:3]):
	print "Initial codon is a valid initiation codon."
else: 
	print "Initial codon is NOT a valid initiation codon"

for frame in [1,2,3]:
	print "Frame", frame, "(Forward):", codons.translate(seq, frame)
	print "Frame", -frame, "(Reverse):", codons.translate(sequence.reverse_comp(), frame)