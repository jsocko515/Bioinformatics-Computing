# Exercise 7.2
# Walid Chatila,   9/28/15

# Write a program that takes a codon table file (such as standard.code from the lecture) and a file containing nucleotide sequence (anthrax_sasp.nuc) as command-line arguments, 
# and outputs the amino-acid sequence.

#############################################################################################################################################
import sys
### Input
input_table = sys.argv[1]
input_seq = sys.argv[2]

#Test Input
#input_table = 'standard.code'
#input_table = 'bacterial.code'
#input_seq = 'anthrax_sasp.nuc'

###METHOD###

# Create Table Function
# Open the codon table file and read into a dictionary
# Also create a start codon dictionary
def create_table(table):
    
    table = open(table)
    data = {}
    for column in table:
        split_column = column.split()
        key = split_column[0]
        value = split_column[2]
        data[key] = value    
    table.close()
    
    b1 = data['Base1']
    b2 = data['Base2']
    b3 = data['Base3']
    aa = data['AAs']
    st = data['Starts']
    
    codons = {}
    init = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        codons[codon] = aa[i]
        init[codon] = (st[i] == 'M')

    # Return the codons dictionary and the init dictionary using the dict() constructor
    return dict(codon_table = codons, init_table = init)

# Find amino acid sequence and check for start codon.
# Use the codon table to find the amino acid seuquecne of an inputted sequence.
# Find out if the first start codon is listed as such in the codon table.
def amino_acid_seq(seq):    
    # Determine the amino acid sequence
    codons = output['codon_table']
    init = output['init_table']
    seq_file = open(seq)
    sequence = ''.join(seq_file.read().split())
    seq_file.close()
    seqlen = len(sequence)

    aaseq = []
    for i in range(0,seqlen,3):
        codon = sequence[i:i+3]
        aa = codons[codon]
        aaseq.append(aa)
    aa_seq = ''.join(aaseq)
    # Check for start codon validity
    start_codon = sequence[0:3]
    if init[start_codon]:
        starts_with_start_codon = True

    else:
        starts_with_start_codon = False

   #Return the original sequence, aa_seq and start_codon using the dict() constructor
    return  dict(sequence = sequence, aa_seq = aa_seq, start_codon=starts_with_start_codon)


output = create_table(input_table)
print output
output = amino_acid_seq(input_seq)
print output
###OUTPUT###
print "The original sequence:", output["sequence"], "."
print " The amino acid sequence:", output["aa_seq"], "."
print " Is the first codon of the sequce a valid start codon?", output["start_codon"]