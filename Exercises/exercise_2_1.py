#Exercise 2.1
#Walid Chatila, 9/9/15

# Write a python program to print out the codon for Methionine (aka the start
# codon) backwards in lower-case symbols.
# - Represent Methionine as string variable codon = "ATG".
# - Use only the techniques shown in lecture.

###################################################################################################

###INPUT###

#Input of Methionine (start codon) "ATG".
start_codon = "ATG"

# Other tested Inputs
# Numbers, different letter, different cases, and symbols will be inputed in the form of a string. 
#start_codon = "atg"
#start_codon = "123"
#start_codon = "ZZZ"
#start_codon = "ABC"
#start_codon = "abc"
#start_codon = "?!@"
#start_codon = 123
#start_codon = abc

###COMPUTATION###

# After the input, the codon is broken into the three nucleotides.

first_nucleotide  = start_codon[0]
second_nucleotide = start_codon[1]
third_nucleotide  = start_codon[2]

# The individual nucleotides are reassembled in the reverse order 

reversed_start_codon = third_nucleotide + second_nucleotide + first_nucleotide

# The reversed codon is changed from uppercase to lower case.

reversed_lowercase_start_codon = reversed_start_codon.lower()


###OUTPUT###

# After all the computation on the start codon is complete,
# the lower-case reversed start codon is printed out.

print "This is the original start codon,", start_codon
print "This is the reversed start codon,", reversed_start_codon
print "This is the reversed lowercase start codon,", reversed_lowercase_start_codon


