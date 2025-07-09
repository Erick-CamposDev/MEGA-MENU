import sys
import time



def cores():
    return{"Reset": "\033[0m",
           "Preto": "\033[30m",
           "Vermelho": "\033[31m",
           "Verde": "\033[32m",
           "Amarelo": "\033[33m",
           "Azul": "\033[34m",
           "Magenta": "\033[35m",
           "Ciano": "\033[36m",
           "Branco": "\033[37m",
           }

def estilos():
    return {"Normal": "\033[0m",
            "Negrito": "\033[1m",
            "Italico": "\033[3m",
            "Sublinhado": "\033[4m",
            "Invertido": "\033[7m",
            "Cortado": "\033[9m"
            }

def background():
    return {"Reset": "\033[0m",
            "Preto": "\033[40m",
            "Vermelho": "\033[41m",
            "Verde": "\033[42m",
            "Amarelo": "\033[43m",
            "Azul": "\033[44m",
            "Magenta": "\033[45m",
            "Ciano": "\033[46m",
            "Branco": "\033[47m"
            }


def submenu(conteudo_principal, sub_conteudo):
    print("=" * 34)
    print(conteudo_principal)
    print("=" * 34) 
    print(sub_conteudo)
    print("=" * 34)

def title(titulo):
    print("=" * 34)
    print(titulo)
    print("=" * 34)


def menu(conteudo):
    c = cores()
    bg = background()
    e = estilos()
    print("\033[1;31mAVISO! CORES PODEM ENTRAR EM CONFLITOS COM OS FUNDOS!\033[m")
    time.sleep(1.5)

    title("Cores disponíveis: ")
    for cor in c:
        if cor != "Reset":
            print(f"{cor}")
            time.sleep(0.5)
    cor = input("Digite a cor: ").capitalize().strip()
    if cor not in c:
        print("Cor inválida! Branco será utilizado!")
        cor = "Branco"
    
    title("Fundos disponíveis: ")
    for fundo in bg:
        if fundo != "Reset":
            print(f"{fundo}")
            time.sleep(0.5)
    fundo = input("Digite o fundo: ").capitalize().strip()
    if fundo not in bg:
        print("Fundo inválido! Fundo preto será utilizado!")
        fundo = "Preto"
    
    title("Estilos disponíveis: ")
    for estilo in e:
        print(estilo)
        time.sleep(0.5)
    estilo = input("Digite o estilo: ").capitalize().strip()
    if estilo not in e:
        print("Estilo inválido! O estilo normal será utilizado!")
        estilo = "Normal"

    formatação = f"{e[estilo]}{c[cor]}{bg[fundo]}"
    reset = c["Reset"]



    print(f"{formatação}{"=" * 34}")
    print(conteudo)
    print(f"{"=" * 34}{reset}", end= "")
    print()


def saida():
    print("Tudo bem! Fecharemos o programa pra você!")
    time.sleep(1)
    print("Fechando em...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Programa fechado com sucesso!")
    sys.exit()