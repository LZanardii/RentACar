#!/usr/bin/env python3
import sqlalchemy.orm as orm
from sqlalchemy.orm import aliased
from model import entities

Session = orm.sessionmaker(bind=entities.engine)
session = Session()

class LocacaoDao:
  def get_all_locacoes(self):
    cidade_origem = aliased(entities.Cidade)
    cidade_destino = aliased(entities.Cidade)

    return session.query(entities.Locacao).join(entities.Cliente).join(cidade_origem, cidade_origem.id == entities.Locacao.cidade_origem_id).join(entities.Veiculo).outerjoin(cidade_destino, cidade_destino.id == entities.Locacao.cidade_destino_id, isouter=True).all()

  def get_locacoes_by_params(self, cliente, modelo):
    cidade_origem = aliased(entities.Cidade)
    cidade_destino = aliased(entities.Cidade)

    queries = []

    if len(cliente) > 0:
      queries.append(entities.Cliente.nome == cliente)
    if len(modelo) > 0:
      queries.append(entities.Veiculo.modelo == modelo)
    
    return session.query(entities.Locacao)\
      .join(entities.Cliente)\
        .join(entities.Veiculo)\
          .join(cidade_origem, cidade_origem.id == entities.Locacao.cidade_origem_id)\
            .outerjoin(cidade_destino, cidade_destino.id == entities.Locacao.cidade_destino_id, isouter=True)\
              .where(*queries).all()

  def get_locacoes_finalizadas(self):
    cidade_origem = aliased(entities.Cidade)
    cidade_destino = aliased(entities.Cidade)
    
    return session.query(entities.Locacao)\
      .join(entities.Cliente)\
        .join(entities.Veiculo)\
          .join(cidade_origem, cidade_origem.id == entities.Locacao.cidade_origem_id)\
            .join(cidade_destino, cidade_destino.id == entities.Locacao.cidade_destino_id)\
              .where().all()