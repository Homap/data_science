#!/usr/bin/python
import sys
from fasta import readfasta
from codon_degeneracy import *
from revcomp_fun import revcomp
from get_codons_fun import *
from gff_to_dict_fun import gff_to_dict

#*******************************************************************
# Written by Homa Papoli Yazdi - 12 August 2019
#*******************************************************************
# annotate_vcf.py used the CDS coordinates in the gff file to 
# annotate each coding position along in the genome into 
# synonymous, missense and nonsense according to the following rule:
#*******************************************************************
# Inputs: sequence.fa annotation.gff
#*******************************************************************
# Run: annotate_vcf.py sequence.fa annotation.gff > output.txt
#*******************************************************************


#*******************************************************************
# Open inputs
#*******************************************************************
fastafile = open(sys.argv[1], "r")
gff_file = open(sys.argv[2], "r")
#*******************************************************************
# Read fasta file into dictionary 
#*******************************************************************
g_fasta = readfasta(fastafile)
#*******************************************************************
# Read gff file into dictionary 
#*******************************************************************
gff_dict = gff_to_dict(gff_file)
#*******************************************************************
# Create the degeneracy count table
#*******************************************************************
degeneracy_table_counts = count_sites()[0]
#*******************************************************************
# Create the degeneracy base table
#*******************************************************************
degeneracy_table_bases = count_sites()[1]
#*******************************************************************

#*******************************************************************
# File header
header = ['chr', 'mRNA_id', 'codon', 'case', 'position_0based', \
		'synonymous', 'missense', 'nonsense']
print("\t".join(header))
#*******************************************************************
# Errors in phase (reading frame) might occur in gff, therefore 
# we record those transcripts where a stop codon is encountered 
# in a separate list
stop_transcripts = []
#*******************************************************************
for key in gff_dict.keys():
	seqid = key[0]
	strand = key[1]
	geneid = key[2]
	if strand == "+":
		for index, item in enumerate(gff_dict[key]):
			start_cds = item[0]
			end_cds = item[1]
			phase_cds = item[2]
			if phase_cds == 0:
				for i in get_codons(g_fasta, seqid, start_cds, end_cds, phase_cds):
					if i[0] in stop_codons:
						stop_transcripts.append(key)
					else:
						for index, item in enumerate(i[0]):
							print(seqid, geneid, i[0], item, i[1] + index, \
								"\t".join(str(i) for i in degeneracy_table_counts[i[0]][index]))
			elif phase_cds == 1:
				first_part_codon = gff_dict[key][index - 1][1] - 2
				second_part_codon = gff_dict[key][index][0]
				first_part = g_fasta[seqid][first_part_codon:first_part_codon + 2]
				second_part = g_fasta[seqid][second_part_codon]
				first_codon = first_part + second_part
				if not first_codon in stop_codons:
					print(seqid, geneid, first_codon, first_codon[0], first_part_codon, \
						"\t".join(str(i) for i in degeneracy_table_counts[first_codon][0]))
					print(seqid, geneid, first_codon, first_codon[1], first_part_codon + 1, \
						"\t".join(str(i) for i in degeneracy_table_counts[first_codon][1]))
					print(seqid, geneid, first_codon, first_codon[2], second_part_codon, \
						"\t".join(str(i) for i in degeneracy_table_counts[first_codon][2]))
				else:
					stop_transcripts.append(key)
				for i in get_codons(g_fasta, seqid, start_cds, end_cds, phase_cds):
					if not i[0] in stop_codons:
						for index, item in enumerate(i[0]):
							print(seqid, geneid, i[0], item, i[1] + index, \
								"\t".join(str(i) for i in degeneracy_table_counts[i[0]][index]))
				else:
					stop_transcripts.append(key)
			elif phase_cds == 2:
				first_part_codon = gff_dict[key][index - 1][1] - 1
				second_part_codon = gff_dict[key][index][0]
				first_part = g_fasta[seqid][first_part_codon]
				second_part = g_fasta[seqid][start_cds:second_part_codon + 2]
				first_codon = first_part + second_part
				if not first_codon in stop_codons:
					print(seqid, geneid, first_codon, first_codon[0], first_part_codon, \
						"\t".join(str(i) for i in degeneracy_table_counts[first_codon][0]))
					print(seqid, geneid, first_codon, first_codon[1], start_cds, \
						"\t".join(str(i) for i in degeneracy_table_counts[first_codon][1]))
					print(seqid, geneid, first_codon, first_codon[2], start_cds + 1, \
						"\t".join(str(i) for i in degeneracy_table_counts[first_codon][2]))
				else:
					stop_transcripts.append(key)
				for i in get_codons(g_fasta, seqid, start_cds, end_cds, phase_cds):
					if not i[0] in stop_codons:
						for index, item in enumerate(i[0]):
							print(seqid, geneid, i[0], item, i[1] + index, \
								"\t".join(str(i) for i in degeneracy_table_counts[i[0]][index]))	
				else:
					stop_transcripts.append(key)			
	elif strand == "-":
		codon_list = []
		for index, item in enumerate(gff_dict[key]):
			start_cds = item[0]
			end_cds = item[1]
			phase_cds = item[2]
			if phase_cds == 0:
				for i in get_codons_reverse(g_fasta, seqid, start_cds, end_cds, phase_cds):
					if not i[0] in stop_codons:
						codon_list.append(i)
				else:
					stop_transcripts.append(key)
			elif phase_cds == 1:
				first_part_codon = gff_dict[key][index][1] - 1
				second_part_codon = gff_dict[key][index - 1][0]
				first_part = g_fasta[seqid][first_part_codon]
				second_part = g_fasta[seqid][second_part_codon:second_part_codon + 2]
				first_codon = revcomp(first_part + second_part)
				if not first_codon in stop_codons:
					codon_list.append((first_codon, second_part_codon + 1, second_part_codon, first_part_codon))
				else:
					stop_transcripts.append(key)
				for i in get_codons_reverse(g_fasta, seqid, start_cds, end_cds, phase_cds):
					if not i[0] in stop_codons:
						codon_list.append(i)	
					else:
						stop_transcripts.append(key)			
			elif phase_cds == 2:
				first_part_codon = gff_dict[key][index][1] - 2
				second_part_codon = gff_dict[key][index - 1][0]
				first_part = g_fasta[seqid][first_part_codon:first_part_codon + 2]
				second_part = g_fasta[seqid][second_part_codon]
				first_codon = revcomp(first_part + second_part)
				if not first_codon in stop_codons:
					codon_list.append((first_codon, second_part_codon, first_part_codon + 1, first_part_codon))
				else:
					stop_transcripts.append(key)
				for i in get_codons_reverse(g_fasta, seqid, start_cds, end_cds, phase_cds):
					if not i[0] in stop_codons:
						codon_list.append(i)
					else:
						stop_transcripts.append(key)

		for index, item in enumerate(codon_list):
			# print(index, item)
			print(seqid, geneid, item[0], item[0][0], item[1], \
				"\t".join(str(i) for i in degeneracy_table_counts[item[0]][0]))	
			print(seqid, geneid, item[0], item[0][1], item[2], \
				"\t".join(str(i) for i in degeneracy_table_counts[item[0]][1]))
			print(seqid, geneid, item[0], item[0][2], item[3], \
				"\t".join(str(i) for i in degeneracy_table_counts[item[0]][2]))
#*******************************************************************
# Close inputs
fastafile.close()
gff_file.close()
#*******************************************************************
