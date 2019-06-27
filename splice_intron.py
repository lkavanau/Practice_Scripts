from __future__ import division 

##sequence
dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

##splice out intron
exon1 = dna[ :63]
exon2 = dna[91: ]

print("Exon1 is " + str(exon1))
print("Exon2 is " + str(exon2))

##percent of the DNA is coding
coding = len(exon1) + len(exon2)
percent_coding = (coding/len(dna)) * 100
print("The percent of coding DNA is " + str(percent_coding)) + " %"

##show coding in uppercase and noncoding in lowercase
intron = dna[64:91]
print(exon1 + intron.lower() + exon2)