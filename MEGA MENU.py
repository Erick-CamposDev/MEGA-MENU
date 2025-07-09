import time
from FuncMenus import design_ui, Inteiro, Float, String, Boolean

print("-=" * 17)
print("MEGA MENU TIPOS")
print("-=" * 17)

while True:
    perm = str(input("Quer começar o programa? [Sim] [Não]: ")).capitalize().strip()
    if perm == "Sim":
        design_ui.menu("Selecione o tipo primitivo:\n"
                        "[I] Inteiro\n"
                        "[F] Float\n" 
                        "[ST] String\n" 
                        "[B] Booleano\n" 
                        "[S] Sair")
        while True:
            escolha = str(input("Selecione o tipo primitivo!: ")).upper().strip()
            if escolha == "I":
                while True:
                    num1 = 0
                    num2 = 0
                    design_ui.submenu("Oque você quer fazer com inteiros?:",
                    "[+] Soma\n" 
                    "[-] Subtração\n" 
                     "[*] Multiplicação\n" 
                     "[/] Divisão\n"
                     "[**] Potência\n"
                     "[R] Raiz\n"
                     "[V] Voltar\n" 
                     "[S] Sair")
                
                    opções1 = str(input("Digite sua opção: ")).upper().strip()
                    if opções1 in ["+","-","*","/","**"]:
                        num1 = int(input("Digite um número: "))
                        num2 = int(input("Digite outro número: "))
                    
                        if opções1 == "+":
                            print(f"A soma de {num1} + {num2} = {Inteiro.soma(num1, num2)}")
                            time.sleep(1.5)
                        elif opções1 == "-":
                            print(f"A diferença entre dos números {num1} - {num2} = {Inteiro.subtração(num1, num2)}")
                            time.sleep(1.5)
                        elif opções1 == "*":
                            print(f"O produto dos números {num1} x {num2} = {Inteiro.multiplicação(num1, num2)}")
                            time.sleep(1.5)
                        elif opções1 == "/":
                                print(F"O quociente dos números {num1} / {num2} = {Inteiro.divisão(num1, num2)}")
                                time.sleep(1.5)
                        elif opções1 == "**":
                            print(f"A potência dos números {num1} ** {num2} = {Inteiro.potenciação(num1, num2)}")
                            time.sleep(1.5)
                    elif opções1 == "R":
                        num = int(input("Digite um número para a raiz quadrada: "))
                        print(f"A raiz de {num} é {Inteiro.raiz(num)}")
                        time.sleep(1.5)  
                    elif opções1 == "V":
                        print("Voltando ao programa...")
                        time.sleep(1.5)
                        break
                    elif opções1 == "S":
                        design_ui.saida()
                    else:
                        print("Valor inválido! Por favor digite o valor correto!")
                        time.sleep(1.5)
                        continue
            elif escolha == "F":
                while True:
                    numf = 0
                    design_ui.submenu("Oque você vai fazer com o float?: ",
                                        "[C] Contar casa decimais\n"
                                        "[A] Arrendondamento\n"
                                        "[I] Inteiro\n" 
                                        "[V] Voltar\n" 
                                        "[S] Sair")
                    opções2 = str(input("Digite sua opção: ")).upper().strip()
                    if opções2 in ["C","A","I"]:
                        numf = float(input("Digite o número em float: "))
                        if opções2 == "C":
                                print(f"O número {numf} tem a posse de{Float.casa_decimal(numf)} casas decimais!")
                                time.sleep(1.5)
                        elif opções2 == "A":
                            print(f"O número {numf} foi arrendodado para {round(numf)}")
                            time.sleep(1.5)
                        elif opções2 == "I":
                                Float.conversão(numf)
                        elif opções2 == "V":
                            print("Voltando ao programa...")
                            time.sleep(1.5)
                            break
                        elif opções2 == "S":
                            design_ui.saida()
                        else:
                            print("Valor inválido! Por favor digite o valor correto!")
                            time.sleep(1.5)
                            continue
                        
            elif escolha == "ST":
                while True:
                    string = []
                    design_ui.submenu("Oque você vai fazer com as strings?:",
                                "[T] Transformação\n"
                                "[A] Análise\n"
                                "[F] Fatiamento\n"
                                "[DJ] Divisão e Junção\n"
                                "[V] Voltar\n"
                                "[S] Sair")
                    opções3 = str(input("Digite sua opção: ")).upper().strip()
                    if opções3 in ["T","A","F","DJ"]:
                        string = str(input("Digite a palavra frase ou número: "))
                        if opções3 == "T":
                            String.menu_transformação(string)
                        elif opções3 == "A":
                            String.menu_analise(string)
                        elif opções3 == "F":
                            String.fatiamento(string)
                        elif opções3 == "DJ":
                            String.divisão_junção(string)
                    elif opções3 == "V":
                            print("Voltando ao programa...")
                            time.sleep(1.5)
                            break
                    elif opções3 == "S":
                          design_ui.saida()
                    else:
                        print("Valor inválido! Por favor digite o valor correto!")
                        time.sleep(1.5)
                        continue
            elif escolha == "B":
                while True:
                    design_ui.submenu("O que você vai fazer com Booleanos?",
                                        "[A] AND ^\n"
                                        "[O] OR  v\n"
                                        "[N] NOT ~\n"
                                        "[T] TABELA VERDADE\n"
                                        "[V] Voltar\n"
                                        "[S] Sair")
                    opções4 = str(input("Digite sua opção: ")).upper().strip()
                    valores = [True, False]
                    if opções4 in ["A", "O"]:
                        VF = str(input("Digite o número 0 ou 1: "))
                        VF2 = str(input("Digite outro número 0 ou 1: "))
                        if VF in ["0", "1"] and VF2 in ["0", "1"]:
                            VF = int(VF)
                            VF2 = int(VF2)
                        else:
                            print("Valor invalido digite novamente!")
                            time.sleep(1.5)
                            continue
                        if opções4 == "A":
                            Boolean.operador_and(VF, VF2)
                        elif opções4 == "O":
                            Boolean.operador_or(VF, VF2)
                    elif opções4 == "N":
                        VFnot = str(input("Digite os números 0 ou 1: "))
                        if VFnot in ["0", "1"]:
                            Boolean.operador_not(VFnot)
                        else:
                            print("Valor invalido digite novamente!")
                            time.sleep(1.5)
                            continue
                    elif opções4 == "T":
                        Boolean.tabela_verdade(valores)
                    elif opções4 == "V":
                        print("Voltando ao programa...")
                        time.sleep(1.5)
                        break
                    elif opções4 == "S":
                        design_ui.saida()
                    else:
                        print("Valor inválido! Por favor digite o valor correto!")
                        time.sleep(1.5)
                        continue
            elif escolha == "S":
                design_ui.saida()
            else:
                print("Valor inválido! Por favor digite o valor correto!")
                time.sleep(1.5)
                continue
        
    if perm == "Não":
        design_ui.saida()
    else:
        print("Valor invalido, por favor digite o valor correto")
        time.sleep(1.5)
        continue