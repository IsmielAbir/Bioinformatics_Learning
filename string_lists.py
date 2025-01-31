given_text = input()

a, b, c, d = map(int, input().split())

r = given_text[a:b+1] +" "+ given_text[c:d+1]
print(r)
        