from __future__ import division

##define function 
def residue(protein, aa):
    protein = protein.upper()
    aa = aa.upper()
    aa_count = protein.count(aa)
    total_aa = len(protein)
    amount = (aa_count/total_aa) * 100
    return(amount)


#base_directory = "/User/test"
#file =base_directory + "/newfile"
#print(file)