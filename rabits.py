def rabit(months, offspring):
    child, parent = 1, 1
    
    for i in range(months-2):
        current = parent + (child * offspring)
        child = parent
        parent = current
        
    return parent
    
r = rabit(30,5)
print(r) 