def DNA(sequence):
    temp = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in sequence:
        temp[i]+=1
    return temp

input_DNA = "TGAAGCTCCAAAGTACACTTCCACAAAAGGTACAGGCCTAGATGATGGGCGCTCTTGTTAACAATCATCTGAGCTCCAGCAGTACTGATGATTGCCGCTGGATCCCACCGGCGCGTAAGTAGTGGGCAGGGGTGTTGGGGGAGAATGAAATAAATTGAAATGATGAATTTTTAAGAGCGAACGCCTTAGACCTCTCTTGACCTTAGTACAAATGCTACGGACACAGACCCATGTTAGGATGTCCCATTGGCAGCTCCACAATATCATGATCCGGGCTCTTGGCGTTACTGTAGCCTGTGCGCGGATGGTAATTACGTAGACAGATTAAGTAGACGTTGCGACTCCATGGTGCAACCCGGCTCTAACTTGCCTAGAAGCTTAGGGCTCCAGCAGTTGGGGGTTCGGGAGCTACGGTAGACCGATTGTTGTAGAGGTAGCCTATCTTTCACTTCTAAAGGAAATACGTCCTATTAAAATGATCACATCTCGTACATCATCGTACCTTAAAGGCAGCTGGTGCTCCTTGGCGAACGACGTGTCCTAATGGAACACACCTGGGCTATTATGCAATACGTGGCTTGTACCTCGTACCTGATGGGGCATATGTGATCGAGCTTTGTCATGCCGACCGCTGTCACTTTAAGCGCGGAAATCTAAGCGGAGAAGCCCGTGGGTATTACGTTAGGTAAGAATACTCGAACACTATAATCCGCGTACATGCGCGTTCTTATTTAAGATTCCCGGCTGTCGCCGGTCCGTGGAGTATCATACCTTGGCTGCCACAAAGGGTTGCGGATCAGAGGTCCATTCATCAAAGTCCTGCAATAATGAGTGTCTGATCGGATAGCGAAGTGTAATCGGGTAAGTCAGCATTGCGGAAGTGGG"

print(DNA(input_DNA))