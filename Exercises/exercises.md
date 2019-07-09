# July 9th 2019
## Exercises

### Exercise 1:
Given the fasta file in python_problemSolve/fasta_exercise.fa, 
write a script to:

* Take every odd line (1, 3, 5, ...) and print the line by adding
">" to the line. Then write the output to the new fasta file.
* We corrected the header in fasta_exercise.fa by searching for 
lines containing "seq" in them. Write a script for a situation 
where no particular pattern appears in the fasta header. That is
the file could be:
`ragnarok`
`ACTGTGTGTGTACAGTGCA`
`thor`
`ACTGTGTGTGTACGT`
`odin`
`ACAACACGTGTGTTTTTTT`

### Exercise 2:
Write a script to read a multi-line fasta file (such as the one below)
into a Python dictionary. A multi-line fasta
looks as below:
`>seq1`
`ACTGTGTGTGTACAGTGCA`
`ACTGTGTGTGTA`
`>seq2`
`ACTGTGTGTGTACGT`
`ACTGTGTGTGTACGT`
`ACTGTGTGT`
`>seq3`
`ACAACACGTGTGTT`
`ACAACACGTGTGTT`
`ACAACA`

### Exercise 3:
Write the script multiline_fasta_to_dict.py as a function. 
So that you can import it to your future scripts and use it as below:
`fasta_to_dict(you_fasta_file)`

### Exercise 4:
Using Pandas and the human genome annotation file 
`Homo_sapiens.GRCh38.85.gff3.gz`, answer the following questions:
*How many transcripts does a gene typically have? What percentage of genes have more than 1 transcript?
*How many exons, CDS, and UTRs does a transcript typically have? What sizes are they?
