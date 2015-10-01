# Exercise 3.1
# Walid Chatila , 9/15/15
# Write a Python program to print answers to the following questions:
# -Does the SASP gene start with a Met codon?
# -Does the SASP gene have a frame 1 Met codon?
# -How many nucleotides in the SASP gene?
# -How many amino-acids in the SASP protein?
# -What is the GC content (% G or C nucleotides) of the SASP gene?
######################################################################################################################################################################################################

###INPUT###

# Anthrax sasp gene:
seq = 'TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG'

#Test Cases#

# Rice yellow mottle virus satellite, RYMV small circular viroid-like RNA hammerhead ribozyme:
#seq = "ccagctgcgcagggggcggagattttgtttcgagccttaccgacactgatgagccaagaggaacttggaggcacccaggaatttcacccgggtcgacctgggcggctaggagccgtgcacagggcgtcgctgtggagcgagcctggcctccaaggggcctggaggcgaaaccggtctgttgggaccactcggaccatcagtcatcgtgctccggcagctt"

# Hermit crab associated circular genome isolate I0085b:
#seq = """cagtattaccctccacttcgtcacaaaataacaaacgatgatttctaaacgctggtgttacactcttaacaactactctgaggatgatgtcgttaccatgaaggcggttcctaccacataccatgtgttaggtaaggaagttggtacaaacggcacaccgcatattcaaggctttttg
#actttcaagtccaataaacgcctctccgcaatgaagaagatcaatgcgcgagcgcattgggaggttgctaaaggaacgtcaaagcaagctgctgattattgcaagaaggatggaaatttcgaagaacttggctccgtcccttctcaaggaaaaaggaccgatcttgaagacgctgcagtgatgataac
#cgctggggagtcacttaaacgagtcgcggaagaacacccaaccgtcgttatcaagtatcataaaggcctctccgctcttaaatctcttctctccgaatcccgggaaaccgacgatgtacgtgggatctggctccatggcccgccagggtgtggtaaatcccatcttgc
#tcggaccgtctccccctatttgaaggctcagaacaaatggtgggatggctatgctaatgaagaatatgtcctaatcgatgacttcgataagggtggtaaatgtctcggccactatctgaagctctgggcagataaatatgaatgtactggtgaaattaaaggcgctactgtcgctctg
#aaccatcgaaaattcataatcacctcaaattaccatcccgatgagatctttgatgatgatagcgtactcctggaagctatcactcgccgtttctctatccgctcctgctggcatcactctagggaagcagacgcagtctggttcgatagtctaacaaaaaaagaagcgcacgccgcaac
#agccaataagtagaatgaattcgacagaagatctactaacatacacatcttatagagcggaggacccactggaccgcacaaacgtctctgggaaaaggcgggaaacttcccgccctctcaaaaactcctaaacaactcacgactgtaaattttgtaccgaagaatggaggat"""

# Sequence with no ATG:
#seq = "AGAGCTCGGG"

# Sequence with no frame 1 ATG:
#seq = "AGAAATG"

# Sequence with frame 1 ATG:
#seq = "cccatgggg"

# Sequence with no G or C:
#seq = "atatatatat"

###METHOD###

# Make the sequence uppercase
def seq_upper(seq):
    return seq.upper()

# Does the gene start with a Met codon?
def start_met(seq):
    seq = seq_upper(seq)
    initMet = seq.startswith('ATG')
    if initMet:
        print "The gene does start with Met('ATG')."
    else:
        print "The gene does not start with Met('ATG')."

# Does the gene have a frame 1 Met codon?
def frame_1_met(seq):
    seq = seq_upper(seq)
    frame = (seq.find('ATG') % 3) + 1
    if frame == 1:
        print "The gene does have a frame 1 Met codon."
    else:
        print "The gene does not have a frame 1 Met codon."

# How many nucleotides in the gene?
def length_nucleotide(seq):
    seq = seq_upper(seq)
    print "There are", len(seq),"nucleotides in the gene."

# How many amino-acids in the protein?
def total_amino_acids(seq):
    seq = seq_upper(seq)
    print "There are", len(seq)/3 , "amino acids in the protein."

# What is the GC content (% G or C nucleotides) of the gene?
def percent_GC(seq):
    seq = seq_upper(seq)
    percent_of_GC= (float(seq.count('G')+seq.count('C'))) / len(seq)* 100
    print "The GC content of the gene:", percent_of_GC ,"%"

###OUTPUT###
    
start_met(seq)
frame_1_met(seq)
length_nucleotide(seq)
total_amino_acids(seq)
percent_GC(seq)

