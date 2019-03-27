#! /usr/bin/python

"""
This script is used to generate random DNA sequences of length not more than 80 nucleotides. 
The input arguments ;
  noSeqs: The user inputs the number sequences to be generated
  lenSeq: The user inputs the length of sequences to be generated
  outfile:  The user inputs the name of the file with the extension .fasta
"""

import sys   #This module interacts with linux sys 
from random import choice  # This module generates random elements from a given sequence



def wakandaSnakes (noSeqs,lenSeq,outfile):
    """
    Generates random DNA sequences in fasta format 
    """
    out = '../Data/'+outfile
    if int(lenSeq) <=80: #To limit length of sequence
        with open (out, "w") as myfile:
            for i in range (1,noSeqs+1):
                header=">"+"snake_sequence"+str(i)  #fasta format header
                myfile.write("%s\n" %header) #write header to new file
                DNA=""                       #empty DNA string
                for c in range (lenSeq):
                    DNA+=choice("ATGC")     #defines contents of sequence and generates random sequences using choice 
                myfile.write("%s\n" %DNA)
    else:
        print ("Length of sequence is longer than 80 nucleotides")


noSeqs=int(sys.argv[1])
lenSeq=int(sys.argv[2])
outfile=sys.argv[3]
wakandaSnakes (noSeqs,lenSeq,outfile)
