# Exercise 7.1 
# Walid Chatila, 9/28/15

# Using just the concepts introduced so far, 
# find as many ways as possible to code DNA reverse complement (at least 3!)

########################################################################################################################
import sys, string
import timeit


###INPUTS###
seq = sys.argv[1]

#Test inputs
#seq = 'CATCATGATFFFGGGFFFGGGFFFGGGNNN'
#seq = 'ATGC'
#seq = 'ATATATATGGGCCCGGGCCGGGCCGGCCGGAATTAATTTTTTTTTT'

###METHODS###

# Function that uses lists methods. 
def rev_complement_1(seq):
	seq = seq.upper()
	seq = list(seq)
	nucleotides = ["A", "T", "G", "C"]
	complements = ["T", "A", "C", "G"]
	revcomp_seq = []
	for nuc in reversed(seq):
			comp = nuc
			if nuc in nucleotides:
				comp = complements[nucleotides.index(nuc)]
			revcomp_seq.append(comp)
	return ''.join(revcomp_seq)

#Function that uses a dictionary and its methods.
def rev_complement_2(seq): 
	seq = seq.upper()
	complements = {"A":"T", "T":"A", "C":"G", "G":"C"}
	revcomp_seq = []
	for nuc in reversed(seq):
		comp = nuc
		if nuc in complements:
			comp = complements[nuc]
		revcomp_seq.append(comp)
	return ''.join(revcomp_seq)

# Function that uses strings and their methods
def rev_complement_3(seq):
	seq = seq.upper()
	nucleotides = "ATGC"
	complements = "TACG"
	revcomp_seq = ""
	for nuc in reversed(seq):
		comp = nuc
		if nuc in complements:
			comp = complements[nucleotides.index(nuc)]
		revcomp_seq += ''.join(comp)
	return revcomp_seq

# Function that uses a translation table, strings, and their mehtods.
def rev_complement_4(seq):
	seq = seq.upper()
	nucleotides = "ATGCN"
	complements = "TACGN"
	tab = string.maketrans(nucleotides,complements)
	return seq.translate(tab)[::-1]

# Function that uses strings and if statemetns 
def rev_complement_5(seq):
	seq = seq.upper()
	revcomp_seq = ''
	for nuc in reversed(seq):
		if nuc == 'A':
			comp = 'T'
			revcomp_seq += ''.join(comp)
		elif nuc == 'T':
			comp = 'A'
			revcomp_seq += ''.join(comp)
		elif nuc == 'C':
			comp = 'G'
			revcomp_seq += ''.join(comp) 
		elif nuc == 'G':
			comp = 'C'
			revcomp_seq += ''.join(comp)
		else:
			revcomp_seq += ''.join(nuc)
	return revcomp_seq

# Fucntion uses a list of tuples and list methods 
def rev_complement_6(seq):
	seq = seq.upper()
	comp = []
	nuc_comp = [('A', 'T'),('T', 'A'), ('G', 'C'), ('C','G')]
	nuc_in_seq = False
	for nuc in seq:
		for x,y in nuc_comp:
			if nuc == x:
				comp.append(y)
				nuc_in_seq = True
		if nuc_in_seq == False:
			comp.append(nuc)
		nuc_in_seq = False 
	rev_comp = list(reversed(comp))
	return ''.join(rev_comp)

###OUTPUT### 
print rev_complement_1(seq)
print rev_complement_2(seq)
print rev_complement_3(seq)
print rev_complement_4(seq)
print rev_complement_5(seq)
print rev_complement_6(seq)
