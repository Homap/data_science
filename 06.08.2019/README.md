# Annotate genomic sites for being synonymous, missense and nonsense

It is often useful to know the impact of a mutation on an amino acid. This will help us to divide genomic sites into those that could be susceptible to selection and those that could be potentially neutral. Mutations in codons can be divided into synonymous and nonsynonymous. Synonymous changes do not change the amino acid. Nonsynonymous changes are further divided into missense (one amino acid into the other) and nonsense (an amino acid into stop codon). 

If any change in a given site changes the amino acid, the site is said to be 0-fold. If any change in a given site does not change the amino acid, the site is said to be 4-fold. Sometimes, two changes in a site would change the amino acid and one change, would keep the same amino acid. In that case, one need to average over the possible changes for the site and eventually for the codon. 

Let's use the counting method as presented in section 2.5.1.1, page 48 of Molecular Evolution: A Statistical Approach by Ziheng Yang.

We want to calculate the number of synonymous and nonsynymous sites for the codon CAC:

|CAC| H | effect |
|---|---|---|
| TAC | Y | nonsynonymous |
| GAC | D | nonsynonymous |
| AAC | N | nonsynonymous |
| CTC | L | nonsynonymous |
| CGC | R | nonsynonymous |
| CCC | P | nonsynonymous |
| CAG | Q | nonsynonymous |
| CAT | H | synonymous |
| CAA | Q | nonsynonymous |

For codon:

Number of synonymous sites : 3 * (1/9) = 0.333

Number of nonsynonymou sites : 3 * (8/9) = 2.667

For each site: 

site 1 (C): 0-fold

site 2 (A): 0-fold

site 3 (C): (1/3) synonymous and (2/3) nonsynonymous

## Scripts in the annotate folder
Using the scripts in the *annotate* folder, you can generate a codon degeneracy table, moreover, using a gff file and your genome fasta sequence, you can annotate each site in the coding sequence into synonymous, missense and nonsense. Such a file can then be easily used to overlap with your VCF file, so not only you will know about the annotation of your SNPs but also you will have the background annotation which is necessary to calculate statistics such as pN/pS.

To create the codon table, simply run:

`python degeneracy_per_codon.py`

To annotate your genome of interest, run (using the example data):

`python annotate_sites.py data/genome.fa data/genome.gff`





