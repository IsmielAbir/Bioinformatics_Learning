sequence = input().upper()


a = b = c = d = 0
for i in sequence:
    if i == 'A':
        a+=1
    elif i =='T':
        b+=1
    elif i =='G':
        c+=1
    elif i =='C':
        d+=1
        
print(f"{a} {d} {c} {b}")