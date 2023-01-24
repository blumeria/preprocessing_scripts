#!/bin/bash
#SBATCH --job-name=p446
#SBATCH --error=%J.err
#SBATCH --output=%J.out
#SBATCH --mem=5G
#SBATCH --time=72:0:0
#SBATCH --cpus-per-task=6

# read in all fams

export listdir='/data/projects/p446_Dialact_Phoenix/2_analyses/B_pacbio/202301_assemblies/1_rawdata/fofn_lists_pool1'
export resultsdir='/data/projects/p446_Dialact_Phoenix/2_analyses/B_pacbio/202301_assemblies/3_assemblies/results/pool1'


declare -a strains
readarray -t strains < sample_list_pool1.txt


for i in ${strains[@]}; do

echo processing $i

singularity exec --bind /data /software/singularity/containers/SMRT-Link-11.0.0.146107-1.ubuntu20.sif \
pbcromwell run pb_assembly_hifi_microbial --nproc 5 \
--task-option ipa2_genome_size="5M" \
--task-option reads=${listdir}/${i}_reads.fofn \
--output-dir=${resultsdir}/${i}

done
