#!/usr/bin/python
import sys

#*******************************************************************************
# Writen by Homa Papoli
#*******************************************************************************
# This script takes a fasta sequence and reads it into a dictionary.
# Each line is added to a list and the sequences in a list are then joined. 
# With each new header, the list is then updated. 
# Usage: ./fasta.py fasta.fa 
#*******************************************************************************

#filename = open(sys.argv[1], 'r')

def readfasta(filename):
	fasta_dict = {}
	l = list()
	header = None
	for line in filename:
		if line.startswith('>'): # a new record
            # save the previous record to the dict
			if header:
				fasta_dict[header] = ''.join(l) 
				del l[:]    # empty the list
			# If there is a space in the sequence name, the name is still imported
			# as a whole with the space as here, we split the sequence on ">" and 
			# we take the first element of the list which consists of the whole name.
			header = line.strip().split('>')[1]
		else:
			l.append(line.strip())

    # save the last record
	fasta_dict[header] = ''.join(l) 

	return fasta_dict
