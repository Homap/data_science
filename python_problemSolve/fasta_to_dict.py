#!/usr/bin/python
import sys

#********************************
# Written by Homa Papoli
# Version 1. 20 June 2019
#********************************
# Exercise 2: Store the fasta file into a dictionary.
#********************************
# Run: python fasta_to_dict.py fasta_exercise_goodheader.fa
#********************************

fasta_file = open(sys.argv[1], "r")

fasta_dict = {}

for line in fasta_file:
	line = line.strip("\n")
	if line.startswith(">"):
		key = line.replace(">", "")
	else:
		value = line
		fasta_dict[key] = value

print(fasta_dict)

fasta_file.close()
# Exercise 2: Create a multi-line fasta and read
# that into a fasta dictionary
# Hint: If a key is repetitive, don't erase its
# value but append the new value to the old
# value. 

# Exercise 3: Write the script read_fasta.py as 
# function. 
# read_fasta(fasta_file)


