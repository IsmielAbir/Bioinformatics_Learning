def Num(s):
    a=c=g=t=0
    for i in s:
        if i == 'A':
            a+=1
        elif i == 'C':
            c+=1
        elif i == 'G':
            g+=1
        elif i == 'T':
            t+=1
    return str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)

print(Num('GTGCACCTGACTCGCACAGAACGCCTTCAGAGGCGCGCATGTTGGATTACTGGTCTGCCTTTATTCACCACGAACCAGAGGTGACCGATGAGGCGCCGCGGAGCTCTTTTTACATGAGGCTGGTGCTGCATAACGCCTTAGCTATTACAGCTGGATGTCCCTTTGGAACCAGTAGCTATCATTCCCAGTTAATACTACCCTCCAGGGTGCCTGTTACTTTATTTCAACGCAAGCGCTAAGTCCGTTCGTCCCTCACGTGTGAAGGCCGGATTCACTAATTCGATTCTTCAACAGGTAGGGTTAATGAGGCGGGTACAACTCCAGCTAGGGATCATCGGGACGTCTGGCGTTCGTCCTGGGGGGGCGCCATAGTCTACCGGCGGCGGGGACTTAGCAGAGGGGACTGATAGAACTGTGGTTACAGATCCACCTGTAGTTGGGTATCGGCTAGTTACTATGTGTGTAGAAATCGCGGCTTCAGGGCCGGGACGGTCGCATGGATTTAGAAGCTTTTTGCACAACATCTTTGGTGGAGAGGTCATTAACTTGCCCCTAAGTGGAACTGGAAACGTAACCTCAGTCTATGAATGAGGATAGGTGACTTGACAAATTAGGCCACAATCTCTCGTTTATTGGGTTGACGACCAGAGAAAAGTTTTATACTAGGCGGAGACTCGCCACAGTGGAGTTTGAGTGTTATCTTATATCTGACCCTGTTCGAAGATTTCCGTCAAACTCATAGACCCATGCATTTGCTACACCGACCTACGTGTAGTAATAACTCCCGTTTCTTCGATGTCACCGTTGACGTCAGTGCTACGTCCGTGACT'))