#!/usr/bin/python
import sys
import time
import gzip
start = time.time()

#********************************
# Written by Homa Papoli
# Version 1. 20 June 2019
#********************************
# Exercise 2: Store the fasta file into a dictionary.
#********************************
# Run: python fasta_to_dict.py fasta_exercise_goodheader.fa
#********************************

fasta_file = gzip.open(sys.argv[1], "rb")

fasta_dict = {}

for line in fasta_file:
	line = line.decode()
	line = line.strip("\n")
	#print(line)
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
