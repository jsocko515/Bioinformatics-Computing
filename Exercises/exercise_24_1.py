from MyDNAStuff import * 
from pylab import *
seq = read_seq_from_file("anthrax_sasp.nuc.txt")
#print seq

gc = percent_GC(seq)
#print gc

gc_values = []
for i in range(0, len(seq),20):
	#print percent_GC(seq[i:i+20]),  seq[i:i+20]
	gc_values.append(percent_GC(seq[i:i+20]))
boxplot(gc_values)
title("GC Percent")
ylabel("Percent")
show()