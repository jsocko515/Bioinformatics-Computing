# Exercise 9.1
# Walid Chatila,     10/5/15

# Write a reverse complement function (and package it up as a program) as compactly as possible, 
# using the techniques introduced today.
#############################################################################################
import sys

###INPUT###

if len(sys.argv) < 2:
	print "Please provide a DnA sequence on the comand-line."
	sys.exit(1)
input_sequence = sys.argv[1]

if len(input_sequence) < 2:
	print "This DNA sequence is too short to perform a reverse complement."
	quit() 

###METHOD###

def reverse_complement_list_comp(seq):	
	return "".join([dict(T = "A", A = 'T', C = 'G', G = 'C').get(nuc,nuc) for nuc in reversed(seq.upper())])

def reverse_complement_map(seq): 
	return "".join(map(lambda nuc: dict(T = "A", A = 'T', C = 'G', G = 'C').get(nuc,nuc), reversed(seq.upper())))

###OUTPU###

print "Reverse complement using list comprehension:", (reverse_complement_list_comp(input_sequence))
print "Reverse complement using the map method:", (reverse_complement_map(input_sequence))
