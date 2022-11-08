#!/usr/bin/env python3
import sqlalchemy.orm as orm
from model import entities

Session = orm.sessionmaker(bind=entities.engine)
session = Session()

class VeiculoDao:

  def get_all_veiculos(self):
    return session.query(entities.Veiculo, entities.Cidade).where(entities.Veiculo.cidade_id == entities.Cidade.id).all()

  def get_veiculos_by_params(self, modelo, ano, cor, cidade, disponivel):
    queries = []
    if len(modelo) > 0:
      queries.append(entities.Veiculo.modelo.like(f'%{modelo}%'))
    if len(ano) > 0:
      queries.append(entities.Veiculo.ano == ano)
    if len(cidade) > 0:
      queries.append(entities.Cidade.nome.like(f'%{cidade}%'))
    if len(cor) > 0:
      queries.append(entities.Veiculo.cor.like(f'%{cor}%'))
    if disponivel:
      queries.append(entities.Veiculo.disponivel == True)
    return session.query(entities.Veiculo, entities.Cidade).where(entities.Veiculo.cidade_id == entities.Cidade.id).filter(*queries).all()
  
  def get_all_modelos(self):
    return session.query(entities.Veiculo.modelo).all()



        