numero_de_linhas = int(input("Digite o numero de linhas: "))
numero_de_colunas = int(input("Digite o numero de colunas: "))

# iniciando uma matriz

matrix = []

print("Digite todos os numeros da matriz")

for linha in range(numero_de_linhas):
    a = []
    for coluna in range(numero_de_colunas):
        a.append(int(input()))
    matrix.append(a)

print(matrix)