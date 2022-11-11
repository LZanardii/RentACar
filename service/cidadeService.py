#!/usr/bin/env python3
from dao import cidadeDao
from service import veiculoService

class CidadeService:
  def get_all_cidades_for_select(self):
    cidade_dao = cidadeDao.CidadeDao()
    query = cidade_dao.get_all_cidades()
    if query:
      clientes = []
      clientes.append("")
      for cidade_dao in query:
        clientes.append(cidade_dao[0])
      return clientes
    else:
      return["Erro ao carregar cidades"]

  def get_cidade_by_name(self, name):
    cidade_dao = cidadeDao.CidadeDao()
    cidade = cidade_dao.get_id_by_name(name)
    if cidade:
      return cidade
    else:
      return[]
  
  def get_veiculos_disponiveis_by_cidade_name(self, name):
    cidade_dao = cidadeDao.CidadeDao()
    veiculo_service = veiculoService.VeiculoService()
    cidade = cidade_dao.get_id_by_name(name)
    veiculos_disponiveis = veiculo_service.get_veiculos_disponiveis_by_cidade_id(cidade.id)
    return veiculos_disponiveis
