##import file
seq_file = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/lists_and_loops/exercises/input.txt")

##output file 
trimmseq = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/lists_and_loops/exercises/trimmedLK.txt", "w")

##trim adaptors
for seq in seq_file:
    trimm_dna = seq[14:]
    trimmseq.write(trimm_dna)
    print("trimmed sequence length " + str(len(trimm_dna)))

##close file