#Excercise 5.1 
#Walid Chatila  9/21/15

#Write a command-line program to compute the reverse complement sequence for the forward #and reverse primer.
########################################################################################################################

import sys 

###INPUT###
forward_primer = sys.argv[1]
reverse_primer = sys.argv[2]

#Test Input: 

#Homo sapiens STS probe D12S341
# forward_primer = TATCCAAGCCCACCCT
# reverse_primer = ATCTTTTACTGTTATGATGAACACA

###METHOD###
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
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

###OUTPUT###
print "Reverse complement of forward primer,", forward_primer,":", reverseComplement(forward_primer)
print "Reverse complement of reverse primer,", reverse_primer,":", reverseComplement(reverse_primer)

