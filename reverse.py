s = input()

sequence = ''

for i in range(len(s)):
    if s[i] =='T':
        sequence+='A'
    elif s[i] == 'A':
        sequence+='T'
    elif s[i] == 'C':
        sequence+='G'
    elif s[i] == 'G':
        sequence+='C'

print(sequence[::-1])