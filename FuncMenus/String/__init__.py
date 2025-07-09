import time

def submenuString(conteudo_principal, sub_conteudo):
    print("=" * 34)
    print(conteudo_principal)
    print("=" * 34) 
    print(sub_conteudo)
    print("=" * 34)

def substuição(frase):
    print(f"Frase atual: {frase}")
    palavra_antiga = input("Digite a palavra que deseja substituir: ")
    palavra_nova = input("Digite a nova palavra: ")
    if palavra_antiga in frase:
        nova_frase = frase.replace(palavra_antiga, palavra_nova)
        print(f"A nova frase ficou: \033[1;37m{nova_frase}\033[m")
    else:
        print("\033[1;31mERRO! PALAVRA NÃO ENCONTRADA!\033[m")
    

def maiuscula(str):
    upper = str.upper()
    print(f"A palavra {str} em maiusculas ficou {upper}")

def minuscula(str):
    lower = str.lower()
    print(f"A palavra {str} em minusculas ficou {lower}")

def titulo(str):
    title = str.title()
    print(f"A palavra {str} em titulo ficou {title}")

def capitalizado(str):
    capitalized = str.capitalize()
    print(f"A palavra {str} capitalizada ficou {capitalized}")

def menu_transformação(str):
    while True:
        print("Carregando menu de transformação...")
        time.sleep(1)
        submenuString("Opções de transformação de strings escolha uma...",
                                      "[S] Substituição\n"
                                      "[U] Maiúscula/Upper\n"
                                      "[L] Minúscula/Lower\n"
                                      "[T] Título\n"
                                      "[C] Capitalizado\n"
                                      "[V] Voltar")
        opções = input("Digite sua opção de transformação: ").upper().strip()
        if opções == "S":
            substuição(str)
        elif opções == "U":
            maiuscula(str)
        elif opções == "L":
            minuscula(str)
        elif opções == "T":
            titulo(str)
        elif opções == "C":
            capitalizado(str)
        elif opções == "V":
            print("Voltando ao programa...")
            time.sleep(1.5)
            break
        else:
            print("\033[1;31mERRO! DIGITE O VALOR CORRETO!\033[m")            


def leitura(str):
    return len(str)

def contador(string):
    letra = input("Qual letra você que você contar?: ")
    if letra in string:
        cont = string.count(letra)
        print("Contando letras...")
        time.sleep(1)
        print(f"Sua string possui {cont} letras")
    else:
        print("\033[1;31mERRO! SUA LETRA NÃO EXISTE NA STRING\033[m")

def procurador(string):
    caractere = input("Digite o caractere que você deseja procurar: ")
    if caractere in string:
        proc = string.find(caractere)
        print("Procurando posição...")
        time.sleep(1.5)
        print(f"O caractere {caractere} foi encontrado na {proc}° posição!")
    else:
        print("\033[1;31mERRO! O CARACTERE NÃO FOI ENCONTRADO NA STRING!\033[m")

def fatiamento(str):
    fatiamento1 = input("Digite o primeiro numero para fatiar: ")
    fatiamento2 = input("Digite o segundo número para fatiar: ")
    fatiamento3 = input("Digite o terceiro número para fatiar: ")

    if fatiamento1 == "":
        fatiamento1 = None
    else:
        fatiamento1 = int(fatiamento1)

    if fatiamento2 == "":
        fatiamento2 = None
    else:
        fatiamento2 = int(fatiamento2)

    if fatiamento3 == "":
        fatiamento3 = None
    else:
        fatiamento3 = int(fatiamento3)

    fatiamento_final = str[fatiamento1:fatiamento2:fatiamento3]
    print("Fatiando string...")
    time.sleep(1.5)
    print(f"A string fatiada ficou {fatiamento_final}!")

def menu_analise(str):
    while True:
        print("Carregando o menu de análise...")
        time.sleep(1)
        submenuString("Opções de análise de strings, escolha uma...",
                                      "[L] Leitura\n"
                                      "[C] Contador\n"
                                      "[P] Procurador\n"
                                      "[V] Voltar")
        opções = input("Digite sua opção: ").upper().strip()
        if opções == "L":
            print(f"A string possui {leitura(str)} caracteres!")
        elif opções == "C":
            contador(str)
        elif opções == "P":
            procurador(str)
        elif opções == "V":
            print("Voltando ao programa...")
            time.sleep(1.5)
            break
        else:
            print("\033[1;31mERRO! DIGITE O VALOR CORRETO!\033[m")

def divisão_junção(str):
    divisão = str.split()
    print("Dividindo a string...")
    time.sleep(1.5)
    print(f"A frase dividida ficou {divisão}")
    time.sleep(0.5)
    while True:
        escolha = input("Deseja utilizar a junção? [S/N]: ").upper().strip()
        if escolha == "S":
            caractere = input("Digite o caractere que deseja para unir a string: ").upper().strip()
            junção = caractere.join(divisão)
            print("Unindo a string...")
            time.sleep(1.5)
            print(f"A string unida ficou {junção}")
        elif escolha == "N":
            print("Voltando ao programa...")
            time.sleep(1.5)
            break
        else:
            print("\033[1;31mERRO! DIGITE O VALOR CORRETO!\033[m")




