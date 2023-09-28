# MarketPlace

<table>
<tr>
    <td align="center">
        <a href="https://open.vscode.dev/diegorkkj/marketplace">
        <img src="https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg" alt="Open in Visual Studio Code">
        </a>
    </td>
    <td align="center">
        <img src="https://img.shields.io/static/v1?label=STATUS&message=%20Finalizado&color=blue&style=for-the-badge&logo=REACT"/>
    </td>
</tr>
</table>

## Especificações do Software de Compra e Venda em Python Orientado a Objeto

O software foi projetado com o objetivo de oferecer um ambiente de E-Commerce eletrônico onde clientes podem se cadastrar, fazer login, visualizar produtos, adicionar itens ao carrinho e realizar compras. Além disso, há funcionalidades específicas para administradores, como gerenciar clientes, produtos e perfis de administrador.
Ele devera ser feito com base nos fundamentos de `associação, agregação e composição` em Python Orientado a Objeto

## Tela Inicial

- **Login**: Os clientes e os Adms podem efetuar login utilizando as informações fornecidas durante o cadastro. Isso dará acesso ao seu perfil e às funcionalidades relacionadas.

- **Sair**: Essa função permite que o usuário saia do software, encerrando a sessão e fechando o programa.

_Observação_: O perfil do administrador já estará previamente definido no sistema, permitindo o acesso com as informações de login cadastradas como root, o cliente devera fazer seu cadastro com a ajuda de um dos adiministradores presentes na loja.

## Tela de Login do Cliente

- **Ver Produto**: Ao selecionar esta opção, o cliente terá acesso a uma lista de todos os produtos disponíveis na loja. Isso permite que eles visualizem os itens disponíveis para compra.

- **Adicionar ao Carrinho**: Esta função permite ao cliente adicionar produtos selecionados ao seu carrinho de compras. Os produtos escolhidos serão armazenados temporariamente no carrinho.

- **Ver Carrinho**: Ao optar por essa funcionalidade, o cliente poderá visualizar todos os produtos que foram adicionados ao seu carrinho durante a sessão de compra.

- **Excluir do Carrinho**: Esta função permite ao cliente remover produtos presentes no carrinho.

- **Checkout**: Esta opção mostra ao cliente seus produtos que foram adicionados ao carrinho e a soma do valor destes produtos durante a sessão da compra.

- **Pagar**: Ao selecionar esta opção, o cliente poderá finalizar sua compra, efetuando o pagamento dos produtos presentes no carrinho. Após a conclusão da compra, os produtos serão removidos do carrinho e adicionados ao histórico de compras do cliente.

- **Voltar**: Esta opção permite ao cliente retornar à tela inicial, efetuando o logout da sua sessão atual.

## Tela de Login do Administrador

- **Cadastrar Cliente**: Permite que o administrador faça o cadastro de novos clientes da loja, coletando informações necessárias para a criação de contas de cliente.

- **Cadastrar Administrador**: Esta função habilita o administrador a criar novos perfis de administrador para gerenciar as operações da loja.

- **Cadastrar Produtos**: O administrador pode utilizar essa opção para adicionar novos produtos ao catálogo da loja, especificando detalhes como nome, preço, descrição, etc.

- **Excluir Produtos**: Essa função possibilita a exclusão de produtos previamente cadastrados na loja.

- **Excluir Clientes**: O administrador pode remover perfis de clientes específicos, se necessário.

- **Excluir Administradores**: O administrador pode remover perfis de administradores específicos, se necessário.

- **Listar Produtos**: Exibe uma lista de todos os produtos atualmente disponíveis na loja.

- **Listar Clientes**: Mostra uma lista de todos os clientes registrados no sistema da loja.

- **Listar Administradores**: Exibe uma lista de todos os perfis de administradores cadastrados na loja.

- **Listar Histórico de Compras**: Esta opção permite que os administradores visualizem o histórico de compras de todos os clientes da loja.

- **Lista o Histórico de Comparas Geral**: Esta Opção permite que os administradores visualizem o histórico de compras geral da loja.

- **Voltar**: Permite ao administrador retornar à tela inicial, efetuando o logout do perfil de administrador atual.

_Observação_: O usuario inicial root ja estará pre-definido no sistema e não podera ser excluido, para acessalo o nome do usuario e sua senha serão root.

Este documento descreve as funcionalidades principais do software de compra e venda em Python Orientado a Objeto.

## Bibliotecas usadas

- **os system**: Ela permite que o programa interaja com o sistema operacional, fornecendo uma maneira de executar comandos do sistema, como limpar a tela, e pausar o programa.

- **random**: Ela permite que o programa gere números aleatórios.

- **String**: Ela permite que o programa gere strings aleatórias.

## Explicação das classes

**Classe Loja**: 
* A classe Loja representa informações sobre uma loja, como nome, endereço e CNPJ.
* Ela possui um construtor __init__ para inicializar essas informações.


**Classe Produto**: 
* A classe Produtos representa os produtos disponíveis na loja.
* Ela possui várias listas para armazenar informações sobre os produtos, carrinho de compras e histórico de compras.
* Métodos como AddProduto, ListarProdutos, RemProdutos, AddCarrinho, ListCarrinho, RemCarrinho, SomaCarrinho, HistoricoCompra, TotalHistorico e       ListarHistorico permitem a gestão de produtos, carrinho de compras e histórico de compras.
* Ela também calcula o valor total do carrinho e mantém o histórico de vendas da loja.

_Funções da classe_
* AddProduto: Adiciona um novo produto.
* ListarProdutos: Lista os produtos.
* RemProdutos: Remove um produto.
* AddCarrinho: Adiciona um produto ao carrinho.
* ListCarrinho: Lista os produtos do carrinho.
* RemCarrinho: Remove um produto do carrinho.
* SomaCarrinho: Calcula o valor total do carrinho.
* HistoricoCompra: Adiciona um produto ao histórico de compras.
* TotalHistorico: Calcula o valor total do histórico de compras.
* ListarHistorico: Lista o histórico de compras.


**Classe Adm**: 
* A classe Adm representa administradores da loja.
* Ela permite adicionar administradores, verificar credenciais e listar administradores.
* Administradores adicionais podem ser adicionados usando o método cadAdm.
* O método verifyAdm verifica se um administrador com um determinado nome e senha existe.
* O método listarAdm lista os administradores e o método delAdm permite remover administradores (exceto o "root").

_Funções da classe_
* cadAdm: Adiciona um novo administrador.
* verifyAdm: Verifica se um administrador existe.
* listarAdm: Lista os administradores.
* delAdm: Remove um administrador.


**Classe Cliente**: 
* A classe Cliente representa os clientes da loja.
* Ela herda funcionalidades relacionadas a produtos da classe Produtos.
* Permite adicionar clientes, listar clientes, verificar credenciais de login e excluir clientes.

_Funções da classe_
* add_Cliente: Adiciona um novo cliente.
* listar_Cliente: Lista os clientes.
* logar_Cliente: Verifica se um cliente existe, e realiza o login deste cliente.
* delCliente: Remove um cliente.


## Autores

<div align="center">
    <table>
    <tr>
        <td align="center" >
        <a href="https://github.com/Projectyuuri07">
            <img src="https://avatars.githubusercontent.com/Projectyuuri07" width="115px;" alt="Foto_Yuri"/><br>
            <sub>
            <b>Yuri Azevedo</b>
            </sub>
        </a>
        </td>
        <td align="center">
        <a href="https://github.com/vitrolaaotn">
            <img src="https://avatars.githubusercontent.com/vitrolaaotn" width="115px;" alt="Foto_Alexandre"/><br>
            <sub>
            <b>Alexandre</b>
            </sub>
        </a>
        </td>
        <td align="center">
        <a href="https://github.com/1GabsFps">
            <img src="https://avatars.githubusercontent.com/1GabsFps" width="115px;" alt="Foto_Gabriel_Neco"/><br>
            <sub>
            <b>Gabriel Neco</b>
            </sub>
        </a>
        </td>
        <td align="center">
        <a href="https://github.com/DzinnnXn">
            <img src="https://avatars.githubusercontent.com/DzinnnXn" width="115px;" alt="Foto_André_Felipe"/><br>
            <sub>
            <b>André Felipe</b>
            </sub>
        </a>
        </td>
        <td align="center">
        <a href="https://github.com/diegorkkj">
            <img src="https://avatars.githubusercontent.com/diegorkkj" width="115px;" alt="Foto_Diego"/><br>
            <sub>
            <b>Diego</b>
            </sub>
        </a>
        </td>
    </tr>
    </table>
</div>
