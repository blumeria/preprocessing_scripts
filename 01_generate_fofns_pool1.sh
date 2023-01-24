#!/bin/bash

# the pacbio SMRTtools assembly pipeline takes as input bam format

export listdir='/data/projects/p446_Dialact_Phoenix/2_analyses/B_pacbio/202301_assemblies/1_rawdata/fofn_lists_pool1'
export SMRT1='/data/projects/p446_Dialact_Phoenix/2_analyses/B_pacbio/202301_assemblies/1_rawdata/r64293e_20221223_103139_1_A01_pool1/demux_bam'
export SMRT2='/data/projects/p446_Dialact_Phoenix/2_analyses/B_pacbio/202301_assemblies/1_rawdata/r64293e_20221228_134539_1_A01_pool1/demux_bam'

declare -a barcodes
readarray -t barcodes < sample_barcode_map_pool1.csv

for i in ${barcodes[@]}; do

echo $i

barcode=$(cut -d "," -f 2 <<< $i)
#echo $barcode 
strain=$(cut -d "," -f 1 <<< $i)
#echo $strain

touch ${listdir}/${strain}_reads.fofn
readlink -f ${SMRT1}/${barcode}/*bam >> ${listdir}/${strain}_reads.fofn
readlink -f ${SMRT2}/${barcode}/*bam >> ${listdir}/${strain}_reads.fofn
readlink -f ${SMRT3}/${barcode}/*bam >> ${listdir}/${strain}_reads.fofn
done












