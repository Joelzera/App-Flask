from flask import Flask

app = Flask(__name__)


# Criando a pagina do site

@app.route("/")
def homepage():
    return "Iniciando a criação do site"

@app.route("/contatos")
def contatos():
    return "E-mail: joelbispo04@hotmail.com"




# Colocando o site no ar
if __name__ == "__main__":
    app.run(debug=True)