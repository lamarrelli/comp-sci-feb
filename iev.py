n = [18489, 16282, 18433, 19343, 19704, 18038]
probA = [1, 1, 1, 0.75, 0.5, 0]               #AA AA, AA Aa, AA aa, Aa Aa, Aa aa, aa aa
expectedA = sum([n * prob * 2 for n, prob in zip(n, probA)])

print(expectedA)
