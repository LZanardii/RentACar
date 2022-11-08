#!/usr/bin/env python3
from dao import locacaoDao

class LocacoesService:
  def get_locacoes_by_params(self, cliente, modelo):
    locacao = locacaoDao.LocacaoDao()
    query = locacao.get_locacoes_by_params(cliente, modelo)
    
    print('=' * 20)
    for r in query:
      print('Cliente:', r.cliente.nome)
      print('Veículo:', r.veiculo.modelo)
      print('Origem:', r.cidade_origem.nome)
      print('Destino:', r.cidade_destino.nome)
      print('=' * 20)
    
    if query:
      return query
    else:
      return["Erro ao carregar modelos"]
