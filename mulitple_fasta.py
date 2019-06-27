##sequences
header1 = "ABC123"
sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"

header2 = "DEF456"
sequence2 = "actgatcgacgatcgatcgatcacgact"

header3 = "HIJ789"
sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

##create multiple fasta file
sequence1_fasta = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/reading_files/exercises/sequence1.fasta", "w")
sequence2_fasta = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/reading_files/exercises/sequence2.fasta", "w")
sequence3_fasta = open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/reading_files/exercises/sequence3.fasta", "w")

##write to fasta files
sequence1_fasta.write(">" + header1 + "\n" + sequence1 + "\n")
sequence2_fasta.write(">" + header2 + "\n" + sequence2.upper() + "\n")
sequence3_fasta.write(">" + header3 + "\n" + sequence3.replace("-", "") + "\n")

#close files
sequence1_fasta.close()
sequence2_fasta.close()
sequence3_fasta.close()