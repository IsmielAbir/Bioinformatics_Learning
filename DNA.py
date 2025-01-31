from Bio.Seq import Seq

dna_seq = Seq("ATGCGT")

rna_seq = dna_seq.transcribe()
protein_seq = rna_seq.translate()

print("DNA Sequence:", dna_seq)
print("RNA Sequence:", rna_seq)
print('Protine Sequesnce:', protein_seq)