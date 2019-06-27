##read in sequence 
dna_file = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/reading_files/exercises/genomic_dna.txt")
my_dna = dna_file.read()

##define intron and exons
exon1= my_dna[0:63]
intron= my_dna[63:90]
exon2 = my_dna[90:]

##create new files
coding_file = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/reading_files/exercises/coding_dnaLK.txt", "w")
noncoding_file = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/reading_files/exercises/noncoding_dnaLK.txt", "w")

##write to new files
coding_file.write(exon1 + exon2)
noncoding_file.write(intron)