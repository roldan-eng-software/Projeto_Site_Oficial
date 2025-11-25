# Portfolio Landing Page 🚀

Landing page moderna e elegante para divulgação de portfólio de projetos, pronta para hospedar no GitHub Pages.

## ✨ Características

- **Design Moderno**: Gradientes vibrantes, glassmorphism e animações suaves
- **Dark Theme**: Tema escuro elegante e profissional
- **Totalmente Responsivo**: Funciona perfeitamente em desktop, tablet e mobile
- **Animações Interativas**: Micro-interações e efeitos hover
- **SEO Otimizado**: Meta tags e estrutura semântica HTML5
- **Performance**: Código otimizado e carregamento rápido

## 🛠️ Tecnologias

- HTML5
- CSS3 (Variáveis CSS, Flexbox, Grid)
- JavaScript (Vanilla JS)
- Python (servidor de desenvolvimento)
- Google Fonts (Inter)

## 🚀 Como Usar Localmente

### Opção 1: Servidor Python (Recomendado)

```bash
# Executar o servidor de desenvolvimento
python server.py
```

O servidor iniciará em `http://localhost:8000`

### Opção 2: Python HTTP Server Simples

```bash
# Python 3
python -m http.server 8000

# Ou especificar diretório
python -m http.server 8000 --directory .
```

### Opção 3: Abrir Diretamente

Simplesmente abra o arquivo `index.html` no seu navegador.

## 📦 Estrutura de Arquivos

```
Projeto_Site_Oficial/
├── index.html          # Estrutura HTML principal
├── styles.css          # Estilos e design system
├── script.js           # Interações e animações
├── server.py           # Servidor de desenvolvimento
└── README.md           # Este arquivo
```

## 🎨 Personalização

### 1. Informações Pessoais

Edite o arquivo `index.html` e atualize:

- **Nome e título** na seção hero
- **Sobre mim** na seção about
- **Informações de contato** na seção contact

### 2. Projetos do Portfólio

Na seção `#portfolio`, substitua os cards de exemplo pelos seus projetos reais:

```html
<div class="project-card reveal">
    <div class="project-icon">🎯</div>
    <h3>Nome do Projeto</h3>
    <p>Descrição do projeto...</p>
    <div class="project-tags">
        <span class="tag">Tecnologia 1</span>
        <span class="tag">Tecnologia 2</span>
    </div>
    <a href="URL_DO_PROJETO" class="project-link" target="_blank" rel="noopener">
        Acessar Projeto →
    </a>
</div>
```

### 3. Cores e Estilo

Edite as variáveis CSS em `styles.css`:

```css
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --bg-primary: #0a0a0f;
  /* ... outras variáveis */
}
```

### 4. Imagens

Substitua a imagem na seção "Sobre" por uma imagem sua ou do seu trabalho:

```html
<img src="caminho/para/sua/imagem.jpg" alt="Descrição">
```

## 🌐 Deploy no GitHub Pages

### Passo 1: Criar Repositório

1. Crie um novo repositório no GitHub
2. Nome sugerido: `seu-usuario.github.io` (para site principal) ou qualquer nome

### Passo 2: Fazer Upload dos Arquivos

```bash
# Inicializar repositório Git
git init

# Adicionar arquivos
git add .

# Commit
git commit -m "Initial commit: Portfolio landing page"

# Adicionar remote
git remote add origin https://github.com/seu-usuario/seu-repositorio.git

# Push para GitHub
git branch -M main
git push -u origin main
```

### Passo 3: Ativar GitHub Pages

1. Vá para **Settings** do repositório
2. Navegue até **Pages** no menu lateral
3. Em **Source**, selecione a branch `main` e pasta `/ (root)`
4. Clique em **Save**
5. Aguarde alguns minutos e seu site estará disponível em:
   - `https://seu-usuario.github.io/seu-repositorio/`
   - Ou `https://seu-usuario.github.io/` (se o repo for `seu-usuario.github.io`)

## 📱 Seções da Landing Page

### Hero
- Título impactante
- Subtítulo e descrição
- Botões de call-to-action

### Sobre
- Apresentação pessoal
- Habilidades e expertise
- Imagem/foto

### Portfólio
- Grid de projetos
- Cards com descrição
- Links para projetos em produção
- Tags de tecnologias

### Contato
- Email
- LinkedIn
- GitHub
- Outras redes sociais

## 🎯 Recursos Implementados

- ✅ Design responsivo mobile-first
- ✅ Navegação suave entre seções
- ✅ Menu mobile com hamburger
- ✅ Animações de scroll reveal
- ✅ Efeitos parallax
- ✅ Hover effects nos cards
- ✅ Glassmorphism nos elementos
- ✅ Gradientes modernos
- ✅ Tipografia profissional
- ✅ SEO otimizado

## 🔧 Customizações Avançadas

### Adicionar Mais Projetos

Copie e cole um card existente dentro de `.portfolio-grid` e personalize.

### Mudar Fonte

Substitua a importação do Google Fonts no `<head>` do `index.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=SuaFonte:wght@400;700&display=swap" rel="stylesheet">
```

E atualize em `styles.css`:

```css
body {
  font-family: 'SuaFonte', sans-serif;
}
```

### Adicionar Formulário de Contato

Para adicionar um formulário funcional, você pode usar serviços como:
- [Formspree](https://formspree.io/)
- [Netlify Forms](https://www.netlify.com/products/forms/)
- [EmailJS](https://www.emailjs.com/)

## 📄 Licença

Este projeto é livre para uso pessoal e comercial.

## 🤝 Contribuições

Sinta-se à vontade para fazer fork, modificar e melhorar!

## 📞 Suporte

Se tiver dúvidas ou problemas, abra uma issue no repositório.

---

**Desenvolvido com ❤️ e código**
