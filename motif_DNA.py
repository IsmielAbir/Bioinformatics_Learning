def motif_DNA(s, t):
    li = []
    for i in range(len(s)):
        if s[i:i+(len(t))] == t:
            li.append(i)
    return li



print(motif_DNA('CGTAATATA', 'AGTGTGCAG'))
