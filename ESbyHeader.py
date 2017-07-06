# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:38:49 2017

"""

from Bio import SeqIO

fd = open('/Users/YuKeji/Downloads/A2-5SNPID.txt','r')
fd_data = fd.readlines()
all_list = []

for i in fd_data:
    s = i.strip('\n')  #strip ENTER!
    all_list.append(s)
    #print(s)
fd.close()

#print(all_list)
Fasta_2B_extract = open('/Users/YuKeji/Downloads/All-Unigene.fa','r')
output_file = open('/Users/YuKeji/Downloads/A2-5SNPID.fa','a')
for key in SeqIO.parse(Fasta_2B_extract, 'fasta'):
    if key.name.split()[0] in all_list:       #strip characters after SPACE
        output_file.write(str('>' + (key.id)) + '\n')
        output_file.write(str(key.seq[0:]) + '\n') 
output_file.close()
Fasta_2B_extract.close()
