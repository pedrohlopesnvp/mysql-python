import mysql.connector

# Função para criar a tabela
def criar_tabela():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="agenda")
    
    cursor = conexao.cursor()
    conexao.commit()
    conexao.close()

# Função para adicionar um novo usuário
def adicionar_usuario(nome, email, fone):
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="agenda")
    cursor = conexao.cursor()

    sql = "INSERT INTO pessoas (nome, email, fone) VALUES (%s, %s, %s)"
    val = (nome, email, fone)
    cursor.execute(sql, val)

    conexao.commit()
    conexao.close()

# Função para listar um novo usuário
def listar_usuarios():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="agenda")
    cursor = conexao.cursor()

    sql = "SELECT * FROM pessoas"
    cursor.execute(sql)

    # Recuperar todos os registros
    resultados = cursor.fetchall()
    for row in resultados:
        print(row)

    conexao.close()

# Função para atualizar um novo usuário
def atualizar_usuario(nome, email, fone, id):
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="agenda")
    cursor = conexao.cursor()

    sql = "UPDATE pessoas SET nome=%s, email=%s, fone=%s WHERE id = %s"
    val = (nome, email, fone, id)

    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()

# Função para deletar um novo usuário
def deletar_usuario(id):
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="agenda")
    cursor = conexao.cursor()

    sql = "DELETE FROM pessoas WHERE id = %s"
    val = (id,)

    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()

# Função do menu de escolhas
def menu():
    print("\n1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuários")
    print("4. Deletar usuários")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        fone = input("Digite o fone do usuário: ")
        adicionar_usuario(nome, email, fone)
        print("Usuário adicionado com sucesso!")

    elif escolha == '2':
        print("Usuário cadastrados:")
        listar_usuarios()

    elif escolha == '3':
        id = int(input("Digite o id do usuário que deseja atualizar: "))
        nome = input("Digite o novo nome do usuário: ")
        email = input("Digite o novo email do usuário: ")
        fone = input("Digite o novo fone do usuário: ")
        atualizar_usuario(nome, email, fone, id)
        print("Usuário alterado com sucesso!")

    elif escolha == '4':
        id = int(input("Digite o id do usuário que deseja deletar: "))
        deletar_usuario(id)
        print("Usuário deletado com sucesso!")

    elif escolha == '5':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha um opção válida.")