def pattern(s, t):
    c = 0
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            c+=1
    return c


s = 'GCGCG'
print(pattern(s, 'GCG'))