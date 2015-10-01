#Exercise 4.1
#Walid Chatila, 9/21/15

# Write a Python program to compute the reverse complement of a codon

###################################################################################################
import sys
###INPUT###

#Input of Methionine (start codon) "ATG".
input_codon = sys.argv[1]

#TEST INPUTS
#input_codon = "atg"
#input_codon = "ATG"
#input_codon = "AATTGG"
#input_codon = "ANF"

###COMPUTATION###

# Takes in a nucleotide and returns its complement
def complement(nuc):
    if nuc == 'A' or nuc == 'a':
        comp = 'T'
    elif nuc == 'T' or nuc == 't':
        comp = 'A'
    elif nuc == 'C' or nuc == 'c':
        comp = 'G'
    elif nuc == 'G' or nuc == 'g':
        comp = 'C'
    elif nuc == 'N' or nuc == 'n':
        comp = 'N'
    else:
        comp = nuc 
    return comp

# Takes in a codon and rerturns its reverse complement
def reverse_complement(codon):
    codon = codon.upper()
    first_nucleotide  = codon[0]
    second_nucleotide = codon[1]
    third_nucleotide  = codon[2]
    comp_first_nucleotide = complement(first_nucleotide)
    comp_second_nucleotide = complement(second_nucleotide)
    comp_third_nucleotide = complement(third_nucleotide)
    reversed_comp_codon = comp_third_nucleotide + comp_second_nucleotide + comp_first_nucleotide
    return reversed_comp_codon

    

###OUTPUT###
print "The reverse complement of", input_codon, ":", reverse_complement(input_codon)





