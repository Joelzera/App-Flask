from flask import Flask

app = Flask(__name__)


# Criando a pagina do site

@app.route("/")
def homepage():
    return "Iniciando a criação do site"




# Colocando o site no ar
app.run()