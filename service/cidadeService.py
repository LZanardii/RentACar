#!/usr/bin/env python3
from dao import cidadeDao

class CidadeService:
  def get_all_cidades_for_select(self):
    cidade = cidadeDao.CidadeDao()
    query = cidade.get_all_cidades()
    if query:
      clientes = []
      clientes.append("")
      for cidade in query:
        clientes.append(cidade[0])
      return clientes
    else:
      return["Erro ao carregar cidades"]
