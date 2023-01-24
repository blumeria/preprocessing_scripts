# preprocessing_scripts

A collection of script that help to preprocess data or input files for specific analysis  



#### Kraken/Braken  

add_kraken_taxon_to_genome.py: add the `>sequence16|kraken:taxid|32630` to a flat file (genome assembly) to make it compatible with custom kraken databases  
#### SMRTTools genome assembly pipeline  

01_generate_fofns_pool1.sh: generate fofn files in order to assemble multiple datasets with the microbial genome analysis pipeline  
get_stats_from_pacbio_assemblies.py: get stats our from assembly.fasta and coverage.report.json for a number of folders aka samples
