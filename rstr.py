N = 93927 
x= 0.487975
s = "AATGGGAC"
probS = 1                    #S in GC
for nucleotide in s:
    if nucleotide in ['G', 'C']:
        probS*= x/2 
    else:
        probS*=(1-x)/2
probScom = 1 - probS
probScomN = probScom ** N
prob_atleastOneS = 1 - probScomN
print(prob_atleastOneS)