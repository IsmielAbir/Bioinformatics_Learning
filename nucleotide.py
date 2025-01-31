from Bio.SeqUtils import gc_fraction
from Bio.Seq import Seq

nucleotide_seq = Seq("ATCGTAGC")

print("Nucleotide Sequence:", nucleotide_seq)

print("Complement:", nucleotide_seq.complement())
print("Reverse Complement:", nucleotide_seq.reverse_complement())

gc_content = gc_fraction(nucleotide_seq) * 100
print(f"GC Content: {gc_content:.2f}%")