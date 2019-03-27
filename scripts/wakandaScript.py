#! /usr/bin/python

"""
This script is used to generate random DNA sequences of length 80 nucleotides in a line. 
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

    out = "../Data/" + outfile
   
    with open (out, "w") as myfile:
        count = 0                   #Initialize counter
        for i in range (1,noSeqs+1):
            header=">"+"snake_sequence"+str(i)  #fasta format header
            myfile.write("%s \n" %header) #write header to new file
            DNA=""
            for c in range (lenSeq):
                DNA+=choice("ATGC")
            for i in DNA: 
                count += 1 # add one to counter for every character in DNA
                if count <= 80: # Each line should not exceed 80 characters
                    myfile.write("%s" %i)
                else:
                    myfile.write("\n")
                    myfile.write("%s" %i) #This will account the lost nucleotide after introducing a new line  
                    count = 1             #Note:if we dont specifically print this character, it is replaced by a new line character
            count = 0                     #Intialize the counter back to 0 for another loop with a new seq
            myfile.write("\n")            #Print the new line of the next sequence 
                

    
    
noSeqs=int(sys.argv[1])
lenSeq=int(sys.argv[2])
outfile=sys.argv[3]
wakandaSnakes (noSeqs,lenSeq,outfile)
