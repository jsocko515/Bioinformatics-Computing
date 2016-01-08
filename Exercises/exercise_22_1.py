# Exercise 22.1
# Walid Chatila, 11/30/15

# Write a python program using SQLObject to lookup the scientific name 
# for a user-supplied organism name. 
#######################################################################
from model_22 import *
import sys 
 
 ###Input###
try:
	organism_name = str(sys.argv[1])
except IndexError:
	print >>sys.stderr, "Please provide the name of an organism."
	sys.exit(1)



###Method###
try: 
	name = Name.selectBy(name=organism_name)[0]
except IndexError:
	print "Cannot find the supplied name. Please provide a valid organism name."
	sys.exit(1)

scientific_name = name.taxa.scientificName


###Output###
print "The common name:", organism_name
print "The scientific name:", scientific_name