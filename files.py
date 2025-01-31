with open('') as f:
    for line_number, line in enumerate(f, start=1):
        if line_number%2==0:
            print(line.strip())