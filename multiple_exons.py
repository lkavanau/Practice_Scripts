##import seequence and exon file
sequence = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/lists_and_loops/exercises/genomic_dna.txt").read()
exon_pos = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/lists_and_loops/exercises/exons.txt")
coding_sequence= ""

##remove exons from sequence file and concatenate
for line in exon_pos:
    exon_strip = line.rstrip("\n")
    exon_list = exon_strip.split(",")
    start = int(exon_list[0])
    stop = int(exon_list[1])
    exon = sequence[start:stop]
    coding_sequence = coding_sequence + exon
    print(coding_sequence)

##write to an output file
all_exon = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/lists_and_loops/exercises/allexonsLK.txt", "w")
all_exon.write(coding_sequence)
all_exon.close()