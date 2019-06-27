from __future__ import division

##DNA sequence
dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

##count the length of the DNA sequence
total = len(dna)
print("length is " + str(total) + " nucleotides")

##count the number of A
total_A = dna.count("A")
print("number of A is " + str(total_A))

##count the number of T
total_T = dna.count("T")
print("number of T is " + str(total_T))

##number of AT
total_AT = total_A + total_T
print("total number of AT is " + str(total_AT))

##percent of AT
percent_AT = (total_AT/total) * 100
print("The DNA sequence is " + str(percent_AT) + " % AT")

