from classe import *

produtos = Produtos()
adm = Adm()
cliente = Cliente()
loja = Loja("LOJA DO CACIQUE", "Ácre", "11091945")


def gerar_parte_aleatoria(length):
    caracteres = string.ascii_uppercase + string.digits
    return "".join(random.choice(caracteres) for _ in range(length))


def gerar_numero_pedido():
    numero_pedido = f"#{gerar_parte_aleatoria(2)}{gerar_parte_aleatoria(2)}{gerar_parte_aleatoria(2)}{gerar_parte_aleatoria(2)}{gerar_parte_aleatoria(3)}"
    return numero_pedido


def voltar():
    limpar()
    print("Voltando...")
    pausar()


# --|Função dos menus|--////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def menucliente():
    limpar()
    print(f"---| BEM VINDO A {loja.nome} |---")
    print(" [1] - Ver Produtos")
    print(" [2] - Adicionar ao Carrinho")
    print(" [3] - Ver Carrinho")
    print(" [4] - Excluir do Carrinho")
    print(" [5] - Checkout")
    print(" [6] - Pagar")
    print(" [7] - Voltar")


def menuadm():
    limpar()
    print("---| OPÇÕES DE GERENCIAMENTO ADM |---")
    print(" [1] - Cadastrar Cliente")
    print(" [2] - Cadastrar Adm")
    print(" [3] - Adicionar Produto")
    print(" [4] - Remove Produto")
    print(" [5] - Remover Cliente")
    print(" [6] - Remover Adm")
    print(" [7] - Listar Produto")
    print(" [8] - Listar Clientes")
    print(" [9] - Listar Adms")
    print(" [10] - Historico de Compras")
    print(" [11] - Historico Geral")
    print(" [12] - Voltar")


def menuprincipal():
    limpar()
    print(f"---| BEM VINDO A {loja.nome} |---")
    print(" [1] - Login")
    print(" [2] - Sair")
    print("Digite o numero equivalente a opção que deseja")


def addProdutos():
    limpar()
    print("Adicionando Produtos")
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    produtos.AddProduto(nome, valor)
    print("Produto adicionado com sucesso")
    pausar()
    limpar()


def verProdutos():
    limpar()
    print("Produtos")
    produtos.ListarProdutos()
    pausar()


def removerProdutos():
    limpar()
    print("Removendo Produtos")
    print("Produtos")
    produtos.ListarProdutos()
    produtoRem = int(input("Digite o numero do produto que deseja remover: "))
    produtos.RemProdutos(produtoRem)
    print("Produto removido com sucesso")
    pausar()


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def main():
    adm.cadAdm("root", "root")
    while True:
        try:
            limpar()
            menuprincipal()
            menu = int(input(">> "))

            match menu:
                case 1:
                    limpar()
                    print("--| Login |--")
                    nome = input("Nome: ")
                    senha = input("Senha: ")
                    if adm.verifyAdm(nome, senha) == True:
                        while True:
                            menuadm()
                            opcao = int(input(">> "))
                            match opcao:
                                case 1:
                                    limpar()
                                    print("--| Cadastrar Cliente |--")
                                    nome = input("Nome: ")
                                    senha = input("Senha: ")
                                    cliente.add_Cliente(nome, senha)
                                case 2:
                                    limpar()
                                    print("--| Cadastrar Adm |--")
                                    nome = input("Nome: ")
                                    senha = input("Senha: ")
                                    adm.cadAdm(nome, senha)
                                    print("Adm cadastrado com sucesso")
                                case 3:
                                    limpar()
                                    print("--| Adicionar Produto |--")
                                    nome = input("Nome do produto: ")
                                    valor = float(input("Valor do produto: "))
                                    descricao = input("Descrição do produto: ")
                                    produtos.AddProduto(nome, descricao, valor)
                                    print("Produto adicionado com sucesso")
                                    pausar()

                                case 4:
                                    limpar()
                                    print("--| Remover Produto |--")
                                    produtos.ListarProdutos()
                                    produtoRem = int(input("Digite o numero do produto que deseja remover: "))
                                    produtos.RemProdutos(produtoRem)
                                case 5:
                                    limpar()
                                    print("--| Remover Cliente |--")
                                    cliente.listar_Clientes()
                                    clienterem = int((input("Digite o numero do cliente que deseja remover: ")))
                                    cliente.DelCliente(clienterem)

                                case 6:
                                    limpar()
                                    print("--| Remover Adm |--")
                                    adm.listarAdm
                                    admrem = int(input("Digite o numero do adm que deseja remover: "))
                                    adm.delAdm(admrem)
                                    print("Adm removido com sucesso")
                                    pausar()
                                case 7:
                                    limpar()
                                    print("--| Listar Produtos |--")
                                    produtos.ListarProdutos()
                                    pausar()
                                case 8:
                                    limpar()
                                    print("--| Listar Clientes |--")
                                    cliente.listar_Clientes()
                                    pausar()
                                case 9:
                                    limpar()
                                    print("--| Listar Adms |--")
                                    adm.listarAdm()
                                    pausar()

                                case 10:
                                    limpar()
                                    print("--| Historico De Compras |--")
                                    produtos.ListarHistorico()
                                    pausar()
                                case 11:
                                    limpar()
                                    print("--| Historico Geral |--")
                                    produtos.TotalHistorico()
                                    pausar()
                                case 12:
                                    voltar()
                                    break
                    elif cliente.logar_Cliente(nome, senha) == True:
                        while True:
                            menucliente()
                            opcCliente = int(input(">> "))
                            match opcCliente:
                                case 1:
                                    limpar()
                                    print("--| Produtos |--")
                                    produtos.ListarProdutos()
                                    pausar()
                                case 2:
                                    limpar()
                                    print("--| Adicionar Produtos ao Carrinho |--")
                                    produtos.ListarProdutos()
                                    produto = int(input("Digite o numero do produto que deseja adicionar ao carrinho: "))
                                    produtos.AddCarrinho(produto)
                                    pausar()
                                case 3:
                                    limpar()
                                    print("--| Ver Carrinho |--")
                                    produtos.ListCarrinho()
                                    pausar()
                                case 4:
                                    limpar()
                                    print("--| Excluir do Carrinho |--")
                                    produtos.ListCarrinho()
                                    produto = int(input("Digite o numero do produto que deseja remover do carrinho: "))
                                    produtos.RemCarrinho(produto)
                                    pausar()
                                case 5:
                                    limpar()
                                    print("--| Checkout |--")
                                    produtos.ListCarrinho()
                                    produtos.SomaCarrinho()
                                    pausar()
                                case 6:
                                    limpar()
                                    print("--| Pagar |--")
                                    print("Pagamento efetuado com sucesso")
                                    numero_pedido = gerar_numero_pedido()
                                    print(f"Numero do pedido: {numero_pedido}")
                                    produtos.HistoricoCompra(numero_pedido)
                                    pausar()
                                case 7:
                                    voltar()
                                    break

                    else:
                        print("Nome ou senha incorretos")
                        pausar()
                case 2:
                    limpar()
                    print("Saindo....")
                    pausar()
                    exit()
        except Exception as erro:  
            print(f'Opa! Houve um erro')
            pausar() 
