import re

accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

#for acc in accs:
    #if re.search(r"5",acc):
    #if re.search(r"(d|e)", acc):
    #if re.search(r"d.*e",acc):
    #if re.search(r"d.e",acc):
    #if re.search(r"d.*e",acc) or re.search(r"e.*d",acc):
    #if re.search(r"^(x|y)",acc):
    #if re.search(r"^(x|y).*e$",acc):
    #if re.search(r"\d{3,}",acc):
    #if re.search(r"d[a|r|p]$",acc):
    #    print(acc)

sequence=open("/Users/lkavanau/Documents/python_for_biologists/exercises and examples/regular_expressions/exercises/dna.txt")
dna=sequence.read().rstrip("\n")
## create an empty list
all_cuts= [0]

## add cut positions for abcI
for match in re.finditer(r"A[ATCG]TAAT",dna):
    all_cuts.append(match.start()+3)

## add cut position for abcII
for match in re.finditer(r"GC[AG][AT]TG",dna):
    all_cuts.append(match.start()+4)

## add final position and put them in ascending order
all_cuts.append(len(dna))
sort_cuts=sorted(all_cuts)
print(sort_cuts)

for i in range(1,len(sort_cuts)):
    cut_position = sort_cuts[i]
    previous_cut_position = sort_cuts[i-1]
    fragment_size = cut_position - previous_cut_position
    print("one fragment size is " + str(fragment_size))