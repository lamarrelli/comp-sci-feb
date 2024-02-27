
def match(s):
    bp = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    x = {}
    
    def cat(i, j):
        if (i, j) in x:
            return x[(i, j)]
        if i >= j:
            return 1
        total=0
        for k in range(i+1, j+1, 2): 
            if s[i] == bp.get(s[k], ''):
                total+=cat(i+1, k-1)*cat(k+1, j)
                total %= 1000000
        
        x[(i, j)] = total
        return total

    return cat(0, len(s) - 1)


s = "AGUUGCAUACGCGCGUAUAAGCAUUAAUUAAUUACGAUGUGCGGCCACGCGCGUACAAUUUUAAAAUCAUGGCAUCGCCGGGCUAAGGAUAGCUCCUUGCAGAUUACGUACAGCGCUAUAUUGCCCGUGCAAUGCCGGUGCGCAUAGUACUUAGCUAUAUAAGCCGUAAGUACUGCUACGCGUACUAACGCGUGCGUACCGAUUCUUAACUAGAUGAUACAUGUAUGCAGCAUCGGCAUUACGUUA"
result = match(s)
print(result)
