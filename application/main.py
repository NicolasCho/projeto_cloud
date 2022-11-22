import os
import json
import time
# Transformando dicionario em JSON e escrevendo para arquivo
# NOME DO ARQUIVO = auto.tfvars.json


# json_object = json.dumps(dictionary, indent=4)
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)


#os.system("comando")          -comandos de terminal
#os.chdir('C:\\Users\\Name\\Desktop\\testing')                  -mudar de diretorio

def instancias():
    while True:
        os.system("cls")
        print("MENU INSTÂNCIA")
        print("--------------------------------------------------------------------------------")
        print("Criar, listar ou deletar instâncias\n")
        print("  1 - Criar instância\n  2 - Listar instância\n  3 - Deletar instância\n  4 - Voltar ao menu principal\n")

        servico = check_input(4)

        if servico == 1:
            os.system("cls")
            print("CRIAÇÃO DE INSTÂNCIA")
            print("--------------------------------------------------------------------------------")
            print("Quantas instâncias do tipo t2.nano a serem criadas (limite 5): \n")
            n_instancias_nano = check_input(5, True)

            print('\n\n')

            print("Quantas instâncias do tipo t2.micro a serem criadas (limite 5): \n")
            n_instancias_micro = check_input(5, True)

            print('\n\n')
            print("Confirmar escolha (y/n)? \n")

            continuar = check_yes_no()

            if continuar == "y" and (n_instancias_nano + n_instancias_micro != 0):
                os.system("cls")
                print("NOMES DAS INSTÂNCIAS")
                print("--------------------------------------------------------------------------------")
                for i in range(1, n_instancias_nano+1):
                    print("Nome da instância t2.nano {}:\n".format(i))    
                    nome_nano = input("=> ")
                    #VERIFICAR SE INSTÂNCIA JA EXISTE E SUBIR ERRO CASO POSITIVO<<<<<<<<<<<<<<<<<<<<<<<
                    #SE NÃO, ADICIONAR AO JSON
                
                print('\n\n')
                for i in range(1, n_instancias_micro+1):
                    print("Nome da instância t2.micro {}:\n".format(i))    
                    nome_micro = input("=> ")
                    #VERIFICAR SE INSTÂNCIA JA EXISTE E SUBIR ERRO CASO POSITIVO<<<<<<<<<<<<<<<<<<
                    #SE NÃO, ADICIONAR AO JSON

                os.system("cls")
                print("Subindo instâncias...\n\n")
                # SUBIR INSTÂNCIAS E PAUSAR ATÉ ACABAR<<<<<<<<<<<<<<<<<<<<<<<<<<<
                time.sleep(3)
                print("Operação finalizada.")
                time.sleep(2)

        elif servico == 2:
            os.system("cls")
            print("TODAS AS INSTÂNCIAS")
            print("--------------------------------------------------------------------------------")
            #LISTAR <<<<<<<<<<<<<<<<<<<<<
            
            print("(pressione ENTER para voltar..)")
            voltar = input("=> ")

        elif servico == 3:
            os.system("cls")
            print("DELETAR INSTÂNCIA")
            print("--------------------------------------------------------------------------------")
            #LISTAR<<<<<<<<<<<<<<<<<<<<<<<<

            print("Qual instância gostaria de deletar?\n")
            #APAGAR DO JSON<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        else:
            return


def usuarios():
    while True:
        os.system("cls")
        print("MENU USUÁRIO")
        print("--------------------------------------------------------------------------------")
        print("Criar, listar ou deletar usuários\n")
        print("  1 - Criar usuários\n  2 - Listar usuários\n  3 - Deletar usuários\n  4 - Voltar ao menu principal\n")

        servico = check_input(4)

        if servico == 1:
            os.system("cls")
            print("CRIAÇÃO DE USUÁRIOS")
            print("--------------------------------------------------------------------------------")
            print("Quantos usuários serão criados (limite 5): \n")
            n_usuarios = check_input(5)


            print('\n\n')
            print("Confirmar escolha (y/n)? \n")

            continuar = check_yes_no()

            if continuar == "y" and n_usuarios != 0:
                os.system("cls")
                print("NOMES DOS USUÁRIOS")
                print("--------------------------------------------------------------------------------")
                for i in range(1, n_usuarios+1):
                    print("Nome do usuário {}:\n".format(i))    
                    nome = input("=> ")
                    #VERIFICAR SE USUARIO JA EXISTE E SUBIR ERRO CASO POSITIVO<<<<<<<<<<<<<<<<<<<<<<<
                    #SE NÃO, ADICIONAR AO JSON

                os.system("cls")
                print("Subindo usuários...\n\n")
                # SUBIR USUÁRIOS E PAUSAR ATÉ ACABAR<<<<<<<<<<<<<<<<<<<<<<<<<<<
                time.sleep(3)
                print("Operação finalizada.")
                time.sleep(2)

        elif servico == 2:
            os.system("cls")
            print("TODOS OS USUÁRIOS")
            print("--------------------------------------------------------------------------------")
            #LISTAR <<<<<<<<<<<<<<<<<<<<<
            
            print("(pressione ENTER para voltar..)")
            voltar = input("=> ")

        elif servico == 3:
            os.system("cls")
            print("DELETAR USUÁRIOS")
            print("--------------------------------------------------------------------------------")
            #LISTAR<<<<<<<<<<<<<<<<<<<<<<<<

            print("Qual usuário gostaria de deletar?\n")
        else:
            return

def sg():
    while True:
        os.system("cls")
        print("MENU SECURITY GROUPS")
        print("--------------------------------------------------------------------------------")
        print("Criar, listar ou deletar groupos de segurança\n")
        print("  1 - Criar groupo de segurança\n  2 - Listar groupos de segurança\n  3 - Deletar groupo de segurança\n  4 - Associar grupo com instância\n  5 - Voltar ao menu principal\n")

        servico = check_input(5)

        if servico == 1:
            os.system("cls")
            print("CRIAÇÃO DE GRUPOS DE SEGURANÇA")
            print("--------------------------------------------------------------------------------")
            print("Quantos grupos serão criados (limite 5): \n")
            n_grupos = check_input(5)


            print('\n\n')
            print("Confirmar escolha (y/n)? \n")

            continuar = check_yes_no()

            if continuar == "y" and n_grupos != 0:
                os.system("cls")
                print("NOMES DOS GRUPOS")
                print("--------------------------------------------------------------------------------")
                for i in range(1, n_grupos+1):
                    print("Nome do grupo {}:\n".format(i))    
                    nome = input("=> ")
                    #VERIFICAR SE USUARIO JA EXISTE E SUBIR ERRO CASO POSITIVO<<<<<<<<<<<<<<<<<<<<<<<
                    #SE NÃO, ADICIONAR AO JSON
                    print("Descrição do grupo {}:\n".format(i))    
                    nome = input("=> ")

                    print("Definir regras de ingress {}:\n".format(i))    
                    nome = input("=> ")
                    #BLOCO, PROTOCOLO, PORTAS, ou deixar padrão <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                os.system("cls")
                print("Subindo grupos...\n\n")
                # SUBIR USUÁRIOS E PAUSAR ATÉ ACABAR<<<<<<<<<<<<<<<<<<<<<<<<<<<
                time.sleep(3)
                print("Operação finalizada.")
                time.sleep(2)

        elif servico == 2:
            os.system("cls")
            print("TODOS OS GRUPOS")
            print("--------------------------------------------------------------------------------")
            #LISTAR <<<<<<<<<<<<<<<<<<<<<
            
            print("(pressione ENTER para voltar..)")
            voltar = input("=> ")

        elif servico == 3:
            os.system("cls")
            print("DELETAR GRUPOS")
            print("--------------------------------------------------------------------------------")
            #LISTAR<<<<<<<<<<<<<<<<<<<<<<<<

            print("Quais grupos gostaria de deletar?\n")

        elif servico == 4:
            os.system("cls")
            print("ASSOCIAR GRUPOS")
            print("--------------------------------------------------------------------------------")
            #LISTAR<<<<<<<<<<<<<<<<<<<<<<<<

            print("Qual grupo?\n")
            id_grupo = input("=> ")

            print("Qual instância?\n")
            id_instancia = input("=> ")

        else:
            return



def main():
    while True:
        os.system("cls")
        print("MENU PRINCIPAL")
        print("--------------------------------------------------------------------------------")
        print("Digite o número correspondente ao serviço desejado:\n")
        print("  1 - Instâncias\n  2 - Usuário IAM\n  3 - Grupo de segurança\n  4 - Sair\n")
        
        servico = check_input(4)
        
        if servico == 1:
            instancias()
        elif servico == 2:
            usuarios()
        elif servico == 3:
            sg()
        else:
            return

def check_yes_no():
    answer = input("=> ")
    while answer != 'y' and answer != "n":        
        print("Entrada inválida")
        answer = input("=> ")
    return answer


def check_input(n_options, include_zero = False):
    floor = 0
    ceiling = n_options
    if include_zero:
        floor = -1
        ceiling = n_options - 1
    
    servico = floor 
    while servico == floor:
        user_input = input("=> ")
        try:
            servico = int(user_input)
            if servico <= floor or servico > ceiling:
                servico = floor
                print("Entrada inválida")

        except:
            print("Entrada inválida")
    
    return servico

if __name__ == "__main__":
    main()