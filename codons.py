def create_codon_dict(file_path):
    
    with open(file_path, 'r') as file:
        rows = file.readlines()  
    
    codon_dict = {}  

    for row in rows:
        
        split_row = row.strip().split('\t')  
        codon = split_row[0] 
        amino_acid = split_row[2]  
        codon_dict[codon] = amino_acid  

    return codon_dict  


print(create_codon_dict("data/codons.txt"))


