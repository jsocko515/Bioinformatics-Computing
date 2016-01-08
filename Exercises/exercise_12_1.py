# Exercise 12.1
# Walid Chatila,  10/23/15

# Write a program that analyzes a PDB file (filename provided on the command-line!)
# to find pairs of lysine residues that might be linked if the BS3 cross-linker is used.
# 	-The rigid BS3 cross-linker is approximately 11 A long.
# 	- Write two versions, one that computes the distance between all pairs of 
#	  lysine residues, and one that uses the NeighborSearch technique.


##################################################################################################
import Bio.PDB.PDBParser, sys, os


###INPUT###
if len(sys.argv) < 2:
    print >>sys.stderr, "Please provide a PDB file."
    sys.exit(1)

pdb_file = sys.argv[1]

if not os.path.exists(pdb_file):
	print >>sys.stderr, pdb_file, "cannot be located, please make sure this file exists."
	sys.exit(1)



###METHOD###
pro_name = pdb_file.split(".")[0]
parser = Bio.PDB.PDBParser(QUIET=True)
structure = parser.get_structure(pro_name, pdb_file)
model = structure[0]
achain = model['A']


# slow version, have to check the atom in resiude with the has_id('NZ')
# need to check if one index larger than the other to eliminate same values and 0 values
# check if the distance between 10 and 12 (11 rigid)
def bs3_slow(a):
	list_res1_index = []
	list_res2_index = []
	res1_value = []
	res2_value = []

	lysresidues = [ residue for residue in a if residue.get_resname() == 'LYS']
	for res1 in lysresidues:
		res1index = res1.get_id()[1]
		for res2 in lysresidues:
			res2index = res2.get_id()[1]
			if( 
				res1.has_id('NZ')       and  
			    res2.has_id('NZ')       and 
			  ( res1index < res2index)  and 
			  ( 10.0 <= (res1['NZ'] - res2['NZ']) <= 12.0)
			   ):
					list_res1_index.append(res1index)
					list_res2_index.append(res2index)
					res1_value.append(res1['NZ'])
					res2_value.append(res2['NZ'])
	
	return dict(list_res1_index = list_res1_index, list_res2_index = list_res2_index, res1_value = res1_value, res2_value = res2_value)
# Funtion using neighbors search the neigbors search checks the for lys residues with the NZ atom
# That are less than 12, however an if statement is used to check if its larger than 11
def bs3_neighbor(a):
	list_res1_index = []
	list_res2_index = []
	res1_value = []
	res2_value = []


	lysresidues = [ residue for residue in a if residue.get_resname() == 'LYS']
	NZ_lys_atoms = [atom['NZ'] for atom in lysresidues if atom.has_id('NZ')]
	neighbors = Bio.PDB.NeighborSearch(NZ_lys_atoms)

	for res1_pos in (NZ_lys_atoms):
		for res2_pos in neighbors.search(res1_pos.get_coord(), 12.0):
			res1 = res1_pos.get_parent()
			res2 = res2_pos.get_parent()
			res1index = res1.get_id()[1]
			res2index = res2.get_id()[1]
			if res1index < res2index and ((res1_pos - res2_pos) > 10.0):
				list_res1_index.append(res1index)
				list_res2_index.append(res2index)
				res1_value.append(res1_pos)
				res2_value.append(res2_pos)
		
	
	return dict(list_res1_index = list_res1_index, list_res2_index = list_res2_index, res1_value = res1_value, res2_value = res2_value)



###OUTPUT###

slow_bs3 = bs3_slow(achain)
neighbor_bs3 = bs3_neighbor(achain)

print "Possible BS3 linker(slow method):"
print "----------------------------------------------------------------------------------------"
for index, y in enumerate(slow_bs3['list_res1_index']):
		print index+1,". Possible bs3 linker: Lys residue", y, "- Lys residue", 
		print slow_bs3['list_res2_index'][index],
		print "--- Distance of", round(slow_bs3['res1_value'][index] - slow_bs3['res2_value'][index], 2)
print
print "Possible BS3 linker(neighbors method):"
print "----------------------------------------------------------------------------------------"
for index, y in enumerate(neighbor_bs3['list_res1_index']):
		print index+1,". Possible bs3 linker: Lys residue", y, "- Lys residue", 
		print neighbor_bs3['list_res2_index'][index],
		print "--- Distance of", round(neighbor_bs3['res1_value'][index] - neighbor_bs3['res2_value'][index], 2)

