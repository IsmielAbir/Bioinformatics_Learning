from Bio.Seq import Seq

def RNA_Protine(RNA):
    rna_seq = Seq.translate(RNA)
    return rna_seq

print(RNA_Protine('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'))