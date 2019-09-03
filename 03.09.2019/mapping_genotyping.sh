#!/bin/bash -l
#SBATCH -A snic2017-X-YYY
#SBATCH -p core
#SBATCH -n 1
#SBATCH -t 01:00:00

ref="data/scaffolds.fa"

# create directories
mkdir -p results/mapping/
mkdir -p results/genotyping/

# load modules
module load bioinfo-tools bwa/0.7.17 samtools/1.8 bcftools/1.8

# index reference genome
bwa index ${ref} &&

# map short read data to reference genome, get bam statistics
for i in HG00731.A HG00731.B HG00733.A;
do
	bwa mem ${ref} data/${i}_1.fastq.gz data/${i}_2.fastq.gz | samtools sort - > results/mapping/${i}.bam
done

# merge bam files from the same sample
samtools merge results/mapping/HG00731.merged.bam results/mapping/HG00731*bam &&
mv results/mapping/HG00733.A.bam results/mapping/HG00733.merged.bam &&

# get bam statistics
for i in HG00731.merged HG00733.merged;
do
	samtools flagstat results/mapping/${i}.bam > results/mapping/${i}.stats.txt;
done

# joint genotyping with bcftools mpileup, get bcf statistics
bcftools mpileup -Ou -Q 30 -q 30 -B -f ${ref} results/mapping/*merged.bam | bcftools call -m -O b -o results/genotyping/all.bcf &&
bcftools stats results/genotyping/all.bcf > results/genotyping/all.stats.txt &&

# remove intermediate files
rm results/mapping/*.bam
