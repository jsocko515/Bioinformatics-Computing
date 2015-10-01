#Exercise 4.2
#Walid Chatila   9/21/15

#Write a Python program to determine whether or not a DNA sequence 
#consists of a (integer) number of (perfect) "tandem" repeats.
#######################################################################################################

import sys
###INPUT###
input_seq = sys.argv[1]

#Test Inputs
#seq1 = "AAAAAAAAAAAAAAAA"
#seq2 = "CACACACACACACAC"
#seq3 = "ATTCGATTCGATTCG"
#seq4 = "GTAGTAGTAGTAGTA"
#seq5 = "TCAGTCACTCACTCAG"

###METHOD###

def check_repeat(seq, section_size):
	repeat = seq[:section_size]
	number_of_repeats = len(seq)/section_size
	if seq == (repeat * number_of_repeats):
		return True
	else:
		return False

def check_for_tandem(seq):
	yes = 0
	seq = seq.upper()
	for section in range (1, len(seq)):
		if len(seq) % section == 0:
			number_of_repeats = len(seq)/section
			if check_repeat(seq, section):
				yes = 1 
				print "The sequence,",seq,"has a tandem repeat, with a repeated sequence of",seq[:section]
				break 
	if yes == 0:
		print "The sequence", seq," does not include a tandem repeat."
###OUTPUT###

check_for_tandem(input_seq)

#Test Outputs
#check_for_tandem(seq1)
#check_for_tandem(seq2)
#check_for_tandem(seq3)
#check_for_tandem(seq4)
#check_for_tandem(seq5)


		
	

