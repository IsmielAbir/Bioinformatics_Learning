def pattern_number(s):
    c = 0
    for i in range(len(s)):
        if s[i]=='A':
            c = c*4+0
        elif s[i]=='C':
            c = c*4+1
        elif s[i]=='G':
            c = c*4+2
        elif s[i]=='T':
            c = c*4+3
    return c
            
s = 'AGT'
print(pattern_number(s))  
            