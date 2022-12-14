from app import app
from service import veiculoService, locacoesService, cidadeService, clienteService
import flask
from flask import render_template, send_file, request, redirect, url_for, flash
from forms import SearchLocacoesForms, SearchVeiculosForms, LocarVeiculoForms, DevolverVeiculoForms
from utils import create_json_locacao, create_file_locacao, create_file_resumo, locacao_validations, create_json_veiuclos_disponiveis
from datetime import date
import json

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/veiculos', methods=['GET', 'POST'])
def veiculos():
  form = SearchVeiculosForms()
  if form.is_submitted():
    veiculo = veiculoService.VeiculoService()
    return render_template('veiculos.html', form=form, veiculos=veiculo.get_veiculos_by_params(form.modelo.data, form.ano.data, form.cor.data, form.cidade.data, form.disponivel.data))
  return render_template('veiculos.html', form=form)


@app.route('/veiculos/locacao', methods=['GET', 'POST'])
def locacao():
  form = LocarVeiculoForms()
  if form.is_submitted():
    cidade_service = cidadeService.CidadeService()
    cliente_service = clienteService.ClienteService()
    veiculos_disponiveis = create_json_veiuclos_disponiveis(locacao_validations(form.cliente.data, form.cidade.data))
    return render_template('locacao.html', form=form, veiculos=veiculos_disponiveis,\
      cidade_id=cidade_service.get_cidade_by_name(form.cidade.data).id, \
        cliente_id=cliente_service.get_cliente_id_by_name(form.cliente.data))
  return render_template('locacao.html', form=form)

@app.route('/veiculos/locacao/save', methods=['GET', 'POST'])
def locacao_save():
  if request.method == 'GET':
    return redirect(url_for('locacao'))
  locacao_service = locacoesService.LocacoesService()
  if (int(request.form['diaria']) <= 0):
    flash("LOCAÇÃO NÃO FINALIZADA; Diária não pode ser menor ou igual a 0", category='alert')
    return redirect(url_for('locacao'))
  try:
    locacao_service.create_locacao(request.form['cliente'], request.form['cidade'], request.form['veiculo'], request.form['diaria'])
    flash(message="LOCAÇÃO FINALIZADA com sucesso", category='success')
    return redirect(url_for('locacao'))
  except Exception as e:
    flash(e)
    return redirect(url_for('locacao'))


@app.route('/veiculos/devolucao', methods=['GET', 'POST'])
def devolucao():
  form = DevolverVeiculoForms()
  if form.is_submitted() and form.is_valid():
    cidade_service = cidadeService.CidadeService()
    locacoes_service = locacoesService.LocacoesService()
    locacao = locacoes_service.get_locacao_aberta_by_cliente_name(form.cliente.data)
    return render_template('devolucao.html', form=form, locacao=locacao, cidade=cidade_service.get_cidade_by_name(form.cidade.data), quilometragem=float(form.quilometragem.data))
  elif form.is_submitted() and form.is_valid() == False:
    flash("Quilometragem não pode ser menor que 0")
    return redirect(url_for('devolucao'))
  return render_template('devolucao.html', form=form)


@app.route('/veiculos/devolucao/save', methods=['GET', 'POST'])
def devolucao_save():
  if request.method == 'GET':
    return redirect(url_for('devolucao'))
  try:
    locacoes_service = locacoesService.LocacoesService()
    locacoes_service.finish_locacao(request.form['locacao_id'], request.form['cidade_destino_id'], request.form['km_rodado'], request.form['veiculo_id'])
    flash(message="DEVOLUÇÃO FINALIZADA com sucesso", category='success')
    return redirect(url_for('devolucao'))
  except Exception:
    flash("Erro ao finalizar devolução", category='alert')
    return redirect(url_for('devolucao'))


@app.route('/locacoes', methods=['GET', 'POST'])
def locacoes():
  form = SearchLocacoesForms()
  if form.is_submitted() and form.is_valid():
    locacoes = locacoesService.LocacoesService()
    query = locacoes.get_locacoes_by_params(form.cliente.data, form.modelo.data)
    post_json = create_json_locacao(query)
    if post_json:
      return render_template('locacoes.html', form=form, locacoes=query, mkdjson=post_json)
    else:
      print("entrei")
      flash("Não existem locações com os filtros selecionados")
      return redirect(url_for('locacoes'))
  elif form.is_submitted() and form.is_valid() == False:
    flash("Selecione ao menos um dos campos abaixo")
    return redirect(url_for('locacoes'))
  return render_template('locacoes.html', form=form)


@app.route('/locacoes/download', methods=['POST', 'GET'])
def locacoes_md_download():
  if request.method == 'GET':
    return redirect(url_for('locacoes'))
  name = f'RentACar-RelatorioLocacoes.md'
  create_file_locacao(name, request.form['locacoes'])
  return send_file(name, as_attachment=True)


@app.route('/resumo', methods=['POST', 'GET'])
def resumo():
  locacoes_service = locacoesService.LocacoesService()
  locacoes_finalizadas = locacoes_service.get_locacoes_finalizadas()
  resumo = locacoes_service.get_resumo_todas_locacoes_finalizadas(locacoes_finalizadas)
  return render_template('resumo.html', locacoes=locacoes_finalizadas, resumo=resumo)


@app.route('/resumo/download', methods=['POST', 'GET'])
def resumo_md_download():
  if flask.request.method == 'GET':
    return redirect(url_for('resumo'))
  date_now = date.today()
  name = f'RentACar-Resumo{date_now}.md'
  create_file_resumo(name, request.form['resumo'])
  return send_file(name, as_attachment=True)