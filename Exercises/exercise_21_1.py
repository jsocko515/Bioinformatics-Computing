# Exercise 21.1
# Walid Chatila    11/23/15

# Write a python program to lookup the scientific name for a user-supplied organism name.
#####################################################################################################
import sqlite3, sys 

###INPUT###
if len(sys.argv) < 2:
	print "Please provide the name of an organism."
	sys.exit(1)

org_name = (sys.argv[1])

###Method###

conn = sqlite3.connect('taxa.db3')
params = [org_name]
c = conn.cursor()
c.execute("""
	select scientific_name from taxonomy, name 
	where name.name = ?
	and 
	taxonomy.tax_id = name.tax_id; 
	""", params)


###Output###
for row in c:
	print "Organism Name:", org_name,  " --- Scientific Name:", row[0]