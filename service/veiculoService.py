#!/usr/bin/env python3
from dao import veiculoDao
class VeiculoService:
  def get_all_veiculos(self):
    try:
      veiculo = veiculoDao.VeiculoDao()
      query = veiculo.get_all_veiculos()
      if query:
        return query
      else:
        raise Exception("Não existem veículos persistidos!")
    except Exception as e:
      return e

  def get_veiculos_by_params(self, modelo, ano, cor, cidade, disponivel):
    try:
      veiculo = veiculoDao.VeiculoDao()
      query = veiculo.get_veiculos_by_params(modelo, ano, cor, cidade, disponivel)
      if query:
        return query
      elif len(query) == 0:
        raise Exception("Não existem veículos persistidos!")
      else:
        raise Exception("Não existem veículos persistidos com dados pesquisados!")
    except Exception as e:
      return e

  def get_all_modelos_for_select(self):
    veiculo = veiculoDao.VeiculoDao()
    query = veiculo.get_all_modelos()
    if query:
      modelos = []
      modelos.append("")
      for modelo in query:
        modelos.append(modelo[0])
      return modelos
    else:
      return["Erro ao carregar modelos"]
  
  def get_veiculos_disponiveis_by_cidade_id(self, id):
    veiculo = veiculoDao.VeiculoDao()
    query = veiculo.get_veiculos_disponiveis_by_cidade_id(id)
    if query:
      return query
    return []

        