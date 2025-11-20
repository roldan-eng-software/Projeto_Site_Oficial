from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-mude-em-producao')

db = SQLAlchemy(app)

# Modelo de Projeto
class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    tecnologias = db.Column(db.String(255), nullable=False)
    link_github = db.Column(db.String(255))
    link_demo = db.Column(db.String(255))
    imagem = db.Column(db.String(255), default='default.jpg')
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    destaque = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Projeto {self.titulo}>'

# Modelo de Contato
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    assunto = db.Column(db.String(255), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    data_envio = db.Column(db.DateTime, default=datetime.now)
    lido = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Contato de {self.nome}>'

# Criar tabelas
with app.app_context():
    db.create_all()

# Rotas
@app.route('/')
def inicio():
    projetos_destaque = Projeto.query.filter_by(destaque=True).limit(3).all()
    return render_template('index.html', projetos=projetos_destaque)

@app.route('/portfolio')
def portfolio():
    pagina = request.args.get('pagina', 1, type=int)
    projetos = Projeto.query.order_by(Projeto.data_criacao.desc()).paginate(page=pagina, per_page=6)
    return render_template('portfolio.html', projetos=projetos)

@app.route('/projeto/<int:id>')
def projeto_detalhe(id):
    projeto = Projeto.query.get_or_404(id)
    return render_template('projeto_detalhe.html', projeto=projeto)

@app.route('/sobre')
def sobre():
    total_projetos = Projeto.query.count()
    return render_template('sobre.html', total_projetos=total_projetos)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        contato_novo = Contato(
            nome=request.form['nome'],
            email=request.form['email'],
            assunto=request.form['assunto'],
            mensagem=request.form['mensagem']
        )
        db.session.add(contato_novo)
        db.session.commit()
        return jsonify({'status': 'sucesso', 'mensagem': 'Mensagem enviada com sucesso!'})
    return render_template('contato.html')

@app.route('/admin/projetos', methods=['GET', 'POST'])
def admin_projetos():
    if request.method == 'POST':
        novo_projeto = Projeto(
            titulo=request.form['titulo'],
            descricao=request.form['descricao'],
            tecnologias=request.form['tecnologias'],
            link_github=request.form.get('link_github', ''),
            link_demo=request.form.get('link_demo', ''),
            destaque=request.form.get('destaque') == 'on'
        )
        db.session.add(novo_projeto)
        db.session.commit()
        return redirect(url_for('admin_projetos'))
    
    projetos = Projeto.query.all()
    return render_template('admin_projetos.html', projetos=projetos)

@app.route('/admin/projeto/<int:id>/editar', methods=['GET', 'POST'])
def editar_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    if request.method == 'POST':
        projeto.titulo = request.form['titulo']
        projeto.descricao = request.form['descricao']
        projeto.tecnologias = request.form['tecnologias']
        projeto.link_github = request.form.get('link_github', '')
        projeto.link_demo = request.form.get('link_demo', '')
        projeto.destaque = request.form.get('destaque') == 'on'
        db.session.commit()
        return redirect(url_for('admin_projetos'))
    return render_template('editar_projeto.html', projeto=projeto)

@app.route('/admin/projeto/<int:id>/deletar', methods=['POST'])
def deletar_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    db.session.delete(projeto)
    db.session.commit()
    return redirect(url_for('admin_projetos'))

@app.route('/admin/mensagens')
def admin_mensagens():
    mensagens = Contato.query.order_by(Contato.data_envio.desc()).all()
    return render_template('admin_mensagens.html', mensagens=mensagens)

if __name__ == '__main__':
    app.run(debug=True)