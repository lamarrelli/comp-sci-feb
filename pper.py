def partialperm(n, k, modulo=1000000):

    result = 1
    for i in range(k):
        result = (result*(n-i))%modulo
    return result

n = 94
k = 9
print(partialperm(n,k))