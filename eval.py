
def eval(n, s, A):
    B = []
    for GC in A:
        probGC = GC/2
        # Probability of A or T
        probAT = (1 - GC) / 2
        
        probs = 1
        for nucleotide in s:
            if nucleotide in ['G', 'C']:
                probs *= probGC
            else:
                probs *= probAT
        
        expected= (n - len(s) + 1) * probs
        B.append(round(expected, 3))
        
    return B
n = 982373
s = "TTCACACG"
A = [0.000, 0.081, 0.129, 0.241, 0.300, 0.324, 0.424, 0.488, 0.528, 0.589, 0.630, 0.747, 0.812, 0.831, 0.909, 1.000]

B = eval(n, s, A)
print(B)
