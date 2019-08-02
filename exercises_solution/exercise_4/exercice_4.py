import pandas
import time

# create a gff header
header = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']

# pandas one-liner to load the gziped-gff
dat = pandas.read_csv("data/Homo_sapiens.GRCh38.85.gff3.gz",compression='gzip', names= header , sep='\t', comment ="#")

# turn the attributes column into a dictionary

dat['attributes']  = [{ dd.split("=")[0] : dd.split("=")[1]  for dd in d.split(";") }for d in dat.attributes]

# simple way of getting transcript per genes 
nb_genes = sum(dat.type == "gene")
nb_transcript = sum(dat.type == "transcript")

# format is a nice function for output
print("Transcript per genes : {t_per_g}".format(t_per_g = nb_transcript/nb_genes))

# using the attribute dictionary to count transcripts
gene_ids = dat.loc[dat.type =="gene", "attributes"].apply(lambda x : x['ID'])
count_t2g = {g : 0 for g in tqdm(gene_ids)}
for k in tqdm(dat.loc[dat.type == "transcript", "attributes"]):
    if k['Parent'] in count_t2g:
        count_t2g[k['Parent']] += 1

print("Number of genes with more than one transcript : {0:.2f}".format(sum([v > 1 for k,v  in count_t2g.items()])/len(count_t2g)))


# This is simple but is gonna take FOREVEEEEEEEEER
start = time.time()
feature_counts = {k : list(dat.type).count(k) for k in set(dat.type)}
end = time.time()
print("This method took {time} seconds".format( time = end - start ))


# This one is way faster, why?
start = time.time()
feature_counts = {k : 0 for k in set(dat.type)}
for f in dat.type:
    feature_counts[f] += 1
end = time.time()
print("This method took {time} seconds".format( time = end - start ))


# check what is in count_t2g

#why are there so many genes with no transcripts???

#let's organise all feats in a "tree" 
feat_tree = {k['ID'] : [] for k in dat.attributes if "ID" in k}
