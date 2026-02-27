import json
from datetime import datetime

# CLASSES

class ContaBancaria:
    """
Cria uma conta bancaria e permite fazer saques, depósitos, transferências e ver histórico
    """
    def __init__(self, id, nome, historico, saldo = 0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        self.historico = historico

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(f'Deposito de €{valor}')
        return "\033[32mValor depositado com sucesso!\033[m"

    def sacar(self, valor):
        if self.saldo < valor:
            return "\033[31mSaldo insuficiente!\033[m"
        else:
            self.saldo -= valor
            self.historico.append(f'Saque de -€{valor}')
            return "\033[32mSaque realizado!\033[m"

    def transferir(self,conta2, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(f'Transferência de €{valor} para a conta {conta2.id}')
            conta2.saldo += valor #CONTA QUE RECEBE A TRANSFERENCIA
            conta2.historico.append(f'Transferência de €{valor} recebida de conta {self.id}')
            return '\033[32mTransferência realizada\033[m'
        else:
            return '\033[31mSaldo insuficiente\033[m'

    def para_dict(self):
        return {'id': self.id, 'nome': self.nome, 'saldo': self.saldo, 'historico': self.historico}

    def exibir_historico(self):
        for movimento in self.historico:
            print(movimento)



# FUNCÕES

def salvar_arquivo(contas):
    with open('contas.json', 'w') as f:
        json.dump([conta.para_dict() for conta in contas], f, indent=4)

def menu():
    print("»«"*15)
    print("\033[33m1 — Criar conta\n"
          "2 — Depositar\n"
          "3 — Sacar\n"
          "4 — Transferir\n"
          "5 — Ver extrato\n"
          "0 — Sair\033[m")
    print("»«" * 15)
    esc = int(input('Escolha uma opção acima: '))
    return esc

def criar_conta(numero_conta, conta):
    historico = []
    nome_conta = input('Digite seu nome: ').strip().capitalize().title()
    saldo_inicial = 200 #Valor obrigatorio a ser depositado para abrir a conta
    conta.append(ContaBancaria(numero_conta,nome_conta,historico,saldo_inicial))
    print('\033[32mConta criada com sucesso!\033[m')
    salvar_arquivo(conta)

def buscar_conta(contas):
    id = int(input('Digite o id da conta: '))
    for conta in contas:
        if conta.id == id:
            return conta
    return None

def seal():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("\n" + "="*60)
    print("#>>> SYSTEM SEAL ENGAGED")
    print(f"#>>> SIGNED BY: BRONDANI")
    print(f"#>>> TIMESTAMP: {agora}")
    print("#>>> STATUS: SECURE")
    print("="*60)