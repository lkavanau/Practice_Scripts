import os
import shutil
import sys  

""" write a program for binning sequences every 100 bp : should be 9 files """

base_directory = ("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/working_with_the_filesystem/exercises/")

for bin_lower in range(100,1000,100):
    bin_upper = bin_lower + 99
    bin_folder_name= str(bin_lower) + "_" + str(bin_upper)
    os.mkdir(base_directory + bin_folder_name)

def process_sequence(line,number):
    dna=line.rstrip("\n")
    length=len(dna)
    print("sequence length is "+ str(length))
    for bin_lower in range(100,1000,100):
        bin_upper = bin_lower + 99
        if length >= bin_lower and length <= bin_upper:
            print("bin is " + str(bin_lower) + " to "+ str(bin_upper))
            bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
            output_path = bin_folder_name + '/' + str(seq_number) + '.dna'

            output=open(base_directory+output_path, "w")
            output.write(dna)
            output.close()

seq_number = 1
for file_name in os.listdir(base_directory):
    if file_name.endswith(".dna"):
        print("reading sequences from "+ file_name)
        dna_file=open(base_directory + file_name)
        for line in dna_file:
            process_sequence(line, seq_number)
            seq_number = seq_number + 1 
