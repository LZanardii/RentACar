#!/usr/bin/env python3
from dao import clienteDao
from service import locacoesService

class ClienteService:
  def get_all_nomes_for_select(self):
    cliente = clienteDao.ClienteDao()
    query = cliente.get_all_nomes()
    if query:
      clientes = []
      clientes.append("")
      for cliente in query:
        clientes.append(cliente[0])
      return clientes
    else:
      return["Erro ao carregar clientes"]

  def have_locacao_ativa_search_by_name(self, name):
    cliente_dao = clienteDao.ClienteDao()
    locacao_service = locacoesService.LocacoesService()
    cliente = cliente_dao.get_id_by_name(name)
    locacoes_abertas = locacao_service.have_locacoes_abertas_by_cliente_id(cliente.id)
    return locacoes_abertas



    

