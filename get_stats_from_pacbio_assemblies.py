"""
collect information from each assembly:
number of contigs
number of circular and complete contigs
mean coverage

Simone Oberhaensli, 2023-01-24

Tested with Python 3.5.2

usage: 

$ python3 get_stats_from_pacbio_assemblies.py --help
usage: get_stats_from_pacbio_assemblies.py [-h]
                                           [--results_folder RESULTS_FOLDER]
                                           [--prefix PREFIX]

description
optional arguments:
  -h, --help            show this help message and exit
  --results_folder RESULTS_FOLDER
                        location where the folders of each sample are
  --prefix PREFIX       output_prefix
"""

import argparse
import os
import os.path
import Bio
from Bio import SeqIO
import json
import csv


# output csv structure:
# strain, nr ctgs, nr complete contigs, mean coverage


# loop through each folder
def loop_folder(mypath):
    statslist = []
    for dir in os.listdir(mypath):
        print(dir)
        path = mypath + '/' + dir
        #print(path)
        try:
            (nrctgs, nrcompctgs) = process_assembly(path)
            #print("{} {}".format(nrctgs, nrcompctgs))
            covlist = get_coverage(path)
            meancov = covlist[0]
            missingbp = covlist[1]
        except:
            print("can not analyse {}".format(dir))
 
        entry = (",".join([dir, str(nrctgs), str(nrcompctgs),str(meancov),str(missingbp)]))
        statslist.append(entry)
    return(statslist)

def process_assembly(folder):
    assembly_file = folder + '/outputs/assembly.rotated.polished.renamed.fsa'
    ctgnr = 0
    completenr = 0
    for seq_record in SeqIO.parse(open(assembly_file, mode='r'), 'fasta'):
        ctgnr+=1
        if 'complete' in seq_record.description:
            completenr+=1
    return(ctgnr,completenr)

def get_coverage(folder):
    list = []
    cov_report = folder + '/outputs/coverage.report.json'
    report = open (cov_report, "r")
    data = json.loads(report.read())
    for i in data['attributes']:
        value = i['value']
        list.append(value)
    return(list)




def main():
    # list of samples required with its corresponding identifier
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument("--results_folder", help="location where the folders of each sample are")
    parser.add_argument("--prefix", help="output_prefix")
    args = parser.parse_args()
    #print(args)

    resultsfolder = args.results_folder
    prfx = args.prefix
    resultslist = loop_folder(resultsfolder)
    outfile = prfx + '_assembly_stat.csv'
    f = open(outfile, "w")
    f.write("strain, nr_ctgs, nr_complete_contigs, mean_coverage, missing_bases\n")
    for row in resultslist:
        print(row, file=f)
    f.close()


if __name__ == "__main__":
    main()
