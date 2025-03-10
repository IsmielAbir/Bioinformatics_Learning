def humming_distance(s, t):
    c=0
    for i in range(len(s)):
        if s[i] not in t[i]:
            c+=1
    return c


print(humming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))
