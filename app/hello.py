from flask import Flask, render_template

# https://flask.palletsprojects.com/en/2.2.x/quickstart/
# https://cursos.alura.com.br/course/flask-crie-webapp-python/task/102406
# https://flask-ptbr.readthedocs.io/en/latest/
# https://flask.palletsprojects.com/en/2.2.x/tutorial/blog/
# https://github.com/pallets/flask
# DJANGO: https://docs.djangoproject.com/en/4.1/intro/tutorial02/
# https://www.fullstackpython.com/flask.html

app = Flask(__name__)

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

@app.route("/inicio")
def hello_world():
    p1 = Pessoa('marcelo', 33)
    p2 = Pessoa('allan', 22)
    p3 = Pessoa('bob', 44)
    list2 = [p1, p2, p3]    
    mylist = ['oi', 'teste', 'aaaaa', 22222, 44444, True]
    myvars = {
        'titulo': 'Oiii, aqui vai um titulooo!!',
        'mylist': mylist,
        'pessoas': list2
    }


    msg = render_template("mytemplate.html", **myvars)
    return msg


@app.route("/novo")
def form_novo():
    pass


@app.route("/criar")
def criar_pessoa():
    pass



#app.run()