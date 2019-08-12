from __future__ import division
import sys
import collections
import warnings

#************************************************************
# Codon table as dictionary
#************************************************************
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
#************************************************************    
# Four nucleotides as list
#************************************************************
nucs = ["A", "T", "C", "G"]
#************************************************************
# IUPAC codes as a dictionary
#************************************************************
IUPAC_code = {'R':['A', 'G'], 'Y':['C', 'T'], 'S':['G', 'C'], 'W':['A', 'T'], 'K':['G', 'T'], 'M':['A', 'C'], 'B':['C', 'G', 'T'], 'D':['A', 'G', 'T'], 'H':['A', 'C', 'T'], 'V':['A', 'C', 'G']}
#************************************************************
# Stop codons as list
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
def count_sites(nucs=nucs, DNA_CODON_TABLE=DNA_CODON_TABLE):
	degeneracy_table = {}
	degeneracy_table_bases = {}
	syn_sitesl = [] # list of synonymous sites
	nonsyn_sitesl = []  # list of non-synonymous sites
	for codon in DNA_CODON_TABLE.keys(): # for each codon in codons list
		if not codon in stop_codons: # do not consider stop codons
			#syn_nonsyn = []
			aa = DNA_CODON_TABLE[codon] # get the amino acid of the codon
			for index in range(0,3,1): # for every base in the codon	
				syn_nonsyn = []
				base_syn = ["0"]
				base_nonsyn = ["0"]
				base_nonsense = ["0"]
				for nuc in nucs: # for every base in A, T, G, C
					if not codon[index] == nuc:
						codon_l = list(codon)
						codon_l[index] = nuc
						new_codon = ''.join(codon_l)
						if not new_codon in stop_codons:
							if DNA_CODON_TABLE[new_codon] == aa:
								syn_nonsyn.append("s")
								base_syn.append(nuc)
							else:
								syn_nonsyn.append("ns")
								base_nonsyn.append(nuc)
						else:
							syn_nonsyn.append("nonsense")
							base_nonsense.append(nuc)

				denominator = syn_nonsyn.count("s") + syn_nonsyn.count("ns") + syn_nonsyn.count("nonsense")
				syn_sites = round((syn_nonsyn.count("s")/denominator), 3)
				nonsyn_sites = round((syn_nonsyn.count("ns")/denominator), 3)
				nonsense_sites = round((syn_nonsyn.count("nonsense")/denominator), 3)
				
				if codon in degeneracy_table.keys():
					degeneracy_table[codon].append((syn_sites, nonsyn_sites, nonsense_sites))
				else:
					degeneracy_table[codon] = [(syn_sites, nonsyn_sites, nonsense_sites)]
				
				if codon in degeneracy_table_bases.keys():
					degeneracy_table_bases[codon].append((":".join(base_syn), ":".join(base_nonsyn), ":".join(base_nonsense)))
				else:
					degeneracy_table_bases[codon] = [(":".join(base_syn), ":".join(base_nonsyn), ":".join(base_nonsense))]
	return degeneracy_table, degeneracy_table_bases
