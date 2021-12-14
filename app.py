x = int(input("Digite um número inteiro: "))

for i in range(4):
    y = int(input("Digite um número inteiro: "))
    if y > x:
        x = y
print(f"O maior número é {x}")
