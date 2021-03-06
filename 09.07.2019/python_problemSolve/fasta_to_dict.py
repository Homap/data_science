#!/usr/bin/python
import sys

#********************************
# Written by Homa Papoli 
# Version 1. 16 July 2019
#********************************
# Exercise 2: Store the fasta file into a dictionary.
#********************************
# Run: python fasta_to_dict.py fasta_exercise_goodheader.fa
#********************************

fasta_file = open(sys.argv[1], "r")

fasta_dict = {}

for line in fasta_file:
	line = line.strip("\n")
	#print(line)
	if line.startswith(">"):
		key = line.replace(">", "")
	else:
		fasta_dict[key] = value

print(fasta_dict)

fasta_file.close()

