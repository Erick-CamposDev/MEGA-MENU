import time
from .. import design_ui

def submenuFloat(conteudo_principal, sub_conteudo):
    tam = len(conteudo_principal)
    print("=" * tam)
    print(conteudo_principal)
    print("=" * tam) 
    print(sub_conteudo)
    print("=" * tam)

def casa_decimal(a):
    a_str = str(a)
    if "." in a_str:
        casas = len(a_str.split(".")[1])
        return casas
    else:
        return "\033[1;31mNÃO POSSUI\033[m"

def menu_inteiro(numf):
    while True:
            perm = input("Deseja ir pro menu extra? [S/N]: ").upper().strip()
            if perm == "S":
                while True:
                    print("Carregando menu extra!")
                    time.sleep(1)
                    submenuFloat("\033[1mMenu Extra com Inteiros oque você vai fazer?\033[m", "[B] Binário\n" 
                                            "[O] Octal\n"
                                            "[H] Hexadecimal\n"
                                            "[S] Sair")
                    opções_extras = str(input("Digite sua opção extra!: ")).upper().strip()
                    if opções_extras == "B":
                                            print("Convertendo o número para binário...")
                                            time.sleep(1)
                                            numBIN = bin(numf)[2:]
                                            print(f"O número {numf} em binário é {numBIN}")
                    elif opções_extras == "O":
                                            print("Convertendo o número para octal...")
                                            time.sleep(1)
                                            numOCT = oct(numf)[2:]
                                            print(f"O número {numf} em octal é {numOCT}")
                    elif opções_extras == "H":
                                            print("Convertendo o número para hexadecimal...")
                                            time.sleep(1)
                                            numHEX = hex(numf)[2:]
                                            print(f"O número {numf} em hexadecimal é {numHEX}")
                    elif opções_extras == "S":
                            design_ui.saida()
                    else:
                        print("\033[1;31mERRO! DIGITE O VALOR CORRETO!\033[m")
                        time.sleep(1.5)
                        continue
            elif perm == "N":
                print("Voltando ao menu de floats...")
                time.sleep(0.5)
                break
            else:   
                print("\033[1;31mVALOR INCORRETO! DIGITE NOVAMENTE!\033[m")


def conversão(numf):
    while True: 
        print("Convertendo o número para inteiro...")
        inteiro = int(numf)
        time.sleep(1.5)
        print(f"O número convertido foi para {inteiro}!")
        menu_inteiro(inteiro)



