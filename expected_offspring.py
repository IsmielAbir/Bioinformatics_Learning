def expected_offspring(list):
    
    probability = [1,1,1,0.75,0.5,0.0]
    
    expected = 0.0
    for i in range(6):
        expected += list[i] * 2 * probability[i]
    return expected

list = list(map(int, input().split()))

print(expected_offspring(list))