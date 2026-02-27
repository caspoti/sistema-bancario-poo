from Dados_Contas import *
from time import sleep

contas = list()

try:
    with open('contas.json', 'r') as f:
        dados = json.load(f)
        for conta_dict in dados:
            conta = ContaBancaria(conta_dict["id"],
                                  conta_dict["nome"],
                                  conta_dict["historico"],
                                  conta_dict["saldo"])
            contas.append(conta)
except:  # CRIA O ARQUIVO (ESTOQUE), CASO ELE NÃO EXISTA
    with open('contas.json', 'w') as f:
        json.dump([conta.para_dict() for conta in contas], f, indent=4)
numero_conta = 100  # A primeira conta vai receber o ID = 100

while True:
    esc = menu()
    sleep(0.5)
    if esc == 0:
        print('\033[33mEncerrando programa...\033[m')
        sleep(2)
        seal()
        break
    elif esc == 1:
        for conta in contas:
            numero_conta = 100 + (len(contas) - 1)
            if conta.id == numero_conta:
                numero_conta += 1
        criar_conta(numero_conta, contas)
        sleep(2)
    elif esc == 2: # DEPOSITAR
        conta = buscar_conta(contas)
        valor = float(input("Digite o valor para depositar: "))
        try:
            print(conta.deposito(valor))
            salvar_arquivo(contas)
        except:
            print("»«" * 15)
            print('\033[31mConta não encontrada ou não existe!\033[m')
            sleep(2)
    elif esc == 3: # SACAR
        conta = buscar_conta(contas)
        valor = float(input("Digite o valor para sacar: "))
        try:
            print(conta.sacar(valor))
            salvar_arquivo(contas)
        except:
            print("»«" * 15)
            print('\033[31mConta não encontrada ou não existe!\033[m')
        sleep(2)
    elif esc == 4: #TRANSFERIR
        print('ID DA SUA CONTA')
        conta = buscar_conta(contas)
        print('ID DA CONTA QUE DESEJA TRANSFERIR')
        conta2 = buscar_conta(contas)
        if conta == conta2:
            print("»«" * 25)
            print('\033[31mVocê não pode transferir para sua própria conta!\033[m')
        else:
            valor = float(input('Digite o valor da transferência: '))
            try:
                print(conta.transferir(conta2, valor))
                salvar_arquivo(contas)
            except:
                print('\033[31mUma das contas não foi encontrada ou não existe!\033[m')
        sleep(2)
    elif esc == 5: # EXTRATO DA CONTA
       conta = buscar_conta(contas)
       try:
           print('\033[36m»» EXTRATO ««\033[m'.center(40, '-'))
           conta.exibir_historico()
           print(f'SALDO DE €{conta.saldo:,.2f}')
       except:
           print('\033[31mConta não encontrada ou não existe!\033[m')
       sleep(2)
    else:
        print('\033[31mA opção não existe\033[m')
        sleep(2)
# ARRUMAR O EXTRATO DA CONTA
# SEGUIR A MESMA LOGICA, USANDO O BUSCAR_CONTA E DEPOIS APLICANDO TRY E A FUNCAO exibir_historico