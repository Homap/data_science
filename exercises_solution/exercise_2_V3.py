#!/usr/bin/python
import sys 
import gzip
from Bio import SeqIO
import time

start = time.time()

#*******************************************************************************
# Writen by Mortiz Buck
#*******************************************************************************

output = {}

with gzip.open(sys.argv[1], "rt") as file:
	for sequence in SeqIO.parse(file, "fasta"):
		output[sequence.id] = str(sequence.seq)

print(output)

end = time.time()
print(end - start)
