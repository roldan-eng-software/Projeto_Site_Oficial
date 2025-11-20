# Portfólio de Projetos - Guia Completo

Um portfólio web moderno e responsivo desenvolvido com Python e Flask para divulgação de seus projetos.

## 📋 Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🚀 Instalação Rápida

### 1. Clonar ou criar o projeto

```bash
mkdir portfolio
cd portfolio
```

### 2. Criar ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Criar estrutura de pastas

```bash
mkdir templates
mkdir static
mkdir static/css
mkdir static/js
mkdir static/images
```

### 5. Copiar os arquivos

- Copie `app.py` para a raiz do projeto
- Copie os arquivos HTML em `templates/`
- Copie `style.css` em `static/css/`
- Copie `script.js` em `static/js/`
- Copie `.env` para a raiz

### 6. Executar a aplicação

```bash
python app.py
```

A aplicação estará disponível em: **http://localhost:5000**

## 📁 Estrutura do Projeto

```
portfolio/
├── app.py                          # Aplicação Flask principal
├── requirements.txt                # Dependências Python
├── .env                           # Variáveis de ambiente
├── portfolio.db                   # Banco de dados (criado automaticamente)
├── templates/                     # Templates HTML
│   ├── base.html                 # Template base
│   ├── index.html                # Homepage
│   ├── portfolio.html            # Galeria de projetos
│   ├── projeto_detalhe.html      # Detalhes do projeto
│   ├── sobre.html                # Página sobre
│   ├── contato.html              # Página de contato
│   ├── admin_projetos.html       # Painel admin - projetos
│   ├── editar_projeto.html       # Editar projeto
│   └── admin_mensagens.html      # Painel admin - mensagens
└── static/                        # Arquivos estáticos
    ├── css/
    │   └── style.css             # Estilos CSS
    ├── js/
    │   └── script.js             # Scripts JavaScript
    └── images/                   # Imagens dos projetos
        └── default.jpg           # Imagem padrão
```

## 🎨 Funcionalidades

### Para Visitantes
- ✅ Homepage atrativa com projetos em destaque
- ✅ Galeria de projetos com paginação
- ✅ Página de detalhes de cada projeto
- ✅ Página "Sobre" com informações e habilidades
- ✅ Formulário de contato funcional
- ✅ Design responsivo (mobile, tablet, desktop)

### Para Administrador
- ✅ Painel de gerenciamento de projetos
- ✅ Criar, editar e deletar projetos
- ✅ Marcar projetos como destaque
- ✅ Visualizar mensagens de contato recebidas
- ✅ Interface intuitiva e fácil de usar

## 🔧 Configuração

### 1. Variáveis de Ambiente (.env)

Edite o arquivo `.env` com suas informações:

```ini
SECRET_KEY=sua-chave-secreta-aqui
FLASK_ENV=development
FLASK_DEBUG=True
SITE_NAME=Meu Portfólio
AUTHOR_NAME=Seu Nome
AUTHOR_EMAIL=seu@email.com
```

### 2. Adicionar Imagens dos Projetos

Coloque as imagens dos seus projetos em `static/images/` com nomes como:
- `projeto1.jpg`
- `projeto2.png`
- etc.

### 3. Customizar Cores

No arquivo `static/css/style.css`, procure por `:root` e altere as cores:

```css
:root {
    --primary-color: #0066cc;      /* Cor principal */
    --secondary-color: #f39c12;    /* Cor secundária */
    --danger-color: #e74c3c;       /* Cor de alerta */
    --success-color: #27ae60;      /* Cor de sucesso */
    --dark-color: #2c3e50;         /* Cor escura */
}
```

## 📊 Usando a Aplicação

### Como Adicionar um Projeto

1. Acesse: `http://localhost:5000/admin/projetos`
2. Preencha o formulário:
   - **Título**: Nome do projeto
   - **Descrição**: Descrição detalhada
   - **Tecnologias**: Separadas por vírgula (ex: Python, Flask, SQLite)
   - **Link GitHub**: URL do repositório (opcional)
   - **Link Demo**: URL da demonstração (opcional)
   - **Destacar**: Marque para aparecer na homepage
3. Clique em "Adicionar Projeto"

### Ver Mensagens de Contato

1. Acesse: `http://localhost:5000/admin/mensagens`
2. Visualize todas as mensagens recebidas
3. Clique em "Responder" para enviar um email

## 🌐 Deploy (Hospedagem)

### Opção 1: Heroku (Gratuito com limitações)

```bash
# Instalar Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Criar app
heroku create seu-nome-app

# Configurar variáveis de ambiente
heroku config:set SECRET_KEY=sua-chave-secreta

# Deploy
git push heroku main
```

### Opção 2: PythonAnywhere

1. Acesse: https://www.pythonanywhere.com/
2. Upload seu código
3. Configure o WSGI
4. Seu site estará online!

### Opção 3: DigitalOcean / AWS / Google Cloud

Use um servidor virtual e instale Flask normalmente.

## 🔐 Segurança em Produção

Antes de fazer deploy:

1. Altere `FLASK_DEBUG=False` no `.env`
2. Gere uma `SECRET_KEY` forte
3. Use um servidor WSGI (gunicorn):
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```
4. Configure um banco de dados robusto (PostgreSQL recomendado)
5. Use HTTPS (SSL/TLS)

## 📚 Aprendizado com Python

Este projeto ensina:

- ✅ Criação de aplicações web com Flask
- ✅ Modelos de banco de dados com SQLAlchemy ORM
- ✅ Rotas e views em web frameworks
- ✅ Templates HTML com Jinja2
- ✅ Formulários HTML e validação
- ✅ Manipulação de banco de dados (CRUD)
- ✅ CSS responsivo e moderno
- ✅ JavaScript para interatividade
- ✅ Variáveis de ambiente com dotenv
- ✅ Deploy de aplicações Python

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Erro: "Address already in use"
Mude a porta em `app.py`:
```python
app.run(debug=True, port=5001)
```

### Banco de dados não está sendo criado
Verifique se a pasta do projeto tem permissão de escrita.

## 📞 Suporte

Se tiver dúvidas, consulte:
- [Documentação Flask](https://flask.palletsprojects.com/)
- [Documentação SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentação Jinja2](https://jinja.palletsprojects.com/)

## 📝 Licença

Este projeto é de código aberto e pode ser usado livremente.

---

**Desenvolvido com ❤️ usando Python e Flask**