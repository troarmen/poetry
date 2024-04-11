from flask import Flask, request

# /index
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá Mundo</h1>'

# /contato

@app.route('/contato')
def contato():
    return """
    <h1> Contato </h1>
    <form action="/submissao_form" method="post">
        <label> E-mail</label>
        <br>
        <input type="email" name="email"/> 
        <br>
        <label> Mensagem </label>
        <br>
        <textarea name="mensagem" rows="3">
        </textarea>
        <br><br>
        <button type="submit">Enviar</button>
    </form>
    """


@app.route('/submissao_form', methods=['POST'])
def submissao_form():
    email = request.form['email']
    mensagem = request.form['mensagem']

    # enviar para o admin

    # salvar no banco

    return f"""
    {email}
    {mensagem}
    """