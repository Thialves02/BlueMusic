from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Musica:
    def __init__(self,nome,artista,link):
        self.nome = nome
        self.artista = artista
        self.link = link

@app.route('/')
def index():
    musica = Musica('SET DJ PEDRO 6.0',
        'MC Don Juan, MC Davi, MC Pedrinho, MC Hariel e MC Ryan SP',
        '')
    return render_template('index.html',musica=musica)

if __name__ == "__main__":
    app.run(debug=True)