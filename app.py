
from flask import Flask, render_template, url_for
app = Flask(__name__)

NAV = [
    {"title":"Home", "endpoint":"index"},
    {"title":"Personagens", "endpoint":"personagens"},
    {"title":"Press Kit", "endpoint":"presskit"},
    {"title":"Contato", "endpoint":"contato"},
]

@app.context_processor
def inject_globals():
    return dict(NAV=NAV, author="Kaioyllan", email="deltaproject144@gmail.com", site_title="Delta-78", site_subtitle="O Passageiro")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personagens')
def personagens():
    # simple data, you can edit images names in /static/img
    chars = [
        {"name":"Miller","role":"Protagonista","bio":"Acorda sozinho na nave e precisa descobrir o que aconteceu.","img": url_for('static', filename='img/Design_sem_nome_(3).png')},
        {"name":"Echo-77","role":"IA de Bordo","bio":"Inteligência artificial com segredos e protocolos questionáveis.","img": url_for('static', filename='img/Design_sem_nome_(4).png')},
        {"name":"Julie Marie","role":"Cientista","bio":"Autora de e-mails SOS; deixou pistas para Miller.","img": url_for('static', filename='img/Design_sem_nome_(1).png')},
    ]
    return render_template('personagens.html', personagens=chars)

@app.route('/presskit')
def presskit():
    return render_template('presskit.html', steam_link="https://store.steampowered.com/app/3715880/Delta_78_O_Passageiro/")

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
