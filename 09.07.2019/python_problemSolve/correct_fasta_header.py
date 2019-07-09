#!/usr/bin/python
import sys

#********************************
# Written by Homa Papoli
# Version 1. 20 June 2019
#********************************
# Excercise 1: Add ">" to the sequence names 
# in the fasta file.
#********************************
# Run: python correct_fasta_header.py fasta_exercise.fa > fasta_exercise_goodheader.fa
#********************************
# Open fasta file
fasta_file = open(sys.argv[1], "r")

# Iterate through each fasta line
for line in fasta_file:
	line = line.strip("\n")
	if "seq" in line:
		print(">"+line)
	else:
		print(line)

fasta_file.close()


