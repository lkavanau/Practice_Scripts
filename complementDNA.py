##sequence
dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

##lowercase and compliment
dna1 = dna.replace("A", "t")
dna2 = dna1.replace("T", "a")
dna3 = dna2.replace("C", "g")
dna4 = dna3.replace("G", "c")
print(dna4)

##return to uppercase
complement= dna4.upper()

print(complement)