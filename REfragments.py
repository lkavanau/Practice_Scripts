##sequence 
dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

##find RE site
REsite = dna.find("GAATTC")

##lenth of fragments
fragment1 = REsite + 1
fragment2 = len(dna) - fragment1

print("REsite is at " + str(REsite))
print("length of fragment 1 is " + str(fragment1))
print("lenth of fragement 2 is " + str(fragment2))