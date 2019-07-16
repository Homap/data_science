#!/usr/bin/python
import sys
import time
import gzip
start = time.time()

#********************************
# Written by Homa Papoli - Madeline Chase
# Version 1. 16 July 2019
#********************************
# Exercise 2: Store the fasta file into a dictionary.
#********************************
# Run: python exercise_2_V1.py fasta_exercise_multi.fa.gz
#********************************

fasta_file = gzip.open(sys.argv[1], "rb")

fasta_dict = {}

for line in fasta_file:
	line = line.decode()
	line = line.strip("\n")
	if line.startswith(">"):
		key = line.replace(">", "")
		value = ""
	else:
		value += line
		fasta_dict[key] = value

print(fasta_dict)

fasta_file.close()

end = time.time()
print(end - start)
