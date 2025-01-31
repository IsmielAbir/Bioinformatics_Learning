from Bio.Seq import Seq

s = input()

rev = Seq(s)

k = rev.reverse_complement()
print(k)