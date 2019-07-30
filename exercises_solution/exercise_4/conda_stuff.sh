cd /home/moritz/repos/ebc/data_science/exercises_solution/exercise_4

get ftp://ftp.ensembl.org/pub/release-85/gff3/homo_sapiens/Homo_sapiens.GRCh38.85.gff3.gz
mv Homo_sapiens.GRCh38.85.gff3.gz data

conda create --name ebc_data_science_exo_4 pandas tqdm biopython
conda install --name ebc_data_science_exo_4 ipython
conda activate  ebc_data_science_exo_4
