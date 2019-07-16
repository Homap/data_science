#!/usr/bin/python
import sys

#********************************
# Written by Homa Papoli and Moritz Buck
# Version 1. 16 July 2019
#********************************
# Excercise 1: Take every odd line (1, 3, 5, ...) 
# and print the line by adding ">" to the line. 
# Then write the output to the new fasta file.
#********************************
# Run: python exercise_1A.py fasta_exercise.fa > fasta_exercise_1A.fa
#********************************
# Open fasta file
fasta_file = open(sys.argv[1], "r")

# Solution 1
#counter = 0
#for line in fasta_file:
#	counter = counter + 1  
#	line = line.strip("\n")
	# if counter%2 != 0:
	# 	print(">"+line)
	# else:
	# 	print(line)

# Solution 2
for counter, line in enumerate(fasta_file):
	line = line.strip("\n")
	if counter%2 == 0:
		print(">"+line)
	else:
		print(line)



fasta_file.close()