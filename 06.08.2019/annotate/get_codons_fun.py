import numpy as np
from revcomp_fun import revcomp

def get_codons(g_fasta, seqid, start, end, phase):
    codon_coordinates = [i for i in np.arange(start + phase, end, 3)]
    for codon_coord in codon_coordinates:
        if codon_coord + 3 <= end:
            codon = g_fasta[seqid][codon_coord:codon_coord+3]
            if not 'N' in codon:
            	yield codon, codon_coord, codon_coord+1, codon_coord+2

def get_codons_reverse(g_fasta, seqid, start, end, phase):
    codon_coordinates = [i for i in np.arange(end - phase, start, -3)]
    for codon_coord in codon_coordinates:
        if codon_coord - 3 >= start:
            codon = g_fasta[seqid][codon_coord-3:codon_coord]
            if not 'N' in codon:
            	yield revcomp(codon), codon_coord - 1 , codon_coord - 2, codon_coord - 3