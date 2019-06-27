import csv

species=[]  
dna=[]
name=[]
expression=[]

def get_AT_content(dna):
    length=len(dna)
    a_count=dna.upper().count('A')
    t_count=dna.upper().count('T')
    at_content=(a_count + t_count) /length
    return at_content

with open('/Users/lkavanau/Documents/python_for_biologists/exercises and examples/conditional_tests/exercises/data.csv') as exercise:
    data=csv.reader(exercise,delimiter=',')
    
    for row in data:
        species=row[0]
        dna=row[1]
        name=row[2]
        expression=int(row[3])
        
        if species == 'Drosophila melanogaster' or species == 'Drosophila simulans':
            print(name)
        if 90 < len(dna) < 110:
            print(name)
        if get_AT_content(dna) < 0.5 and expression > 200:
            print(name)
        if (name.startswith('k') or name.startswith('h')) and not species == 'Drosophila melanogaster':
            print(name)
        if get_AT_content(dna) > 0.65:
            print(name + " has high AT content")
        elif get_AT_content(dna) < 0.45:
            print(name + " has low AT content")
        else:
            print(name + " has medium AT content")