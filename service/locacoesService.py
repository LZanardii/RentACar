#!/usr/bin/env python3
from dao import locacaoDao

class LocacoesService:
  def get_locacoes_by_params(self, cliente, modelo):
    locacao = locacaoDao.LocacaoDao()
    query = locacao.get_locacoes_by_params(cliente, modelo)
    if query:
      return query
    else:
      return["Erro ao carregar modelos"]
