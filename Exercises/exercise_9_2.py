# Exercise 9.2
# Walid Chatila, 10/5/15

#Write a program to compute and output the frequency of each nucleotide 
# in a DNA sequence using a dictionary,Output the frequencies in most-occurrences to least-occurrences order.
#############################################################################################################

import sys

###INPUT###

if len(sys.argv) < 2:
	print "Please provide a DnA sequence on the comand-line."
	sys.exit(1)
input_sequence = sys.argv[1]

###METHOD###

def count_freq(sequence):
	count = {}
	for nuc in sequence.upper():
		count[nuc] = count.get(nuc, 0) + 1
	freq = []
	[freq.append((keys,values)) for keys, values in sorted(count.items(), key = lambda p: p[1], reverse = True)]
	return freq	 


###OUTPUT###

for pairs in count_freq(input_sequence):
	print "For the nucleotide", pairs[0], "the frequency is", pairs[1]
