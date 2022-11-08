#!/usr/bin/env python3
from dao import clienteDao

class ClienteService:
  def get_all_nomes(self):
    cliente = clienteDao.ClienteDao()
    query = cliente.get_all_nomes()
    if query:
      clientes = []
      clientes.append("")
      for cliente in query:
        clientes.append(cliente[0])
      return clientes
    else:
      return["Erro ao carregar modelos"]
