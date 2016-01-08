class codon_table:
    def __init__(self):
        self.table = {}

    def read_codons_from_filename(self, codonfile):
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
        self.table = codon_table
        return self.table


    def amino_acid(self, codon):
        try:
            return self.table[codon][0]
        except KeyError:
            return 'X'

    def is_init(self, codon):
        starts_with_start_codon = True
        try:
            self.table[codon][1]
            if self.table[codon][1] == False:
                starts_with_start_codon = False 
        except KeyError:
            starts_with_start_codon = False
        return starts_with_start_codon
   
    # Check for repeated amino acids when N is in the codon as the 3rd element, a lower-case X is used illustrate that the codon didnt match to an amino acid. 
    def aa_checker(self, codon):
        aa_check = set()
        for nuc in ['A', 'T', 'C','G']:
            new_codon = codon[:2] + nuc
            try:
                self.table[new_codon][0]
                aa_check.add(self.table[new_codon][0])

            except KeyError:
                return 'x'     
        if len(aa_check) > 1 or len(aa_check) == 0 :
                return 'x'
        return aa_check.pop().lower()

    # Find amino acid sequence and check for start codon.
    # Will now call aa_checker if a N is located as the 3rd codon, or return X if the codon is not present
    def translate(self, seq, frame):    
        # Determine the amino acid sequence
        seq += ((abs(frame)-1) * "N") 
        seqlen = len(seq)
        aaseq=[]
        for i in range(frame-1,seqlen,3):
            codon = seq[i:i+3]
            if codon[2] == 'N' and codon.count('N') == 1:
                aa = self.aa_checker(codon)
            else:
                aa = self.amino_acid(codon)
            aaseq.append(aa)
        aa_seq = ''.join(aaseq)
        return  aa_seq 
