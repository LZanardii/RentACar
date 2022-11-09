import json
from service import clienteService, cidadeService
from flask import redirect, url_for, flash

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

def create_file_locacao(name, locacoes):
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

def create_file_resumo(name, resumo):
  resumo_json = json.loads(resumo)
  with open(name, 'w', encoding="UTF-8") as f:
    f.write('| KMs até agora | Total R$ KM  | Dias Reservados | Total R$ Diárias | Total R$ |' + '\n')
    f.write('|---------------|--------------|-----------------|------------------|----------|' + '\n')
    f.write('| {} | {} | {} | {} | {} |'.format(resumo_json[0], resumo_json[1], resumo_json[2], resumo_json[3], resumo_json[4]))
    f.close()

def locacao_validations(cliente, cidade):
  cliente_service = clienteService.ClienteService()
  cidade_service = cidadeService.CidadeService()

  if cliente_service.have_locacao_ativa_search_by_name(cliente):
    flash(f'Cliente {cliente} possui locação em aberto! Finalize antes de realizar outra locação')
    redirect(url_for('locacao'))
    return

  veiculos_disponiveis = cidade_service.get_veiculos_disponiveis_by_cidade_name(cidade)

  if len(veiculos_disponiveis) == 0:
    flash(f'{cidade} não possui carros disponíveis')
    redirect(url_for('locacao'))
    return
  return veiculos_disponiveis

def create_json_veiuclos_disponiveis(veiculos):
  if veiculos:
    list_veiculos = []
    for veiculo in veiculos:
      list_veiculos.append(
        {
          "id": veiculo.id,
          "modelo": str(veiculo.modelo), 
          "cor": str(veiculo.cor), 
          "ano": str(veiculo.ano), 
        }
      )
    return json.loads(json.dumps(list_veiculos))
  else:
    return []
