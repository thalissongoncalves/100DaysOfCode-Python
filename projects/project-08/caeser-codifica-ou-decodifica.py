import art

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cifra_cesar(direcao_entrada, texto_entrada, deslocamento_entrada):
    palavra = ""
    for letra in texto_entrada:
        if letra in alfabeto:
            indice = alfabeto.index(f"{letra}")
            if direcao_entrada == "codificar":
                palavra += alfabeto[indice + deslocamento_entrada]
            elif direcao_entrada == "decodificar":
                palavra += alfabeto[indice - deslocamento_entrada]
        else:
            palavra += letra
    if direcao_entrada == "codificar":
        print(f"O texto codificado é {palavra}")
    elif direcao_entrada == "decodificar":
        print(f"O texto decodificado é {palavra}")

print(art.logo)

direcao = input("Digite 'codificar' para criptografar, digite 'decodificar' para descriptografar:\n")
texto = input("Digite sua mensagem:\n").lower()
deslocamento = int(input("Digite o número de deslocamento:\n"))

deslocamento = deslocamento % 26

cifra_cesar(direcao_entrada=direcao, texto_entrada=texto, deslocamento_entrada=deslocamento)
pergunta = input("Digite 'sim' se deseja continuar. Caso contrário, digite 'não'\n")
while pergunta == "sim":
    direcao = input("Digite 'codificar' para criptografar, digite 'decodificar' para descriptografar:\n")
    texto = input("Digite sua mensagem:\n").lower()
    deslocamento = int(input("Digite o número de deslocamento:\n"))
    cifra_cesar(direcao_entrada=direcao, texto_entrada=texto, deslocamento_entrada=deslocamento)
    pergunta_dois = input("Digite 'sim' se deseja continuar. Caso contrário, digite 'não'\n")
    if pergunta_dois == "não":
        pergunta = "não"
print("Adeus 👋")
