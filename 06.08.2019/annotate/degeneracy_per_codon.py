#!/usr/bin/python
from __future__ import division
import sys
import collections
import warnings

DNA_CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    
# Specify four nucleotides
#************************************************************
nucs = ["A", "T", "C", "G"]
#************************************************************
# Specify IUPAC codes as a dictionary
#************************************************************
IUPAC_code = {'R':['A', 'G'], 'Y':['C', 'T'], 'S':['G', 'C'], 'W':['A', 'T'], 'K':['G', 'T'], 'M':['A', 'C'], 'B':['C', 'G', 'T'], 'D':['A', 'G', 'T'], 'H':['A', 'C', 'T'], 'V':['A', 'C', 'G']}
#************************************************************
#*******************************************************************************
# Stop codons
#*******************************************************************************
stop_codons = ['TGA', 'TAA', 'TAG', 'TRA', 'TAR']
#*******************************************************************************

# Get codons from a DNA sequence
#*******************************************************************************
def get_codons(sequence, nucs=nucs, DNA_CODON_TABLE=DNA_CODON_TABLE):
	all_codons = []
	for i in range(0, len(sequence)-2, 3): # a codon every three bases
		codon = sequence[i:i+3]
		if not 'N' in codon:
			all_codons.append(codon) # append all codons in the all_codons list
	return all_codons
#*******************************************************************************
# Count synonymous-nonsynonymous sites
#*******************************************************************************
def count_sites(sequence, nucs=nucs, DNA_CODON_TABLE=DNA_CODON_TABLE):
	codons = get_codons(sequence) # get_codons returns a list of all codons
	syn_sitesl = [] # list of synonymous sites
	nonsyn_sitesl = []  # list of non-synonymous sites
	for codon in codons: # for each codon in codons list
		# Synonymous sites with SNP ********************************************
		matching = [i for i in codon if i in IUPAC_code.keys()] # check if codon contains a SNP
		if matching: # if there is a SNP in codon
			if len(matching) == 1: # if there is only one SNP in a codon
				# example: AGY would be AGC and AGT
				syn_nonsyn1 = [] # append "s" or "ns" for the first codon = AGC
				syn_nonsyn2 = [] # append "s" or "ns" for the second codon = AGT
				# **************************************************************
				SNP = list(matching)[0] # the IUPAC code for the SNP in the codon
				codon1 = codon.replace(SNP, IUPAC_code[SNP][0]) # replace the IUPAC code, e.g. Y with C
				aa1 = DNA_CODON_TABLE[codon1] # get the respective amino acid from codon table
				codon2 = codon.replace(SNP, IUPAC_code[SNP][1]) # replace the IUPAC code, e.g. Y with T
				aa2 = DNA_CODON_TABLE[codon2] # get the respective amino acid from codon table
				for index in range(0,3,1): # each codon has 3 bases, loop over them 
					for nuc in nucs: # loop over the 4 nucleotides
						if not codon1[index] == nuc: # if the base in codon is not the base in the nucs
							codon1_l = list(codon1) # set codon1 as a list
							codon1_l[index] = nuc # change nucleotide of the codon in a given position
							new_codon1 = ''.join(codon1_l) # change the codon list back into string
							if not new_codon1 in stop_codons: # if the new codon is not in the stop codons
								if DNA_CODON_TABLE[new_codon1] == aa1: # check if the changed codon would translate into the same amino acid
									syn_nonsyn1.append("s") # in that case append "s" it to syn_nonsyn1 list
								else: # if the amino acid changes
									syn_nonsyn1.append("ns") # append "ns" to syn_nonsyn1 list 
						if not codon2[index] == nuc:
							codon2_l = list(codon2)
							codon2_l[index] = nuc
							new_codon2 = ''.join(codon2_l)
							if not new_codon2 in stop_codons:
								if DNA_CODON_TABLE[new_codon2] == aa2:
									syn_nonsyn2.append("s")
								else:
									syn_nonsyn2.append("ns")
				# do calculations for synonymous and nonsynonymous sites
				syn_sites1 = 3*(syn_nonsyn1.count("s")/len(syn_nonsyn1))
				nonsyn_sites1 = 3*(syn_nonsyn1.count("ns")/len(syn_nonsyn1))
				syn_sites2 = 3*(syn_nonsyn2.count("s")/len(syn_nonsyn2))
				nonsyn_sites2 = 3*(syn_nonsyn2.count("ns")/len(syn_nonsyn2))
				SNP_syn_sites = (syn_sites1+syn_sites2)/2
				SNP_nonsyn_sites = (nonsyn_sites1+nonsyn_sites2)/2
				syn_sitesl.append(SNP_syn_sites)
				nonsyn_sitesl.append(SNP_nonsyn_sites)
		else: # if the codon does not contain a SNP
			syn_nonsyn = []
			aa = DNA_CODON_TABLE[codon] # get the amino acid of the codon
			for index in range(0,3,1): # for every base in the codon					
				for nuc in nucs: # for every base in A, T, G, C
					if not codon[index] == nuc:
						codon_l = list(codon)
						codon_l[index] = nuc
						new_codon = ''.join(codon_l)
						if not new_codon in stop_codons:
							if DNA_CODON_TABLE[new_codon] == aa:
								syn_nonsyn.append("s")
							else:
								syn_nonsyn.append("ns")
			syn_sites = 3*(syn_nonsyn.count("s")/len(syn_nonsyn))
			nonsyn_sites = 3*(syn_nonsyn.count("ns")/len(syn_nonsyn))
			syn_sitesl.append(syn_sites)
			nonsyn_sitesl.append(nonsyn_sites)
	return sequence, sum(syn_sitesl), sum(nonsyn_sitesl)
	
print ("Number(i)"+"\t"+"Codon"+"\t"+"Nonsynonymous(n)"+"\t"+"Synonymous(s)")
counter = 0	
for codons in DNA_CODON_TABLE.keys():
	if not codons in stop_codons:
		counter += 1
		l = list(count_sites(codons, nucs=nucs, DNA_CODON_TABLE=DNA_CODON_TABLE))
		print (str(counter)+"\t"+str(l[0])+"\t"+str(round(l[2],3))+"\t"+str(round(l[1],3)))
	
