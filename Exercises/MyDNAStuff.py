# Read sequence from file
def read_seq_from_file(seq_filename):
	seq_file = open(seq_filename)
	dna_seq = ''.join(seq_file.read().split())
	dna_seq = dna_seq.upper()
	seq_file.close()
	return dna_seq

# Make the sequence uppercase
def seq_upper(seq):
    return seq.upper()

# How many nucleotides in the sequence?
def length_seq(seq):
	return len(seq)

# Sequence Complement 
def complement(seq):
	comp_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	return ''.join(map(comp_dict.get, seq))

# Reversed Sequence:
def reversed_seq(seq):
	return ''.join(reversed(seq))

# Reverse Complement:
def reverse_comp(seq):
	return complement(reversed_seq(seq))

# Does the sequence start with a start codon?
def start_met(seq):
    if seq.startswith('ATG'):
    	return True
    else:
    	return False 

 # Does the sequence have a frame 1 Met codon?
def frame_1_met(seq):
    if ((seq.find('ATG') % 3) + 1) == 1:
        return True
    else:
    	return False 

# How many amino-acids in the seq/protein?
def total_amino_acids(seq):
    return len(seq)/3 

# What is the GC content (% G or C nucleotides) of the sequence?
def percent_GC(seq):
    return ((float(seq.count('G')+seq.count('C'))) / len(seq)* 100)
    


# The next two fucntiosn are Used for checking Tandem Repeats
def check_repeat(seq, section_size):
	repeat = seq[:section_size]
	number_of_repeats = len(seq)/section_size
	if seq == (repeat * number_of_repeats):
		return True
	else:
		return False
###call this one###
def check_for_tandem(seq):
	yes = 0
	seq = seq.upper()
	for section in range (1, len(seq)):
		if len(seq) % section == 0:
			number_of_repeats = len(seq)/section
			if check_repeat(seq, section):
				yes = 1 
				return True
				break 
	if yes == 0:
		return False 

# The next two functions are for checking if a sequence is a Reverse Complement Palindrome
def split_seq(seq):
	half_seq_len = len(seq)/2
	if len(seq) % 2 == 0:
		seq1 = seq[:half_seq_len]
		seq2 = seq[half_seq_len:]
	else:
		seq1 = seq[:half_seq_len]
		seq2 = seq[half_seq_len + 1:]
	return seq1, seq2 
###call this one###
def check_rev_comp_palindrome(seq):
		seq = seq.upper()
		seq1, seq2 = split_seq(seq)
		reverse_comp_seq2 = reverse_comp(seq2)
		if seq1 == reverse_comp_seq2:
			return True
		else:
			return False 