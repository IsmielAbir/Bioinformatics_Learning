from Bio.Seq import Seq

def RNA_to_Amino(s):
    
    rna = Seq(s)
    
    protein = rna.translate()
    
    return protein

rna_sequence = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
print(RNA_to_Amino(rna_sequence))
