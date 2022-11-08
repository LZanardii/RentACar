from app import app
from service import veiculoService, locacoesService
import flask
from flask import render_template, send_file, request, redirect, url_for
from forms import SearchLocacoesForms, SearchVeiculosForms
from utils import create_json_locacao, create_file_locacao, create_file_resumo
from datetime import date

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

@app.route('/veiculo/locacao')
def locacao():
  return render_template('locacao.html')

@app.route('/veiculo/devolucao')
def devolucao():
  return render_template('devolucao.html')

@app.route('/locacoes', methods=['GET', 'POST'])
def locacoes():
  form = SearchLocacoesForms()
  if form.is_submitted() and form.is_valid():
    locacoes = locacoesService.LocacoesService()
    query = locacoes.get_locacoes_by_params(form.cliente.data, form.modelo.data)
    return render_template('locacoes.html', form=form, locacoes=query, mkdjson=create_json_locacao(query))
  return render_template('locacoes.html', form=form)

@app.route('/locacoes/download', methods=['POST', 'GET'])
def locacoes_md_download():
  if flask.request.method == 'GET':
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