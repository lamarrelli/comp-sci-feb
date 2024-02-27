n= 1818
m=830
y =[[0]*(n + 1) for _ in range(n + 1)]
mod= 1000000
for i in range(n + 1):
    y[i][0] = 1
    for j in range(1, i + 1):
        y[i][j] = (y[i-1][j-1] + y[i-1][j])%mod  #C(n, k)=C(n-1, k-1)+C(n-1, k)
sum_aspc = sum(y[n][k] for k in range(m, n + 1))%mod
print(sum_aspc)
