import os
import json
import time
import ipaddress
from dotenv import load_dotenv  
import boto3

load_dotenv()   
ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")


session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='us-east-1'
)

ec2 = session.resource('ec2')


#variáveis a serem passadas ao terraform 
var_dict={
    "users": [],
    "instance_conf" : [],
    "sec_groups" : [],
    "association" : []
}


#os.chdir("../terraform")
if os.path.isfile("auto.tfvars.json"):
    f  = open("auto.tfvars.json")
    var_dict = json.load(f)
else:
    with open('auto.tfvars.json', 'w') as fp:
        json.dump(var_dict, fp, indent=4)



def instancias():
    while True:
        os.system("cls")
        print("MENU INSTÂNCIA")
        print("--------------------------------------------------------------------------------")
        print("Criar, listar ou deletar instâncias\n")
        print("  1 - Criar instância\n  2 - Listar instância\n  3 - Deletar instância\n  4 - Voltar ao menu principal\n")

        for instance in ec2.instances.all():
            print(
                "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\nENI: {6}\n".format(
                instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state,
                instance.network_interfaces[0].id
                )
            )

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

                    instance = {"instance_name": nome_nano, "instance_type": "t2.nano"}
                    var_dict["instance_conf"].append(instance)
                    
                print('\n\n')
                for i in range(1, n_instancias_micro+1):
                    print("Nome da instância t2.micro {}:\n".format(i))    
                    nome_micro = input("=> ")
                    
                    instance = {"instance_name": nome_micro, "instance_type": "t2.micro"}
                    var_dict["instance_conf"].append(instance)
                
                with open('auto.tfvars.json', 'w') as fp:
                    json.dump(var_dict, fp, indent=4)

                os.system("cls")
                print("Subindo instâncias...\n\n")
                print("--------------------------------------------------------------------------------")
                #os.system("terraform plan -var-file='secrets.tfvars'")
                #os.system("terraform apply -var-file='secrets.tfvars' -auto-approve")
                print("--------------------------------------------------------------------------------")
                print("Operação finalizada.")
                time.sleep(2)

        elif servico == 2:
            os.system("cls")
            print("TODAS AS INSTÂNCIAS")
            print("--------------------------------------------------------------------------------")
            i = 0
            for instancia in (var_dict["instance_conf"]):
                print("{} -> name:{} , type: {}".format(i, instancia["instance_name"], instancia["instance_type"]))
                i += 1
                print('\n')

            i-=1
            print("(pressione ENTER para voltar..)")
            voltar = input("=> ")

        elif servico == 3:
            os.system("cls")
            print("DELETAR INSTÂNCIA")
            print("--------------------------------------------------------------------------------")
            i = 0
            for instancia in (var_dict["instance_conf"]):
                print("{} -> name:{} , type: {}".format(i, instancia["instance_name"], instancia["instance_type"]))
                i += 1
                print('\n')

            if i == 0:
                print("(pressione ENTER para voltar..)")
                voltar = input("=> ")
            else:
                i-=1
                print("Qual instância gostaria de deletar?\n")

                delete_instance = check_input(i, include_zero=True)

                print("Confirmar escolha (y/n)? \n")
                continuar = check_yes_no()

                if continuar == 'y':
                    var_dict['instance_conf'].pop(delete_instance)

                    with open('auto.tfvars.json', 'w') as fp:
                        json.dump(var_dict, fp, indent=4)

                    os.system("cls")
                    print("Deletando instância...\n\n")
                    print("--------------------------------------------------------------------------------")
                    #os.system("terraform plan -var-file='secrets.tfvars'")
                    #os.system("terraform apply -var-file='secrets.tfvars' -auto-approve")
                    print("--------------------------------------------------------------------------------")
                    print("Operação finalizada.")
                    time.sleep(2)

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
                    conflict = True
                    
                    while conflict:
                        conflict = False
                        nome = input("=> ")
                        for user in var_dict['users']:
                            if user["name"] == nome:
                                conflict = True
                                print("Usuário já existe\n")

                    user = {"name": nome}
                    var_dict["users"].append(user)

                with open('auto.tfvars.json', 'w') as fp:
                    json.dump(var_dict, fp, indent=4)
                    
                os.system("cls")
                print("Subindo usuários...\n\n")
                print("--------------------------------------------------------------------------------")
                #os.system("terraform plan -var-file='secrets.tfvars'")
                #os.system("terraform apply -var-file='secrets.tfvars' -auto-approve")
                print("--------------------------------------------------------------------------------")
                print("Operação finalizada.")
                time.sleep(2)

        elif servico == 2:
            os.system("cls")
            print("TODOS OS USUÁRIOS")
            print("--------------------------------------------------------------------------------")
            i = 0
            for user in (var_dict["users"]):
                print("{} -> name:{}".format(i, user["name"]))
                i += 1
                print('\n')

            i-=1
            
            print("(pressione ENTER para voltar..)")
            voltar = input("=> ")

        elif servico == 3:
            os.system("cls")
            print("DELETAR USUÁRIOS")
            print("--------------------------------------------------------------------------------")
            i = 0
            for user in (var_dict["users"]):
                print("{} -> name:{}".format(i, user["name"]))
                i += 1
                print('\n')
            
            if i == 0:
                print("(pressione ENTER para voltar..)")
                voltar = input("=> ")
            else:
                i-=1
                print("Qual usuário gostaria de deletar?\n")

                delete_user = check_input(i, include_zero=True)

                print("Confirmar escolha (y/n)? \n")
                continuar = check_yes_no()

                if continuar == 'y':
                    var_dict['users'].pop(delete_user)

                    with open('auto.tfvars.json', 'w') as fp:
                        json.dump(var_dict, fp, indent=4)

                    os.system("cls")
                    print("Deletando usuário...\n\n")
                    print("--------------------------------------------------------------------------------")
                    #os.system("terraform plan -var-file='secrets.tfvars'")
                    #os.system("terraform apply -var-file='secrets.tfvars' -auto-approve")
                    print("--------------------------------------------------------------------------------")
                    print("Operação finalizada.")
                    time.sleep(2)

        else:
            return

def sg():
    while True:
        os.system("cls")
        print("MENU GRUPOS DE SEGURANÇA")
        print("--------------------------------------------------------------------------------")
        print("Criar, listar, deletar ou associar groupos de segurança\n")
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
                for i in range(1, n_grupos+1):
                    os.system("cls")
                    print("Definição dos grupos")
                    print("--------------------------------------------------------------------------------")
                    print("Nome do grupo {}:\n".format(i))    
                    conflict = True
                    
                    while conflict:
                        conflict = False
                        nome = input("=> ")
                        for sec_group in var_dict['sec_groups']:
                            if sec_group["name"] == nome:
                                conflict = True
                                print("Grupo de já existe\n")

                    print("Descrição do grupo {}:\n".format(i))    
                    descricao = input("=> ")

                    print("Definir regras de entrada (ingress) para {}? (y/n) ['n' para definições padrões]\n".format(i))   
                    regras_ingress = check_yes_no()
                    if regras_ingress == "y":
                        print("Porta de início do intervalo: \n")   
                        print("(porta limite = 1023)\n")   
                        porta_inicio = check_range(0, 1023)

                        print("Porta final do intervalo: \n")
                        print("(porta limite = 1023)\n")   
                        porta_final = check_range(porta_inicio, 1023)

                        protocolo = "tcp"

                        print("Definir bloco de domínio e prefixo:")
                        print("exemplo: primeiro input => 0.0.0.0,   segundo input => 24")
                        print("resultado: 0.0.0.0/24)\n")   
                        ip = check_ip()

                        print("\nPrefixo: (0 a 32)")
                        prefix = check_input(32, include_zero=True)
                        cidr_list = []
                        cidr_block = ip + "/" + str(prefix)
                        cidr_list.append(cidr_block)

                        ingress = [{"from_port":porta_inicio, "to_port": porta_final, "protocol": protocolo, "cidr_blocks": cidr_list}]
                    else:
                        ingress = [{"from_port":443, "to_port": 443, "protocol": "tcp", "cidr_blocks": ["10.0.0.0/16"]}]

                    print("Definir regras de saída (egress) para {}? (y/n) ['n' para definições padrões]\n".format(i))   
                    regras_egress = check_yes_no() 
                    if regras_egress == "y":
                        print("Porta de início do intervalo: \n")   
                        print("(porta limite = 1023)\n")   
                        porta_inicio = check_range(0, 1023)

                        print("Porta final do intervalo: \n")
                        print("(porta limite = 1023)\n")   
                        porta_final = check_range(porta_inicio, 1023)

                        protocolo = "tcp"

                        print("Definir bloco de domínio e prefixo:")
                        print("exemplo: primeiro input => 0.0.0.0,   segundo input => 24")
                        print("resultado: 0.0.0.0/24)\n")   
                        ip = check_ip()

                        print("\nPrefixo: (0 a 32)")
                        prefix = check_input(32, include_zero=True)
                        cidr_list = []
                        cidr_block = ip + "/" + str(prefix)
                        cidr_list.append(cidr_block)

                        egress = [{"from_port":porta_inicio, "to_port": porta_final, "protocol": protocolo, "cidr_blocks": cidr_list}]
                    else:
                        egress = [{"from_port":443, "to_port": 443, "protocol": "tcp", "cidr_blocks": ["0.0.0.0/0"]}]

                    group = {"name": nome, "description": descricao, "ingress": ingress, "egress": egress}
                    var_dict["sec_groups"].append(group)

                with open('auto.tfvars.json', 'w') as fp:
                    json.dump(var_dict, fp, indent=4)

                os.system("cls")
                print("Criando grupos...\n\n")
                print("--------------------------------------------------------------------------------")
                #os.system("terraform plan -var-file='secrets.tfvars'")
                #os.system("terraform apply -var-file='secrets.tfvars' -auto-approve")
                print("--------------------------------------------------------------------------------")
                print("Operação finalizada.")
                time.sleep(2)

        elif servico == 2:
            os.system("cls")
            print("TODOS OS GRUPOS DE SEGURANÇA")
            print("--------------------------------------------------------------------------------")
            i = 0
            for grupo in (var_dict["sec_groups"]):
                print("{} -> name:{}".format(i, grupo["name"]))
                print("{} -> descrição:{}".format(i, grupo["descritpion"]))
                print("{} -> ingress:{}".format(i, grupo["ingress"]))
                print("{} -> egress:{}".format(i, grupo["egress"]))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('\n')
                i += 1

            i-=1
            
            print("(pressione ENTER para voltar..)")
            voltar = input("=> ")

        elif servico == 3:
            os.system("cls")
            print("DELETAR GRUPOS DE SEGURANÇA")
            print("--------------------------------------------------------------------------------")
            i = 0
            for grupo in (var_dict["sec_groups"]):
                print("{} -> name:{}".format(i, grupo["name"]))
                i += 1
                print('\n')
            
            if i == 0:
                print("(pressione ENTER para voltar..)")
                voltar = input("=> ")
            else:
                i-=1
                print("Qual grupo gostaria de deletar?\n")

                delete_group = check_input(i, include_zero=True)

                print("Confirmar escolha (y/n)? \n")
                continuar = check_yes_no()

                if continuar == 'y':
                    var_dict['sec_groups'].pop(delete_group)

                    with open('auto.tfvars.json', 'w') as fp:
                        json.dump(var_dict, fp, indent=4)

                    os.system("cls")
                    print("Deletando grupo...\n\n")
                    print("--------------------------------------------------------------------------------")
                    #os.system("terraform plan -var-file='secrets.tfvars'")
                    #os.system("terraform apply -var-file='secrets.tfvars' -auto-approve")
                    print("--------------------------------------------------------------------------------")
                    print("Operação finalizada.")
                    time.sleep(2)

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

# --------------------------------------------------------------------------------------------------------- #

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

# --------------------------------------------------------------------------------------------------------- #
def check_ip():
    while True:
        try:
            ip = str(ipaddress.ip_address(input('=> ')))
            break
        except ValueError:
            continue
    return ip


def check_yes_no():
    answer = input("=> ")
    while answer != 'y' and answer != "n":        
        print("Entrada inválida")
        answer = input("=> ")
    return answer

def check_range(start, end):
    valor = -1
    while valor < 0:
        valor = input("=> ")
        try:
            valor = int(valor)
            if valor < start  or valor > end:
                valor = -1
                print("Entrada inválida")

        except:
            valor = -1
            print("Entrada inválida")
    
    return valor

def check_input(n_options, include_zero = False, exclude_limit = False):
    floor = 0
    ceiling = n_options
    if include_zero:
        floor = -1
    if exclude_limit:
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