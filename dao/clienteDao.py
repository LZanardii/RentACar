#!/usr/bin/env python3
import sqlalchemy.orm as orm
from model import entities

Session = orm.sessionmaker(bind=entities.engine)
session = Session()

class ClienteDao:
    def get_all_nomes(self):
        return session.query(entities.Cliente.nome).all()
    
    def get_id_by_name(self, name):
        return session.query(entities.Cliente.id).where(entities.Cliente.nome == name).first()

    def get_clientes_locacao_aberta(self):
        return session.query(entities.Cliente.nome).join(entities.Locacao).where(entities.Cliente.id == entities.Locacao.cliente_id).filter(entities.Locacao.km_rodado == None).all()
        