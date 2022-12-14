#!/usr/bin/env python3
import sqlalchemy.orm as orm
from model import entities

Session = orm.sessionmaker(bind=entities.engine)
session = Session()

class CidadeDao:
    def get_all_cidades(self):
        return session.query(entities.Cidade.nome).all()
    
    def get_id_by_name(self, name):
        return session.query(entities.Cidade).where(entities.Cidade.nome == name).first()