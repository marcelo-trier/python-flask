from flask import Flask, render_template

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

#app.run()