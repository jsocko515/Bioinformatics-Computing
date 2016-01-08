# Exercise 13.2 (bonus)
# Walid Chatila, 10/23/15

# Write a program to count the number of specta in the file "Data1.mzXML.gz" using 
# ElementTree's iterparse function.
# 	-How many MS spectra are there?
#	-How many MS/MS spectra are there?
#	-How many MS/MS spectra have a precuror m/z value between 750 and 1000 Da?
###################################################################################
import gzip, xml.etree.ElementTree as ET

###INPUT###
file = gzip.open("Data1.mzXML.gz")
###METHOD###
ns ="{http://sashimi.sourceforge.net/schema_revision/mzXML_2.0}"
ms_level_1 = 0
ms_level_2 = 0
ms2_precursor = 0
for event,ele in ET.iterparse(file):
	if ele.tag ==  (ns + 'scan'):
		if ele.attrib['msLevel'] == '1':
			ms_level_1 += 1
		elif ele.attrib['msLevel'] == '2':
			ms_level_2 += 1
			pz_value = ele.find(ns + 'precursorMz').text
			if 750.0 <= float(pz_value) >= 1000.0:
				ms2_precursor += 1 
	
###OUTPUT###
print "There are", ms_level_1, "MS spectra."
print "There are", ms_level_2, "MS/MS spectra." 
print "There are", ms2_precursor, "MS/MS spectra tha have a precursor m/z value between 750 and 1000 Da."
