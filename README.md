<h1 align="center"> Sistema para Locadora de Veículos </h1>
<h3>Usando Flask Framework</h3>
<p> 
  O trabalho consiste em desenvolver um sistema Web simplificado para locadoras de veículos.
O código fonte deve ser desenvolvido em Python 3, utilizar o conteúdo trabalhado em aula. O
programa deve ser orientado a objetos, utilizar a biblioteca Flask, e para persistência de dados,
deve ser usado um banco SQLite acessado a partir da biblioteca SQLAlchemy.
</p>
<h3>Diagrama de Classes:</h3>
<p>O diagrama de classes abaixo representa o estado inicial para o desenvolvimento. É permitido
adicionar atributos e métodos de acordo com a necessidade.</p>
<img src="/img/diagrama-classes.png">
<h3>Funcionalidades:</h3>
<p>O programa deverá conter as seguintes funcionalidades no menu:</p>
<ul>
<li>1. Consultar veículos: O usuário seleciona em um combobox o nome de um atributo
(modelo, cor, ano ou cidade) e em uma caixa de texto/combobox, digita/escolhe o valor
do atributo. Após pressionar o botão “Consultar”, o sistema mostra na tela uma tabela
com todos os dados dos veículos que se enquadram na condição.</li>
<li>2. Realizar locação: Cliente seleciona em um combobox seu nome e a cidade de origem
em outro combobox, e pressiona o botão “Prosseguir”. Nesse instante, o sistema
verifica se o cliente possui alguma locação ativa. Caso afirmativo, mostra uma
mensagem informando que o cliente não pode fazer nova locação, e não prossegue com
a reserva. O sistema também verifica se há ao menos um veículo disponível na cidade
informada. Caso não haja, deve informar o cliente e não prosseguir com a locação. Mas
se existir ao menos um veículo disponível, e o cliente não possuir nenhuma locação
ativa, o sistema mostra em uma tabela com radiogroup o modelo, cor e ano de todos os
veículos disponíveis na cidade. Em seguida, o cliente seleciona o radiobutton
correspondente ao veículo que deseja alugar, informa a quantidade de diárias, e
pressiona o botão “Realizar Locação”. Nesse momento, o sistema registra a locação do
veículo para o cliente.</li>
<li>3. Realizar devolução: O cliente seleciona seu nome, a cidade de devolução, informa a
quilometragem percorrida e pressiona o botão “Prosseguir”. Nesse instante, o sistema
verifica se o cliente possui alguma locação ativa. Caso afirmativo, o sistema exibe os
dados do veículo alugado, a quantidade de dias contratados, o valor total das diárias
reservadas, o valor referente aos quilômetros rodados, e o valor total a ser pago. O
cliente confere os dados e pressiona o botão “Realizar Devolução”. Então, o sistema
atualiza a cidade e o odômetro do veículo, e o libera para nova locação. Caso o cliente
não tenha locação ativa, o sistema deve mostrar uma mensagem.</li>
<li>4. Consultar locações: Usuário informa o nome de um cliente ou o modelo de um veículo
e o sistema mostra na tela uma tabela com todos os dados dos veículos e das locações
correspondentes, ativas e finalizadas. Nessa mesma tela, deve ser possível exportar a
listagem como arquivo markdown.</li>
<li>5. Resumo: Mostrar na tela um resumo de todas as locações já finalizadas, contendo os
somatórios de km rodados, quantidade de dias reservados, somatório do valor das
diárias, somatório do valor dos km rodados e valor total das locações (diárias + km
rodados).
<ul>
</ul> 


