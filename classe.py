import os
import random
import string


def limpar():
    os.system("cls")


def pausar():
    os.system("pause")


class Loja:
    def __init__(self, nome, endereço, cnpj):
        self.nome = nome
        self.endereço = endereço
        self.cnpj = cnpj


class Produtos:
    def __init__(self):
        self.produtos = []
        self.descs = []
        self.preco = []
        self.listacarrinho = []
        self.listacarrinhopreco = []
        self.descs = []
        self.listacarrinho = []
        self.historicoNome = []
        self.historicoProduto = []
        self.historicoValor = []
        self.somacarrinho = []
        self.historicoNpedido = []

    def AddProduto(self, nome, desc, valor):
        self.produtos.append(nome)
        self.preco.append(valor)
        self.descs.append(desc)

    def ListarProdutos(self):
        i = 0
        for i in range(len(self.produtos)):
            print(f" Produto: {self.produtos.index(self.produtos[i])}  |  Nome: {self.produtos[i]}  |  Desc: {self.descs[i]}  |  Valor: {self.preco[i]}")
            i += 1

    def RemProdutos(self, produto):
        del self.produtos[produto]
        del self.preco[produto]
        del self.descs[produto]

    def AddCarrinho(self, produto):
        self.listacarrinho.append(self.produtos[produto])
        self.listacarrinhopreco.append(self.preco[produto])
        print("Produto adicionado com sucesso")

    def ListCarrinho(self):
        i = 0
        for i in range(len(self.listacarrinho)):
            print(f" Produto: {self.listacarrinho.index(self.listacarrinho[i])}  |  Nome: {self.listacarrinho[i]}   |  Valor: {self.listacarrinhopreco[i]}")
            i += 1

    def RemCarrinho(self, vetor):
        del self.listacarrinho[vetor]
        del self.listacarrinhopreco[vetor]
        if vetor > len(self.listacarrinho):
            print("Não existe esse produto")
        else:
            print("Produto removido com sucesso")

    def SomaCarrinho(self):
        self.somacarrinho = sum(self.listacarrinhopreco)
        print(f"Valor total do carrinho: {self.somacarrinho}")

    def HistoricoCompra(self, Npedido):
        self.historicoProduto.append(self.listacarrinho)
        self.historicoNpedido.append(Npedido)
        i = 0
        for i in range(len(self.listacarrinho)):
            self.historicoValor.append(self.listacarrinhopreco[i])
            i += 1

    def TotalHistorico(self):
        print(f" O valor total vendido em sua loja foi de: {sum(self.historicoValor)}")

    def ListarHistorico(self):
        i = 0
        for i in range(len(self.historicoProduto)):
            print(f" Numero do pedido: {self.historicoNpedido[i]}  |  Produtos: {self.listacarrinho}  |  Valor: {self.listacarrinhopreco}")
            i += 1


class Adm:
    def cadAdm(self, nome, senha):
        self.adms = []
        self.adms.append(nome)
        self.admsSenha = []
        self.admsSenha.append(senha)

    def verifyAdm(self, nome, senha):
        if nome in self.adms and senha in self.admsSenha:
            return True
        else:
            return False

    def listarAdm(self):
        i = 0
        for i in range(len(self.adms)):
            print(f" Index: {i}  |  Nome: {self.adms[i]}  |  Senha: {self.admsSenha[i]}")
            i += 1

    def delAdm(self, adm):
        if adm == 0:
            print("Não é possivel remover o adm root")
        else:
            del self.admsSenha[adm]
            del self.adms[adm]
        if adm >= len(self.adms):
            print("Não existe esse adm")



class Cliente(Produtos):
    def __init__(self):
        self.clientes = []
        self.clienteSenha = []

    def add_Cliente(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.clientes.append(nome)
        self.clienteSenha.append(senha)

    def listar_Clientes(self):
        i = 0
        for i in range(len(self.clientes)):
            print(f"Index: {i}  |  Nome: {self.clientes[i]}  |  Senha: {self.clienteSenha[i]}")
            i += 1

    def logar_Cliente(self, nome, senha):
        if nome in self.clientes and senha in self.clienteSenha:
            return True
        else:
            return False

    def DelCliente(self, cliente):
        del self.clientes[cliente]
        del self.clienteSenha[cliente]
        if cliente >= len(self.clientes):
            print("Não existe esse cliente")
        else:
            print("Cliente removido com sucesso")