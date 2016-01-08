# Exercise 23.1
# Walid Chatila  11/30/15
# Write a python program using SQLObject to find the taxonomic lineage of a user-supplied organism name.
# 	- Make sure to used the small_taxa.db3 file. 
########################################################################################################
from model_23 import * 

init()
 
 ###Input###
try:
	organism_name = str(sys.argv[1])
except IndexError:
	print >>sys.stderr, "Please provide the name of an organism."
	sys.exit(1)

###Method/OUTPUT###
try: 
	name = Name.selectBy(name=organism_name)[0]
except IndexError:
	print "Cannot find the supplied name. Please provide a valid organism name."
	sys.exit(1)
t = name.taxonomy


print "Organism", t.scientific_name, "has name(s):"
for n in t.names:
	print "	-",n.name
for c in t.children:
	print "Organism",t.scientific_name,"has child:" 
	print "	-",c.scientific_name
print "Organism", t.scientific_name, "has parent:"
print "	-", t.parent.scientific_name


r = t
lineage = [r.scientific_name]
while r != r.parent:
	r = r.parent
	lineage.append(r.scientific_name)

print 
print "Lineage:"
for parent in lineage:
	print parent, ":",


