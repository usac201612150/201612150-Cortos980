def collatz(N):
    Lista = []
    Final = 0
    archivo = open('collatz.txt','w')
    for i in range (2, N+1):
        while (Final != 1):
            Final = ParImpar(i)
            Lista.append(Final)
            archivo.write(str(Lista)+'\n')
    archivo.close()


def ParImpar(num):
    Div = num%2
    if (Div == 0):
        Nuevo = num//2
        return Nuevo
    else: 
        Nuevo = 3*num +1
        return Nuevo

collatz(150)
