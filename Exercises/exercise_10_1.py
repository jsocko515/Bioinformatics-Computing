#Exercise 10.1
#Walid Chatila, 10/12/15

# Write a porgram that reads the microarray data in "data.csv" and computes the mean and standar deviation
# of the expression values of a specific gene overall, and within each sample category. 
	# - Get the name of the microarray datafile from the command-line.
	# - Get the name ofthe gene from the command-line. 
########################################################################################################################

import sys, csv, math

###INPUT###

if len(sys.argv) < 3:
    print "Please provide a csv file and the header for the gene."
    sys.exit(1)

input_file = sys.argv[1]
input_gene = sys.argv[2]


###METHOD###

#Will read through the file, and assign the Tumour column and specified gene column to lists.
def readfile_getcoloumns(file, gene):
	csv_file = open(file)
	reader = csv.DictReader(csv_file)
	gene_list = []
	tumour_list = []
	for rows in reader:
		tumour_list.append(rows['TUMOUR'])
		gene_list.append(rows[gene]) 
	gene_list = map(float, gene_list)
	tumour_list = map(int, tumour_list)
	csv_file.close()
	return dict(gene_list = gene_list, tumour_list = tumour_list)

#Split up the gene rows based on tumour category
def tumour_category(gene_list, tumour_list):
	cat1 = []
	cat2 = []
	for i in range(len(tumour_list)):
		if tumour_list[i] == 1:
			cat1.append(gene_list[i])
		else:	
			cat2.append(gene_list[i])
	return dict(cat1_list = cat1, cat2_list = cat2)

#Get the mean and the standard deviation of a list of numbers
def mean_stdv(list):
	mean = lambda x:  sum(x)/len(x)
	stdv = lambda x:  math.sqrt(((len(x)*(sum([i**2 for i in x]))) - (sum(x)**2))  /  float((len(x)*(len(x)-1))))
	return dict(mean = mean(list), stdv = stdv(list))

###OUTPUT###

desired_columns  = readfile_getcoloumns(input_file, input_gene)
category_lists   = tumour_category(desired_columns["gene_list"], desired_columns["tumour_list"])
gene_stats 		 = mean_stdv(desired_columns["gene_list"])
category_1_stats = mean_stdv(category_lists["cat1_list"])
category_2_stats = mean_stdv(category_lists["cat2_list"])

print "The mean and standard deviation of expression values for the gene,", input_gene, ", are", gene_stats['mean'], "and", gene_stats['stdv'], "respectively."
print "The mean and standard deviation of expression values for the gene," , input_gene,", in the first Tumour category are", category_1_stats['mean'], "and",  category_1_stats['stdv'], "respectively."
print "The mean and standard deviation of expression values for the gene," , input_gene,", in the second Tumour category are", category_2_stats['mean'], "and",  category_2_stats['stdv'], "respectively."


