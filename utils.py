import json

def create_json_locacao(locacoes):
  NULL_ATRIBUTE = "Dado nao mapeado"
  list_locacoes = []
  for locacao in locacoes:
    list_locacoes.append(
      {
        "cliente":str(locacao.cliente.nome), 
        "modelo":str(locacao.veiculo.modelo), 
        "cidade_origem":str(locacao.cidade_origem.nome), 
        "cidade_destino":str(locacao.cidade_destino.nome if locacao.cidade_destino else NULL_ATRIBUTE), 
        "km_rodado":str(locacao.km_rodado if locacao.km_rodado else NULL_ATRIBUTE), 
        "qtd_dias":str(locacao.qt_dias_reservados), 
        "valor_total":str(locacao.km_rodado * locacao.veiculo.valor_km_rodado + locacao.qt_dias_reservados * locacao.veiculo.valor_km_rodado if locacao.km_rodado else 'Locação nao finalizada'), 
      }
    )
  return json.dumps(list_locacoes)

def create_file_locacao(name ,locacoes):
  locacoes_json = json.loads(locacoes)
  with open(name, 'w', encoding="UTF-8") as f:
    f.write('| Clinete | Modelo | Cidade de Origem | Cidade de Destino | KM Rodados | Quantidade de Dias | Valor Total |' + '\n')
    f.write('|---------|--------|------------------|-------------------|------------|--------------------|-------------|' + '\n')
    for locacao in locacoes_json:
      f.write('| {} | {} | {} | {} | {} | {} | {} |'\
        .format(locacao['cliente'], locacao['modelo'],\
           locacao['cidade_origem'], locacao['cidade_destino'],\
            locacao['km_rodado'], locacao['qtd_dias'], locacao['valor_total']) \
          + '\n')
    f.close()
