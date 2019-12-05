terminal = ['Piloto', 'Chefe Servico','Oficial 1','Oficial 2', 'Comissaria 1', 'Comissaria 2', 'Presidiario','Policial']
aviao = []

def indo(pessoa1, pessoa2):
    terminal.remove(pessoa1)
    terminal.remove(pessoa2)
    print('- Viagem de ida:')
    print(f'O motorista {pessoa1} e o passageiro {pessoa2} estão saindo do terminal e indo para o avião')
    print()
    aviao.append(pessoa1)
    aviao.append(pessoa2)
    situacao()

def voltando(pessoa1, pessoa2=None):
    aviao.remove(pessoa1)
    if pessoa2:
        aviao.remove(pessoa2)
    print('- Viagem de volta:')
    print(f'O motorista {pessoa1} e o passageiro {pessoa2} estão saindo do avião e indo para o terminal')
    print()
    terminal.append(pessoa1)
    if pessoa2:
        terminal.append(pessoa2)
    situacao()

def situacao():
    print('- Situação:')
    print(f'Pessoas no terminal = {terminal}')
    print(f'Pessoas no avião = {aviao}')
    print()