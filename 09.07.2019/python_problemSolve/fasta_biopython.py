#!/usr/bin/python
import sys 
import gzip
from Bio import SeqIO
import time

start = time.time()
output = {}

with gzip.open(sys.argv[1], "rt") as file:
	for sequence in SeqIO.parse(file, "fasta"):
		output[sequence.id] = str(sequence.seq)

end = time.time()
print(end - start)
