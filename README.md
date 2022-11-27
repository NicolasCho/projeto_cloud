# Projeto AWS-Terraform: Provisionando infraestrutura

* Nicolas Byung Kwan Cho

---
## Descrição

O projeto visa ser capaz de provisionar uma infraestrutura em nuvem na AWS utilizando o Terraform. Para tanto, disponibiliza-se 
uma interface em linha de comando que auxilia nessa criação.

---
## Instalação

Recomenda-se a criação de um ambiente virtual Python:

```
python -m venv venv
```

Ativar o ambiente e instalar as dependências dentro do diretório *application*:

```
venv\Scripts\activate
pip install -r requirements.txt
```

Para configurar credenciais, criar um arquivo *terraform.tfvars* no diretório *terraform* com:

```
aws_access_key = "{sua access key}"
aws_secret_key = "{sua secret key}"
```

e um arquivo *.env* no diretório *application* com:

```
ACCESS_KEY = "{sua access key}"
SECRET_KEY = "{sua secret key}"
```

Para executar a aplicação:

```
python main.py
```

O comando terraform init é executado no início da aplicação.

---
## Operação

A aplicação inicia na tela do menu principal e dá opção de escolher entre os menus secundários que manuseiam serviços diferentes.
Cada opção pode ser selecionada digitando o número correspondente:

    1. Leva ao menu de instâncias, onde é possível criar, deletar ou listar as instâncias disponíveis
    2. Leva ao menu de usuário, onde é possível criar, deletar ou listar os usuários existentes
    3. Leva ao menu de grupos de segurança, onde é possível criar, deletar, listar ou associar um grupos de segurança a instâncias
    existentes
    4. Sair da aplicação

Cada serviço diferente tem um menu que se comporta da mesma forma.

Uma VPC irá subir automaticamente quando a primeira alteração for realizada, assim como a subnet.

### Instâncias

    1. Criar instâncias
    Permite que o usuário crie uma ou mais instâncias de dois tipos diferentes (t2.nano ou t2.micro). Primeiro será questionado
    quantas instâncias do tipo nano serão criadas e depois quantas do tipo micro. Em seguida será necessário o nome de cada 
    instância. Será gerada a chave de acesso das instâncias em application/instances.

    2. Listar instâncias
    Lista todas as instâncias criadas

    3. Deletar instâncias
    Mostra a lista de todas as instâncias e deleta a instância que corresponde ao indice provido pelo usuário.

    4. Voltar ao menu principal

### Usuários

    1. Criar usuários
    Permite que o usuário crie um ou mais usuários no IAM. Primeiro será questionado quantos usuários serão criados, em seguida o 
    nome de cada usuário. Para cada usuário criado será gerada a chave de acesso daquele usuário em um diretório 
    application/keys/users

    2. Listar usuários
    Lista todos os usuários criados

    3. Deletar usuários
    Mostra a lista de todos os usuários e deleta o usuário que corresponde ao indice provido pelo usuário da aplicação.

    4. Voltar ao menu principal

### Grupos de segurança

    1. Criar grupos de segurança
    Permite que o usuário crie um ou mais grupos de segurança. Para cada grupo de segurnça será necessário informar o nome do
    grupo, uma descrição e se deseja utilizar personalizadas e entrada (ingress) e saída (egress). Caso não seja necessário,
    o grupo será criados com as regras padrões.

    2. Listar grupos de usuário
    Lista todos os grupos de usuário

    3. Deletar grupos de usuário
    Mostra a lista de todas os grupos e deleta o grupo que corresponde ao indice provido pelo usuário. Ao deletar um grupo
    que possui uma associação a determinada instância, a associação também será removida.

    4. Associar grupos com instâncias
    Lista todos os grupos e todas as instâncias e questiona qual grupo e qual instância deverão ser associados. Caso a 
    associação já exista, o processo será cancelado.

    5. Voltar ao menu principal