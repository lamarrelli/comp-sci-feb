def match(s):
    bp = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    
    x = {}
    
    def motz(i, j):
        if i >= j:
            return 1 
        if (i, j) in x:
            return x[(i, j)]
        total = motz(i + 1, j)
        for k in range(i+1, j+1):
            if s[i] == bp.get(s[k], ''): 
                total += motz(i+1, k-1)*motz(k+1, j)
                total %= 1000000
        
        x[(i, j)] = total
        return total
    

    return motz(0, len(s) - 1)
s = "AACGUAGUUACGCACCAGCUUAUUCGGAGGGAGGACUUGGCUAGGCUCAGCAGCCACGUGGACCAACAUCGUACGCGAUAAUGUGUUCACAAUAGCACCAGCCCAGUGCGGAUCUUCAAUGUCACAACAUAACCUUAGCCGACCUUACUCCGGCGAGGUGUGCAAUGGUAGCCACAUUGGUUCUUCAAGUUCGUGAUUCAACGACGAACUCAUCUCGUUACAGUGGUUAAGAAUAACGUUGACUUAGCGA"
result = match(s)
print(result)

