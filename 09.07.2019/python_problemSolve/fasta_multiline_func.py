#!/usr/bin/python
import sys
import time
import gzip
start = time.time()

#*******************************************************************************
# Writen by Homa Papoli
#*******************************************************************************
# This script takes a fasta sequence and reads it into a dictionary.
# Each line is added to a list and the sequences in a list are then joined. 
# With each new header, the list is then updated. 
# Usage: ./fasta_multiline_func.py asta_exercise_multi.fa 
#*******************************************************************************

#filename = open(sys.argv[1], 'r')
#filename = gzip.open(sys.argv[1], "rt")

def readfasta(filename):
	fasta_dict = {}
	l = list()
	header = None
	for line in filename:
		line = line[:-1]
		if line.startswith('>'): # a new record
	        # save the previous record to the dict
			if header:
				fasta_dict[header] = ''.join(l) 
				l=[]    # empty the list
			header = line[1:]
		else:
			l.append(line)

	# save the last record
	fasta_dict[header] = ''.join(l) 

	return fasta_dict

import fasta_multiline_func
readfasta(filename.fa)

end = time.time()
print(end - start)