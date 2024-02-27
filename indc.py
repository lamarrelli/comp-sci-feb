import math
def indc(n):
    probabilities = [0]*(2*n+1)
    
    for k in range(2*n+1):
        prob = 0
        for i in range(k, 2*n+1):
            prob += math.comb(2*n, i)*((1/2)**(2*n))
        probabilities[k] = math.log10(prob)
    return probabilities[1:]                           #exlude possibility of 0 sharing
n = 47
prob1 = indc(n)
probstr = ' '.join(f"{prob:.3f}" for prob in prob1)
print(probstr)
