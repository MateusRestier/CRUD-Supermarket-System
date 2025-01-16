import os

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Funcionario:
    def __init__(self, nome, cargo, senha):
        self.nome = nome
        self.cargo = cargo
        self.senha = senha

class Supermercado:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.funcionarios = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.salvar_produtos()

    def remover_produto(self, nome_produto):
        self.produtos = [produto for produto in self.produtos if produto.nome != nome_produto]
        self.salvar_produtos()

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.salvar_clientes()

    def remover_cliente(self, nome_cliente):
        self.clientes = [cliente for cliente in self.clientes if cliente.nome != nome_cliente]
        self.salvar_clientes()

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        self.salvar_funcionarios()

    def remover_funcionario(self, nome_funcionario):
        self.funcionarios = [funcionario for funcionario in self.funcionarios if funcionario.nome != nome_funcionario]
        self.salvar_funcionarios()

    def atualizar_cargo_funcionario(self, nome_funcionario, novo_cargo):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome_funcionario:
                funcionario.cargo = novo_cargo
                self.salvar_funcionarios()
                break

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self.produtos:
                print(f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes:
                print(f"Nome: {cliente.nome}, Email: {cliente.email}")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            for funcionario in self.funcionarios:
                print(f"Nome: {funcionario.nome}, Cargo: {funcionario.cargo}")

    def autenticar_cliente(self, email, senha):
        email = email.strip()
        senha = senha.strip()
        for cliente in self.clientes:
            if cliente.email == email and cliente.senha == senha:
                return cliente
        return None

    def autenticar_funcionario(self, nome, senha):
        nome = nome.strip()
        senha = senha.strip()
        for funcionario in self.funcionarios:
            if funcionario.nome == nome and funcionario.senha == senha:
                return funcionario
        return None

    def carregar_dados(self):
        self.carregar_produtos()
        self.carregar_clientes()
        self.carregar_funcionarios()

    def carregar_produtos(self):
        try:
            filepath = os.path.join(os.path.dirname(__file__), 'produtos.txt')
            with open(filepath, 'r') as file:
                for line in file:
                    nome, preco, quantidade = [item.strip() for item in line.strip().split(',')]
                    self.adicionar_produto(Produto(nome, float(preco), int(quantidade)))
        except FileNotFoundError:
            print("Arquivo produtos.txt não encontrado.")

    def carregar_clientes(self):
        try:
            filepath = os.path.join(os.path.dirname(__file__), 'clientes.txt')
            with open(filepath, 'r') as file:
                for line in file:
                    nome, email, senha = [item.strip() for item in line.strip().split(',')]
                    self.adicionar_cliente(Cliente(nome, email, senha))
        except FileNotFoundError:
            print("Arquivo clientes.txt não encontrado.")

    def carregar_funcionarios(self):
        try:
            filepath = os.path.join(os.path.dirname(__file__), 'funcionarios.txt')
            with open(filepath, 'r') as file:
                for line in file:
                    nome, cargo, senha = [item.strip() for item in line.strip().split(',')]
                    self.adicionar_funcionario(Funcionario(nome, cargo, senha))
        except FileNotFoundError:
            print("Arquivo funcionarios.txt não encontrado.")

    def salvar_produtos(self):
        filepath = os.path.join(os.path.dirname(__file__), 'produtos.txt')
        with open(filepath, 'w') as file:
            for produto in self.produtos:
                file.write(f"{produto.nome},{produto.preco},{produto.quantidade}\n")

    def salvar_clientes(self):
        filepath = os.path.join(os.path.dirname(__file__), 'clientes.txt')
        with open(filepath, 'w') as file:
            for cliente in self.clientes:
                file.write(f"{cliente.nome},{cliente.email},{cliente.senha}\n")

    def salvar_funcionarios(self):
        filepath = os.path.join(os.path.dirname(__file__), 'funcionarios.txt')
        with open(filepath, 'w') as file:
            for funcionario in self.funcionarios:
                file.write(f"{funcionario.nome},{funcionario.cargo},{funcionario.senha}\n")

def menu_produtos(supermercado):
    while True:
        print("\nMenu de Produtos")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Voltar ao Menu Principal")
        
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            nome = input("Digite o nome do produto: ")
            try:
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                supermercado.adicionar_produto(Produto(nome, preco, quantidade))
                print(f"Produto {nome} adicionado.")
            except ValueError:
                print("Entrada inválida. Preço deve ser um número e quantidade deve ser um inteiro.")
        
        elif escolha == '2':
            nome = input("Digite o nome do produto a ser removido: ")
            supermercado.remover_produto(nome)
            print(f"Produto {nome} removido.")
        
        elif escolha == '3':
            supermercado.listar_produtos()
        
        elif escolha == '4':
            break
        
        else:
            print("Escolha inválida. Por favor, tente novamente.")

def menu_clientes(supermercado):
    while True:
        print("\nMenu de Clientes")
        print("1. Listar Produtos")
        print("2. Voltar ao Menu Principal")
        
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            supermercado.listar_produtos()
        
        elif escolha == '2':
            break
        
        else:
            print("Escolha inválida. Por favor, tente novamente.")

def menu_funcionarios(supermercado):
    while True:
        print("\nMenu de Funcionários")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Adicionar Cliente")
        print("5. Remover Cliente")
        print("6. Listar Clientes")
        print("7. Adicionar Funcionário")
        print("8. Remover Funcionário")
        print("9. Listar Funcionários")
        print("10. Atualizar Cargo de Funcionário")
        print("11. Voltar ao Menu Principal")
        
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            nome = input("Digite o nome do produto: ")
            try:
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                supermercado.adicionar_produto(Produto(nome, preco, quantidade))
                print(f"Produto {nome} adicionado.")
            except ValueError:
                print("Entrada inválida. Preço deve ser um número e quantidade deve ser um inteiro.")
        
        elif escolha == '2':
            nome = input("Digite o nome do produto a ser removido: ")
            supermercado.remover_produto(nome)
            print(f"Produto {nome} removido.")
        
        elif escolha == '3':
            supermercado.listar_produtos()
        
        elif escolha == '4':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            senha = input("Digite a senha do cliente: ")
            supermercado.adicionar_cliente(Cliente(nome, email, senha))
            print(f"Cliente {nome} adicionado.")
        
        elif escolha == '5':
            nome = input("Digite o nome do cliente a ser removido: ")
            supermercado.remover_cliente(nome)
            print(f"Cliente {nome} removido.")
        
        elif escolha == '6':
            supermercado.listar_clientes()
        
        elif escolha == '7':
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            senha = input("Digite a senha do funcionário: ")
            supermercado.adicionar_funcionario(Funcionario(nome, cargo, senha))
            print(f"Funcionário {nome} adicionado.")
        
        elif escolha == '8':
            nome = input("Digite o nome do funcionário a ser removido: ")
            supermercado.remover_funcionario(nome)
            print(f"Funcionário {nome} removido.")
        
        elif escolha == '9':
            supermercado.listar_funcionarios()
        
        elif escolha == '10':
            nome = input("Digite o nome do funcionário: ")
            novo_cargo = input("Digite o novo cargo: ")
            supermercado.atualizar_cargo_funcionario(nome, novo_cargo)
            print(f"Cargo do funcionário {nome} atualizado para {novo_cargo}.")
        
        elif escolha == '11':
            break
        
        else:
            print("Escolha inválida. Por favor, tente novamente.")

def menu_principal(supermercado):
    while True:
        print("\nSistema de Gestão de Supermercado")
        print("1. Login como Cliente")
        print("2. Login como Funcionário")
        print("3. Sair")
        
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            cliente = supermercado.autenticar_cliente(email, senha)
            if cliente:
                print(f"Bem-vindo, {cliente.nome}!")
                menu_clientes(supermercado)
            else:
                print("Email ou senha inválidos.")
        
        elif escolha == '2':
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            funcionario = supermercado.autenticar_funcionario(nome, senha)
            if funcionario:
                print(f"Bem-vindo, {funcionario.nome}!")
                menu_funcionarios(supermercado)
            else:
                print("Nome ou senha inválidos.")
        
        elif escolha == '3':
            break
        
        else:
            print("Escolha inválida. Por favor, tente novamente.")

def main():
    supermercado = Supermercado()
    supermercado.carregar_dados()
    menu_principal(supermercado)

if __name__ == "__main__":
    main()
