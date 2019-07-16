#!/usr/bin/python
import sys

#********************************
# Written by Homa Papoli
# Version 1. 16 July 2019
#********************************
# Excercise 1: Take every odd line (1, 3, 5, ...) 
# and print the line by adding ">" to the line. 
# Then write the output to the new fasta file.
#********************************
# Run: python exercise_1B.py fasta_nopatter_header.fa
# think also about solving it with regex:
# Exercise: Solving the same problem with regex.
#********************************
# Open fasta file
fasta_file = open(sys.argv[1], "r")

seq_letters = 'ATCGRYMKSWHBVDN'

# Iterate through each fasta line
for line in fasta_file:
	line = line.strip("\n")
	set1 = set(line.upper()).difference(set(seq_letters))
	if set1: # if evaluates everything as boolean. empty sets
	# and None is set to False. 
		print(">"+line)
	else:
		print(line)

fasta_file.close()