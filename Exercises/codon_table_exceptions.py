def read_codons_from_filename(codonfile):
    file = open(codonfile)
    data = {}
    for column in file:
        split_column = column.split()
        key = split_column[0]
        value = split_column[2]
        data[key] = value    
    file.close()
    
    b1 = data['Base1']
    b2 = data['Base2']
    b3 = data['Base3']
    aa = data['AAs']
    st = data['Starts']

    codon_table = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        isInit = (st[i] == 'M')
        codon_table[codon] = (aa[i], isInit)
    return codon_table

# Check for repeated amino acids when N is in the codon as the 3rd element, a lower-case X is used illustrate that the codon didnt match to an amino acid. 
def aa_checker(codon_table, codon):
    aa_check = set()
  
    for nuc in ['A', 'T', 'C','G']:
        new_codon = codon[:2] + nuc
        try:
            codon_table[new_codon][0]
        except KeyError:
            return 'x'
    aa_check.add(codon_table[new_codon][0]) 
    if len(aa_check) > 1 or len(aa_check) == 0 :
            return 'x'
    return aa_check.pop().lower()

# Find amino acid sequence and check for start codon.
# Will now call aa_checker if a N is located as the 3rd codon, or return X if the codon is not present
def amino_acid_seq(seq, frame, codon_table):    
    # Determine the amino acid sequence
    seq += ((abs(frame)-1) * "N") 
    seqlen = len(seq)
    aaseq=[]
    for i in range(frame-1,seqlen,3):
        codon = seq[i:i+3]
        if codon[2] == 'N' and codon.count('N') == 1:
            aa = aa_checker(codon_table, codon)
        else:
            try:
                aa = codon_table[codon][0]
            except KeyError:
                aa = 'X'
        aaseq.append(aa)
    aa_seq = ''.join(aaseq)
   
    # Check for start codon validity
    start_codon = seq[0:3]
    starts_with_start_codon = True
    try:
        codon_table[start_codon][1]
    except KeyError:
        starts_with_start_codon = False 
 
    return  dict(aa_seq = aa_seq, start_codon=starts_with_start_codon)

# Will translate the sequence for each of the frames
def frames(seq, reverse_complement, codon_table): 
    frames = {}
    for frame in [1,2,3]:
        frames[frame] = amino_acid_seq(seq, frame, codon_table)
        frames[-frame] = amino_acid_seq(reverse_complement, frame, codon_table)
    return frames