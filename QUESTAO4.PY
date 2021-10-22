

print("*****SEQUENCIA DE FETUCCINE******")
n=int(input("digite o primeiro numero:"))
m=int(input("digite o segundo numero:"))
serie = int(0)

print(n,end=',')
print(m,end=',')

for (i) in range(3,10):
    if (i % 2 == 0):
        serie = m-n
    else:
        serie = m+n

    n=m
    m=serie
    print(serie,end=',')


