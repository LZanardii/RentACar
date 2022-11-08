#!/usr/bin/env python3
import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///rent-a-car.db', echo=False, connect_args={'check_same_thread': False})
conn = engine.connect()

Base = orm.declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)


class Cidade(Base):
    __tablename__ = 'cidade'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)


class Veiculo(Base):
    __tablename__ = 'veiculo'

    id = db.Column(db.Integer, primary_key=True)
    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id'), nullable=False)
    modelo = db.Column(db.String(100),  nullable=False)
    cor = db.Column(db.String(100),  nullable=False)
    ano = db.Column(db.Integer,  nullable=False)
    odometro = db.Column(db.Integer,  nullable=False)
    disponivel = db.Column(db.Boolean,  nullable=False)
    valor_diaria = db.Column(db.Float,  nullable=False)
    valor_km_rodado = db.Column(db.Float,  nullable=False)


class Locacao(Base):
    __tablename__ = 'locacao'

    id = db.Column(db.Integer, primary_key=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculo.id'), nullable=False) 
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cidade_origem_id = db.Column(db.Integer, db.ForeignKey('cidade.id'), nullable=False)
    cidade_destino_id = db.Column(db.Integer, db.ForeignKey('cidade.id'))
    km_rodado = db.Column(db.Integer)
    qt_dias_reservados = db.Column(db.Integer, nullable=False)

Veiculo.cidade = orm.relationship('Cidade', back_populates='veiculos')
Cidade.veiculos = orm.relationship('Veiculo', back_populates='cidade')

Locacao.veiculo = orm.relationship('Veiculo', back_populates='locacoes')
Veiculo.locacoes = orm.relationship('Locacao', back_populates='veiculo')

Locacao.cliente = orm.relationship('Cliente', back_populates='locacoes')
Cliente.locacoes = orm.relationship('Locacao', back_populates='cliente')

Locacao.cidade_origem = orm.relationship('Cidade', back_populates='locacoes_origem', foreign_keys=[Locacao.cidade_origem_id])
Cidade.locacoes_origem = orm.relationship('Locacao', back_populates='cidade_origem',  foreign_keys=[Locacao.cidade_origem_id])

Locacao.cidade_destino = orm.relationship('Cidade', back_populates='locacoes_destino', foreign_keys=[Locacao.cidade_destino_id])
Cidade.locacoes_destino = orm.relationship('Locacao', back_populates='cidade_destino', foreign_keys=[Locacao.cidade_destino_id])

Base.metadata.create_all(engine)