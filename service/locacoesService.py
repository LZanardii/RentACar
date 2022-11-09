#!/usr/bin/env python3
from dao import locacaoDao

class LocacoesService:
  ERRO_RESPONSE = "Erro ao carregar locações"

  def get_locacoes_by_params(self, cliente, modelo):
    locacao = locacaoDao.LocacaoDao()
    query = locacao.get_locacoes_by_params(cliente, modelo)
    if query:
      return query
    else:
      return None

  def get_locacoes_finalizadas(self):
    locacao = locacaoDao.LocacaoDao()
    query = locacao.get_locacoes_finalizadas()
    if query:
      return query
    else:
      return[self.ERRO_RESPONSE]

  def have_locacoes_abertas_by_cliente_id(self, id):
    locacao = locacaoDao.LocacaoDao()
    query = locacao.get_locacoes_abertas_by_cliente_id(id)
    if query:
      return True
    else:
      return False

  def get_resumo_todas_locacoes_finalizadas(self, locacoes_finalizadas):
    km_total = 0
    valor_km_total = 0
    diaria_total = 0
    valor_diaria_total = 0
    valor_total = 0

    for locacao in locacoes_finalizadas:
      km_total += locacao.km_rodado
      valor_km_total += locacao.km_rodado * locacao.veiculo.valor_km_rodado
      diaria_total += locacao.qt_dias_reservados
      valor_diaria_total += locacao.qt_dias_reservados * locacao.veiculo.valor_diaria

    valor_total = valor_diaria_total + valor_km_total

    return [km_total, valor_km_total, diaria_total, valor_diaria_total, valor_total]

  def create_locacao(self, cliente, cidade, veiculo, diarias):
    try:
      locacao = locacaoDao.LocacaoDao()
      locacao.create_locacao(cliente, cidade, veiculo, diarias)
    except Exception as e:
      raise e
    

