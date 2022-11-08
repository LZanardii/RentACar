#!/usr/bin/env python3
from model import entities

Session = entities.orm.sessionmaker(bind=entities.engine)
session = Session()

try:
    cidades = [
        entities.Cidade(id=1,nome="Canoas"),
        entities.Cidade(id=2,nome="Criciúma"),
        entities.Cidade(id=3,nome="Curitiba"),
        entities.Cidade(id=4,nome="Florianópolis"),
        entities.Cidade(id=5,nome="Lajes"),
        entities.Cidade(id=6,nome="Pelotas"),
        entities.Cidade(id=7,nome="Porto Alegre"),
        entities.Cidade(id=8,nome="São Leopoldo")
    ]
    
    clientes = [
        entities.Cliente(id=1,nome="Ana"),
        entities.Cliente(id=2,nome="Ivan"),
        entities.Cliente(id=3,nome="Marcos"),
        entities.Cliente(id=4,nome="Maria"),
        entities.Cliente(id=5,nome="Pedro"),
        entities.Cliente(id=6,nome="Sofia")
    ]
    
    veiculos = [
        entities.Veiculo(id=1, modelo="Gol",      cor="Cinza",     ano="2016",  odometro="137852", cidade_id=7, disponivel=True,   valor_diaria=108.67, valor_km_rodado=0.93),
        entities.Veiculo(id=2, modelo="Up",       cor="Branco",    ano="2017",  odometro="86541",  cidade_id=8, disponivel=False,  valor_diaria=70.12,  valor_km_rodado=0.47),
        entities.Veiculo(id=3, modelo="Argo",     cor="Preto",     ano="2019",  odometro="42876",  cidade_id=1, disponivel=True,   valor_diaria=121.4,  valor_km_rodado=1.02),
        entities.Veiculo(id=4, modelo="Mobi",     cor="Vermelho",  ano="2018",  odometro="61907",  cidade_id=3, disponivel=True,   valor_diaria=76.19,  valor_km_rodado=0.39),
        entities.Veiculo(id=5, modelo="Gol",      cor="Azul",      ano="2019",  odometro="49389",  cidade_id=2, disponivel=False,  valor_diaria=77.47,  valor_km_rodado=0.51),
        entities.Veiculo(id=6, modelo="Onix",     cor="Prata",     ano="2017",  odometro="77635",  cidade_id=4, disponivel=False,  valor_diaria=78.74,  valor_km_rodado=0.55),
        entities.Veiculo(id=7, modelo="Sandero",  cor="Cinza",     ano="2019",  odometro="34518",  cidade_id=8, disponivel=True,   valor_diaria=82.61,  valor_km_rodado=0.64),
        entities.Veiculo(id=8, modelo="Duster",   cor="Branco",    ano="2018",  odometro="57114",  cidade_id=7, disponivel=True,   valor_diaria=118.17, valor_km_rodado=1.05),
        entities.Veiculo(id=9, modelo="Cruze",    cor="Preto",     ano="2020",  odometro="8013",   cidade_id=6, disponivel=False,  valor_diaria=120.63, valor_km_rodado=1.08),
        entities.Veiculo(id=10,modelo="Argo",     cor="Vermelho",  ano="2017",  odometro="106857", cidade_id=5, disponivel=True,   valor_diaria=91.96,  valor_km_rodado=0.63),
    ]
    
    locacoes = [
        entities.Locacao(id=1,  veiculo_id=3,  cliente_id=2, cidade_origem_id=1, cidade_destino_id=1,    km_rodado=291,   qt_dias_reservados=2),
        entities.Locacao(id=2,  veiculo_id=8,  cliente_id=3, cidade_origem_id=1, cidade_destino_id=7,    km_rodado=917,   qt_dias_reservados=4),
        entities.Locacao(id=3,  veiculo_id=1,  cliente_id=1, cidade_origem_id=1, cidade_destino_id=7,    km_rodado=674,   qt_dias_reservados=3),
        entities.Locacao(id=4,  veiculo_id=4,  cliente_id=6, cidade_origem_id=6, cidade_destino_id=3,    km_rodado=1433,  qt_dias_reservados=5),
        entities.Locacao(id=5,  veiculo_id=9,  cliente_id=3, cidade_origem_id=6, cidade_destino_id=None, km_rodado=None,  qt_dias_reservados=5),
        entities.Locacao(id=6,  veiculo_id=10, cliente_id=6, cidade_origem_id=2, cidade_destino_id=5,    km_rodado=545,   qt_dias_reservados=4),
        entities.Locacao(id=7,  veiculo_id=6,  cliente_id=1, cidade_origem_id=4, cidade_destino_id=None, km_rodado=None,  qt_dias_reservados=4),
        entities.Locacao(id=8,  veiculo_id=7,  cliente_id=5, cidade_origem_id=8, cidade_destino_id=8,    km_rodado=478,   qt_dias_reservados=2),
        entities.Locacao(id=9,  veiculo_id=2,  cliente_id=5, cidade_origem_id=8, cidade_destino_id=None, km_rodado=None,  qt_dias_reservados=6),
        entities.Locacao(id=10, veiculo_id=5,  cliente_id=4, cidade_origem_id=2, cidade_destino_id=None, km_rodado=None,  qt_dias_reservados=3)
    ]
    
    session.add_all(cidades)
    session.add_all(clientes)
    session.add_all(veiculos)
    session.add_all(locacoes)
    
    session.commit()
except Exception as e:
    session.rollback()
    print(e)