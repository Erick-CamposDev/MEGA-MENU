import time


def operador_and(vf, vf2):
    op_and = vf and vf2
    if op_and == 1:
        confirmação = True
    elif op_and == 0:
        confirmação = False
    print(f"O valor final do and é {op_and} ou seja é {confirmação}")
    time.sleep(1.5)


def operador_or(vf,v2):
    op_or = vf or v2
    if op_or == 1:
        confirmação = True
    elif op_or == 0:
        confirmação = False
    print(f"O valor final do or é {op_or} ou seja é {confirmação}")
    time.sleep(1.5)

def operador_not(v):
    op_not = int(not v)
    if op_not == 1:
        confirmação = True
    elif op_not == 0:
        confirmação = False
    print(f"O valor final do not é {op_not} ou seja é {confirmação}")
    time.sleep(1.5)

def tabela_verdade(valores):
    print("Operadores disponíveis: [AND, OR, NOT]")
    while True:
        escolha = input("Escolha seu operador: ").upper().strip()
        if escolha not in ["AND", "OR", "NOT"]:
            print("\033[1;31mERRO! OPERADOR NÃO EXISTE!\033[m")
            continue
        elif escolha == "AND":
            print("CARREGANDO TABELA VERDADE...")
            time.sleep(1.5)
            print("A   |   B   | A and B")
            print("-=" * 17)
            for A in valores:
                for B in valores:
                    resultado = A and B
                    print(f"{A!s:^5} {B!s:^5} {resultado!s:^7}")
            print("-=" * 17)
            time.sleep(1)
            break
        elif escolha == "OR":
            print("CARREGANDO TABELA VERDADE...")
            time.sleep(1.5)
            print("A   |   B   | A or B")
            print("-=" * 17)
            for A in valores:
                for B in valores:
                    resultado = A or B
                    print(f"{A!s:^5} {B!s:^5} {resultado!s:^7}")
            print("-=" * 17)
            time.sleep(1)
            break
        elif escolha == "NOT":
            print("CARREGANDO TABELA VERDADE...")
            time.sleep(1.5)
            print("A   | Not A")
            print("-=" * 7)
            for A in valores:
                resultado = not A
                print(f"{A!s:^5} {resultado!s:^5}")
            print("-=" * 7)
            time.sleep(1)
            break