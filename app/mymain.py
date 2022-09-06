from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash

# https://flask.palletsprojects.com/en/2.2.x/quickstart/
# https://cursos.alura.com.br/course/flask-crie-webapp-python/task/102406
# https://flask-ptbr.readthedocs.io/en/latest/
# https://flask.palletsprojects.com/en/2.2.x/tutorial/blog/
# https://github.com/pallets/flask
# DJANGO: https://docs.djangoproject.com/en/4.1/intro/tutorial02/
# https://www.fullstackpython.com/flask.html

app = Flask(__name__, static_folder="static")
app.secret_key = 'my-test'

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    def __str__(self) -> str:
        msg = f'Nome: {self._nome} - Idade: {self._idade}'
        return msg

p1 = Pessoa('marcelo', 33)
p2 = Pessoa('allan', 22)
p3 = Pessoa('bob', 44)
list2 = [p1, p2, p3]    


#@app.route("/inicio")
@app.route("/")
def hello_world():
    mylist = ['oi', 'teste', 'aaaaa', 22222, 44444, True]
    myvars = {
        'titulo': 'Oiii, aqui vai um titulooo!!',
        'mylist': mylist,
        'pessoas': list2
    }


    msg = render_template("inicio.html", **myvars)
    return msg


@app.route("/novo")
def form_novo():
    myvars = {
        'titulo': 'adicionando algum dadoooo!!',
        'rota_criar': '/criar'
    }
    myhtml = render_template('myform.html', **myvars)
    return myhtml


# Flask aceita somente metodo GET.
# precisa informar o POST
@app.route("/criar", methods=['POST'])
def criar_pessoa():
    nome = request.form['nome']
    idade = request.form['idade']
    nova_pessoa = Pessoa(nome, idade)
    #nova_pessoa = Pessoa("myttmp", "475465")
    list2.append(nova_pessoa)
    myvars = {
        'titulo': 'Inseridooooo!!!',
        'myp': nova_pessoa
    }
    #myhtml = render_template('criar_ok.html', **myvars)
    return redirect('/')


@app.route("/login")
def tela_login():
    myvars = {}
    myhtml = render_template('login.html', **myvars)
    return myhtml

@app.route("/autenticar", methods=['POST'])
def fazer_autenticacao():
    # ERRO DE SECRET KEY..
    if request.form['nome'] == 'admin' and request.form['senha'] == 'admin':

        session['usuario'] = request.form['nome']
        session['estah_logado'] = True
        flash('Usuário logado com sucesso!')
        return redirect('/')
    else:
        flash('Erro no login/senha. tente novamente')
        return redirect('/login')

#app.run(debug=True)