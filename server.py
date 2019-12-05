from funcoes import indo, voltando

indo('Piloto', 'Oficial 1')
voltando('Piloto')

indo('Piloto', 'Oficial 2')
voltando('Piloto')

indo('Chefe Servico', 'Comissaria 1')
voltando('Chefe Servico')

indo('Piloto', 'Chefe Servico')
voltando('Chefe Servico')

indo('Chefe Servico', 'Comissaria 2')
voltando('Chefe Servico')

indo('Policial', 'Presidiario')
voltando('Piloto')

indo('Piloto', 'Chefe Servico')

print('Todos chegaram seguros e de acordo com as regras pré determinadas!')