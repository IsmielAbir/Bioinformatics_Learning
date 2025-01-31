s = input()

words = s.split()

l = {}

for word in words:
    if word in l:
        l[word] +=1
    else:
        l[word] = 1
for word, count in l.items():
    print(f"{word} {count}")
