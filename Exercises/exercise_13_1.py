# Exercise 13.1
# Walid Chatila, 10/23/15

# Write a program to pick out, and print, the references of a XML format 
# UniProt entry, in a nicely formatted way.
#####################################################################################
import sys, xml.etree.ElementTree as ET, urllib, requests

###INPUT###

if len(sys.argv) < 2:
    print >>sys.stderr, "Please provide a accession number for the uniprot gene/protein."
    sys.exit(1)

input_accesion = sys.argv[1] 
thefile = urllib.urlopen('http://uniprot.org/uniprot/'+input_accesion+'.xml')



###METHOD###
document = ET.parse(thefile)
root = document.getroot()
ns = '{http://uniprot.org/uniprot}'

#Will only print out journal article references, not submissions
def reference_creator(root, ns):
	all_refs = {}
	for entry in root.findall(ns+'entry'):
		for reference in entry.findall(ns+'reference'):
			citation = reference.find(ns +'citation')
			if citation.attrib['type'] != 'journal article':
				continue
			authors_list = citation.find(ns+"authorList")
			authors = []
			for person in authors_list.findall(ns+'person'):
				authors.append(person.attrib['name'])
			for consortium in authors_list.findall(ns+'consortium'):
				authors.append(person.attrib['name'])
			

			key = int(reference.attrib['key'])
			ref_dic = {}
			ref_dic['authors'] = authors
			ref_dic['publish_date'] = citation.attrib['date']
			ref_dic['title'] = citation.find(ns+'title').text
			ref_dic['journal_name'] = citation.attrib['name']
			ref_dic['first_page'] = citation.attrib['first']
			ref_dic['last_page'] = citation.attrib['last']
			all_refs[key] = ref_dic
	return all_refs



###OUTPUT###
references = reference_creator(root,ns)
print "References for Journal Articles:"
for key, value in sorted(references.iteritems()):
	print
	print key,"."
	print ', '.join(value['authors']),". ",
	print "(", value['publish_date'],").",
	print value['title'],
	print value['journal_name'],", ",
	print value['first_page'], "-", value['last_page'],"."
