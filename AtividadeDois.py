import os

os.system("cls || clean")

class conta_bancaria:

    def __init__(self, banco: str, agencia: str, numero_conta: str, tipo_conta: str, saldo_atual: float, limite_disponivel: str) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.saldo_atual = saldo_atual
        self.limite_disponivel = limite_disponivel


    def __str__(self) -> str:
        return (f"Banco: {self.banco}"
        f"\nAgência: {self.agencia}"
        f"\nNúmero da conta: {self.numero_conta}"
        f"\nTipo da conta: {self.tipo_conta}"
        f"\nSaldo Atual: {self.saldo_atual}"
        f"\nLimite dísponivel: {self.limite_disponivel}")

class funcionario:


    def __init__(self, codigo_funcionario: str, nome: str, endereco: str, telefone: str, email: str, conta_banco: conta_bancaria ) -> None:
        self.codigo_funcionario = codigo_funcionario
        self.nome = nome
        self.endereco = endereco      
        self.telefone = telefone
        self.email = email
        self.conta_banco = conta_banco


    def exibir_dados(self) -> str:
            return (f"Nome do funcionário: {self.nome}"
                    f"\nTelefone: {self.telefone}"
                    f"\nCódigo do funcinário: {self.codigo_funcionario}"
                    f"\nE-mail: {self.email}"
                    f"\nEndereço: {self.endereco}"
                    f"\nConta bancária: {self.conta_banco}")

conta = conta_bancaria("Inter","1545645","3030","Corrente", 6000, "80,000 R$")
funcionario_um = funcionario("15151545","Roberton","Rua b 22 A", "71986320995","roberton@hotmail.com", conta)


print(funcionario_um.exibir_dados())

