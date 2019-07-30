import pandas
import time


header = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
dat = pandas.read_csv("data/Homo_sapiens.GRCh38.85.gff3.gz",compression='gzip', names= header , sep='\t', comment ="#")
dat['attributes']  = [{ dd.split("=")[0] : dd.split("=")[1]  for dd in d.split(";") }for d in dat.attributes]

nb_genes = sum(dat.type == "gene")
nb_transcript = sum(dat.type == "transcript")
print("Transcript per genes : {t_per_g}".format(t_per_g = nb_transcript/nb_genes))

gene_ids = dat.loc[dat.type =="gene", "attributes"].apply(lambda x : x['ID'])
count_t2g = {g : 0 for g in tqdm(gene_ids)}
for k in tqdm(dat.loc[dat.type == "transcript", "attributes"]):
    if k['Parent'] in count_t2g:
        count_t2g[k['Parent']] += 1

print("Number of genes with more than one transcript : {0:.2f}".format(sum([v > 1 for k,v  in count_t2g.items()])/len(count_t2g)))




start = time.time()
feature_counts = {k : list(dat.type).count(k) for k in set(dat.type)}
end = time.time()
print("This method took {time} seconds".format( time = end - start ))


start = time.time()
feature_counts = {k : 0 for k in set(dat.type)}
for f in dat.type:
    feature_counts[f] += 1
end = time.time()
print("This method took {time} seconds".format( time = end - start ))





feat_tree = {k['ID'] : [] for k in dat.attributes if "ID" in k}
