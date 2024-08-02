# Solicita o nome e a quantidade de XP do herói
nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de XP do herói: "))

# Determina o nível com base na quantidade de XP
if xp < 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 5000:
    nivel = "Prata"
elif 5001 <= xp <= 7000:
    nivel = "Ouro"
elif 7001 <= xp <= 8000:
    nivel = "Platina"
elif 8001 <= xp <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Exibe o resultado
print(f"O Herói {nome} está no nível {nivel}")
