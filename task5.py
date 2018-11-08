n = int(input("unesite n: "))
b=n
c=n

x=[]
broj=1
ProizvodGlavne=1
ProizvodSporedne=1
for i in range(n):
    x.append([])
    for j in range(n):
        x[i].append(broj)
        if i==j:
            ProizvodGlavne*=broj
        if i*j==(n-i-1):
            ProizvodSporedne*=broj
        broj+=1

print ('\n')
print("Generisana matrica: ")
for vektor in x:
    print(vektor)
print ('\n')
print("Proizvod elemenata glavne dijagonale je: "+str(ProizvodGlavne))
print("Proizvod elemenata sporedne dijagonale je: "+str(ProizvodSporedne))

k = 0
l = 0
y=[]
while (k < b and l < c):

    for i in range(l, c):
        y.append(x[k][i])
    k += 1

    for i in range(k, b):
        y.append(x[i][c - 1])
    c -= 1

    if (k < b):
        for i in range(c - 1, (l - 1), -1):
            y.append(x[b - 1][i])
        b -= 1

    if (l < c):
        for i in range(b - 1, k - 1, -1):
            y.append(x[i][l])
        l += 1
print ('\n')
print("Vektor spirale matrice:", y)