##sequences
header1 = "ABC123"
sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"

header2 = "DEF456"
sequence2 = "actgatcgacgatcgatcgatcacgact"

header3 = "HIJ789"
sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

##create fasta file
fasta_file = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/reading_files/exercises/fastaLK.txt", "w")

##write to fasta file
fasta_file.write(">" + header1 + "\n" + sequence1 + "\n")
fasta_file.write(">" + header2 + "\n" + sequence2.upper() + "\n")
fasta_file.write(">" + header3 + "\n" + sequence3.replace("-", "") + "\n")

#close file
fasta_file.close()