#Exercise 2.2
# Walid Chatila, 9/9/15

# Write a python program to find the position and the translation frame number
# of the first start-codon in the DNA sequence:
# gcatcacgttatgtcgactctgtgtggcgtctgctggg

################################################################################

###INPUT##

# The DNA sequence being analzyed has to be inputed.
# The start codon, Methionine (atg) has to be inputed as well.

dna_sequence = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"

# Test Cases:
#dna_sequence = "atg"
#dna_sequence = "aatg"
#dna_sequence = "aaatg"
#dna_sequence = "aaaatg"
#dna_sequence = "GCATCACGTTATGTCGACTCTGTGTGGCGTCTGCTGG
#dna_sequence = "aaaaaaaaaaaa"
#dna_sequence = "123456"
#dna_sequence = "aaaatgaaaatg"


start_codon  = "atg"

###COMPUTATION###

# The FIND method will be used to find the first instance of the start codon.
instance_of_start_codon = dna_sequence.find(start_codon) 

# Modulus wil be used to find the translation frame of the start codon.
translation_frame = (instance_of_start_codon  % 3) + 1

# This addition of one will give the actual position of the start codon. 
position_of_start_codon = instance_of_start_codon + 1

###OUTPUT###

print "The DNA sequence being analyzed is,", dna_sequence
print "The position of the start codon is,", position_of_start_codon
print "The translation frame number of the first start codon is,", translation_frame

