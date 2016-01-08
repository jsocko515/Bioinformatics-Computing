# Exercise 11.1 
# Walid Chatila, 10/19/15

# Download human proteins from RefSeq and compute amino-acid frequencies for the (RefSeq) human proteome.
# 	-Which amino-acid occurs the most? The least?
# Download human proteins from SwissProt and compute amino-acid frequencies for the SwissProt human proteome.
# 	-Which amino-acid occurs the most? The least?
# How similar are the human amino-acid frequencies of in RefSeq and SwissProt?

##############################################################################################################
import Bio.SeqIO, sys, gzip

###INPUT###
if len(sys.argv) < 3:
	print >>sys.stderr, "Please provide a Refseq Fasta File and a SwissProt File. "
	sys.exit(1)

refseq_file = sys.argv[1]
swiss_file = sys.argv[2]


###METHOD###

#Opens the File
def open_file(file):
	seqfile = gzip.open(file)
	return seqfile

#Finds the county of amino acid then gets their percentage.
def aa_freq(file, type):
	count = {}
	for seq_record in Bio.SeqIO.parse(file, type):
		for aa in seq_record.seq:
			count[aa] = count.get(aa, 0) + 1
		
	total_aa = sum(count.values())
	for amino_acid, cnt in count.items():
		count[amino_acid] = (float(cnt)/float(total_aa)) * 100
	return count

# Takes in the coutns forthe two files. Returns a list for each file with the frequencies. 
# Also returns a list of the difference between Refseq frequencies and Swiss Prot frequencies.
# Determines the max and min for each of the lists. 
def compare(refseq, swiss):
	amino_acids = set()
	amino_acids.update(refseq.keys()) 
	amino_acids.update(swiss.keys())

	refseq_list  = [("Refseq", "Freq")] 
	swiss_list   = [("Swiss", "Freq")]
	compare_list = [("Compare", "Freq")]

	for amino_acid in amino_acids:
		refseq_freq = refseq.get(amino_acid, 0)
		swiss_freq  = swiss.get(amino_acid, 0)
		compare_list.append(((refseq_freq-swiss_freq), amino_acid))
		refseq_list.append((refseq_freq, amino_acid))
		swiss_list.append((swiss_freq, amino_acid))
	
	max_refseq  = max(refseq_list[1:])
	max_swiss   = max(swiss_list[1:])
	max_compare = max(compare_list[1:])

	min_refseq  = min([x for x in refseq_list[1:] if x[0] != 0.0])
	min_swiss   = min([x for x in swiss_list[1:] if x[0] !=0.0])
	min_compare = min(compare_list[1:])
	
	return dict(refseq_list = refseq_list, swiss_list = swiss_list, compare_list = compare_list, max_refseq = max_refseq, max_compare = max_compare, max_swiss = max_swiss, min_compare = min_compare, min_swiss = min_swiss, min_refseq = min_refseq)

# A print function that will print out in an organized manner. 
def print_output(dic_list, list, min, max):
	print dic_list[list][0][0], ":", dic_list[list][0][1]
	print "----------------"
	for i in sorted(dic_list[list][1:], key=lambda x: x[0]):
		print i[1], ":", round(i[0], 4)

	if list != "compare_list":
		print "The ", dic_list[min][1], "amino acid had the minimum frequency"
		print "The ", dic_list[max][1], "amino acid had the maximum frequency"  
	else:
		print "The ", dic_list[min][1], "amino acid was seen more in the Swissprot file."
		print "The ", dic_list[max][1], "amino acid was seen more in the Refseq file"  


###OUTPUT###

open_refseq = open_file(refseq_file)
open_swiss  = open_file(swiss_file)

refseq_freq = aa_freq(open_refseq, "fasta")
swiss_freq  = aa_freq(open_swiss, "swiss")

dict_of_lists = compare(refseq_freq, swiss_freq)


print_output(dict_of_lists, "refseq_list", "min_refseq", "max_refseq")
print 	
print_output(dict_of_lists, "swiss_list", "min_swiss", "max_swiss")
print
print_output(dict_of_lists, "compare_list", "min_compare", "max_compare")

open_refseq.close()
open_swiss.close()

