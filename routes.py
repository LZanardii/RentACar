from app import app
from service import veiculoService, locacoesService
from flask import render_template
from forms import SearchLocacoesForms, SearchVeiculosForms

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
    # cliente = clienteDao.ClienteDao()
    # clientes = cliente.get_all_clientes()
    return render_template('locacao.html')

@app.route('/veiculo/devolucao')
def devolucao():
    # cliente = clienteDao.ClienteDao()
    # clientes = cliente.get_all_clientes()
    return render_template('devolucao.html')

@app.route('/locacoes', methods=['GET', 'POST'])
def locacoes():
    form = SearchLocacoesForms()
    if form.is_submitted() and form.is_valid():
        locacoes = locacoesService.LocacoesService()
        return render_template('locacoes.html', form=form, locacoes=locacoes.get_locacoes_by_params(form.cliente.data, form.modelo.data))
    return render_template('locacoes.html', form=form)

@app.route('/resumo')
def resumo():
    # cliente = clienteDao.ClienteDao()
    # clientes = cliente.get_all_clientes()
    return render_template('resumo.html')