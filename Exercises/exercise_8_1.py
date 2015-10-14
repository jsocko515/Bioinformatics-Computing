# Exercise 8.1
# Walid Chatila,   10/5/15

# Modify your DNA translation program to translate in each forward frame (1,2,3)
# Modify your DNA translation program to translate in each reverse translation frame too.
# Modify your translation program to handle 'N' symbols in the third position of a codon
# If all four codons represented correspond to the same amino-acid, then output that amino-acid. Otherwise, output 'X'.

#############################################################################################################################################

import sys
### Input ###

if len(sys.argv) < 3:
    print "Please provide a file for the code table and a file for the DNA sequence on the comand-line."
    sys.exit(1)
input_table = sys.argv[1]
input_seq = sys.argv[2]

#Test Input
#input_table = 'standard.code'
#input_table = 'bacterial.code'
#input_seq = 'anthrax_sasp.nuc'

###METHOD###

# Open the codon table file and read into a dictionary
# Also create a start codon dictionary: init 
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
    return dict(codon_table = codons, init_table = init)

# Open the sequence file and store in a variable
def sequence(seq):
    seq_file = open(seq)
    sequence = ''.join(seq_file.read().split())
    seq_file.close()
    return sequence

# Find the reverse complement of a sequence 
def rev_complement(seq):
    #return "".join([dict(T = "A", A = 'T', C = 'G', G = 'C').get(nuc,nuc) for nuc in reversed(seq.upper())])
    return "".join(map(lambda nuc: dict(T = "A", A = 'T', C = 'G', G = 'C').get(nuc,nuc), reversed(seq.upper())))
  


# Check for repeated amino acids when N is in the codon as the 3rd element  
def aa_checker(codons, codon):
    aa_check = set()
    for nuc in ['A', 'T', 'C','G']:
        new_codon = codon[:2] + nuc
        aa_check.add(codons[new_codon])
    if len(aa_check) > 1:
        return 'X'
    return aa_check.pop()


# Find amino acid sequence and check for start codon.
# Will now call aa_checker if a N is located as the 3rd codon, or return X if the codon is not present
def amino_acid_seq(seq, frame, codons, init):    
    # Determine the amino acid sequence
    seq = ((abs(frame)-1) * "N") + seq
    seqlen = len(seq)
    aaseq=[]
    for i in range(frame-1,seqlen,3):
        codon = seq[i:i+3]
        if codon in codons:
            aa = codons[codon]
        elif codon[2] == 'N' and codon.count('N') == 1:
            aa = aa_checker(codons, codon)
        else:
            aa = 'X'
        aaseq.append(aa)
    aa_seq = ''.join(aaseq)
   
    # Check for start codon validity
    start_codon = seq[0:3]
    if start_codon in init and init[start_codon]:
        starts_with_start_codon = True
    else:
        starts_with_start_codon = False
    return  dict(aa_seq = aa_seq, start_codon=starts_with_start_codon)

# Find the amino acid sequence for all frames (1, 2, 3, -1, -2, -3)
def frames(seq, reverse_complement, codons, init): 
    frames = {}
    for frame in [1,2,3]:
        frames[frame] = amino_acid_seq(seq, frame, codons, init)
        frames[-frame] = amino_acid_seq(reverse_complement, frame, codons, init)
    return frames
  

###OUTPUT###
tables = create_table(input_table)
sequence = sequence(input_seq)
rev_comp_seq = rev_complement(sequence)
frames = frames(sequence, rev_comp_seq, tables['codon_table'], tables['init_table'])

print "The original sequence:", sequence,"."
print
for i in (frames):
    print " The amino acid sequence of frame", i,":", frames[i]["aa_seq"], "."
    print " Is the first codon of the frame", i, "sequce a valid start codon?", frames[i]["start_codon"]
    print
