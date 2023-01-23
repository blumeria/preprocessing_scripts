"""
add a kraken taxon to each sequence in a flat file so that is is 
compatible with kraken format:

>sequence16|kraken:taxid|32630  Adapter sequence
CAAGCAGAAGACGGCATACGAGATCTTCGAGTGACTGGAGTTCCTTGGCACCCGAGAATTCCA

Simone Oberhaensli, 2023-01-23


run like this:

$ python3 add_kraken_taxon_to_genome.py --id=32630 --description='some informative description' --assemblyfile=genome.fa

runs with Python 3.5.2
"""


import argparse
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord




# add id and description to each sequence
# has to have the following format
# >sequence16|kraken:taxid|32630  Adapter sequence
def add_id(record,taxid,descr):
    newid = record.id + '|kraken:taxid|' + taxid
    record.id = newid
    record.description = descr
    return(record)  

# loop through genome file and process each sequence, then write to file
def process_flatfile(flatfile, taxid, descr):
    file_out='genome_kraken.fasta'
    with open(file_out, 'w') as f_out:
        for seq_record in SeqIO.parse(open(flatfile, mode='r'), 'fasta'):
            newseq = add_id(seq_record, taxid, descr)
            r = SeqIO.write(newseq, f_out, 'fasta')
            if r!=1: print('Error while writing sequence:  ' + newseq.id)

def main():
    # list of samples required with its corresponding identifier
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument("--id", help="TaxID of the organism")
    parser.add_argument("--assembly", help="assembly in fasta format")
    parser.add_argument("--description", help="additional info that goes into the description")
    args = parser.parse_args()
    print(args)

    myflat = args.assembly
    mytaxid = args.id
    descr = args.description
    flatrenamed = process_flatfile(myflat, mytaxid, descr)

if __name__ == "__main__":
    main()
