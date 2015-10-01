# Exercise 5.2
# Walid Chatila   9/21/15

#Write a command-line program to test whether a PCR primer is a reverse complement palindrome.
##############################################################################################

import sys

###INPUT###
inputSeq = sys.argv[1]

#Test Case Inputs
#inputSeq1 = "TTGAGTAGACGCGTCTACTCAA"
#inputSeq2 = "ATATATATATATATAT"
#inputSeq3 = "ATCTATATATATGTAT"
#inputSeq4 = "TTGAGTAGACGTCGTCTACTCAA"
#inputSeq5 = "ATCAT"

###METHOD###
def split_seq(seq):
	half_seq_len = len(seq)/2
	if len(seq) % 2 == 0:
		seq1 = seq[:half_seq_len]
		seq2 = seq[half_seq_len:]
	else:
		seq1 = seq[:half_seq_len]
		seq2 = seq[half_seq_len + 1:]
	return seq1, seq2 

def complement(nuc):
    nucleotides = 'ACGTNacgtn'
    complements = 'TGCANtgcan'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reverseComplement(seq):
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

def check_rev_comp_palindrome(seq):
		seq = seq.upper()
		seq1, seq2 = split_seq(seq)
		reverse_comp_seq2 = reverseComplement(seq2)
		if seq1 == reverse_comp_seq2:
			print "This sequence", seq, "is a reverse complement palindrome."
		else:
			print "This sequence", seq, "is not a reverse complement palindrome."

###OUTPUT###
check_rev_comp_palindrome(inputSeq)

#Test Case Output
#check_rev_comp_palindrome(inputSeq1)
#check_rev_comp_palindrome(inputSeq2)
#check_rev_comp_palindrome(inputSeq3)
#check_rev_comp_palindrome(inputSeq4)
#check_rev_comp_palindrome(inputSeq5)