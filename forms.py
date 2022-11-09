from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import Length, DataRequired
from service import veiculoService, clienteService, cidadeService
        
class SearchVeiculosForms(FlaskForm):
  cor = StringField('cor', validators=[Length(min=1)])
  ano = StringField('ano', validators=[Length(min=1)])
  modelo = StringField('modelo', validators=[Length(min=1)])
  cidade = StringField('cidade', validators=[Length(min=1)]) 
  disponivel = BooleanField('disponivel') 
  submit = SubmitField('Pesquisar') 
    # def is_valid(self):
    #     if (
    #         self.cor.validate(Length(min=1)) == False and 
    #         self.ano.validate(Length(min=1)) == False and 
    #         self.modelo.validate(Length(min=1)) == False and
    #         self.disponivel.validate(self.disponivel.data == False) and
    #         self.cidade.validate(Length(min=1)) == False):
    #         return False
    #     return True
class SearchLocacoesForms(FlaskForm):
  veiculos = veiculoService.VeiculoService()
  clientes = clienteService.ClienteService()

  cliente = SelectField(choices=clientes.get_all_nomes_for_select())
  modelo = SelectField(choices=veiculos.get_all_modelos_for_select())
  submit = SubmitField('Pesquisar') 

  def is_valid(self):
    if (self.cliente.data != "" or self.modelo.data != ""):
      return True
    return False

class LocarVeiculoForms(FlaskForm):
  clientes = clienteService.ClienteService()
  cidades = cidadeService.CidadeService()

  cliente = SelectField(choices=clientes.get_all_nomes_for_select(), validators=[DataRequired()])
  cidade = SelectField(choices=cidades.get_all_cidades_for_select(), validators=[DataRequired()])
  submit = SubmitField('Prosseguir') 

  def is_valid(self):
    if (self.cliente.data != "" and self.cidade.data != ""):
      return True
    return False
