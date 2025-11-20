// Script para funcionalidades adicionais do portfólio

// Smooth scroll para links internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Adicionar animação ao scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, {
    threshold: 0.1
});

// Observar cards de projetos
document.querySelectorAll('.project-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s, transform 0.5s';
    observer.observe(card);
});

// Validação do formulário de contato
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const nome = formData.get('nome').trim();
        const email = formData.get('email').trim();
        const assunto = formData.get('assunto').trim();
        const mensagem = formData.get('mensagem').trim();
        
        // Validações básicas
        if (!nome || !email || !assunto || !mensagem) {
            alert('Por favor, preencha todos os campos obrigatórios');
            return;
        }
        
        // Validar email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Por favor, insira um email válido');
            return;
        }
        
        // Enviar formulário
        fetch(this.action || '/contato', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const messageDiv = document.getElementById('formMessage');
            if (data.status === 'sucesso') {
                messageDiv.innerHTML = '<p style="color: green; background-color: #d4edda; padding: 1rem; border-radius: 4px;">✓ ' + data.mensagem + '</p>';
                contactForm.reset();
                
                // Limpar mensagem após 5 segundos
                setTimeout(() => {
                    messageDiv.innerHTML = '';
                }, 5000);
            } else {
                messageDiv.innerHTML = '<p style="color: red; background-color: #f8d7da; padding: 1rem; border-radius: 4px;">✗ Erro ao enviar mensagem</p>';
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            document.getElementById('formMessage').innerHTML = '<p style="color: red; background-color: #f8d7da; padding: 1rem; border-radius: 4px;">✗ Erro na conexão</p>';
        });
    });
}

// Função para formatar data
function formatarData(data) {
    const opcoes = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(data).toLocaleDateString('pt-BR', opcoes);
}

// Adicionar classe ativa ao menu de navegação
function updateActiveNav() {
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-menu a').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath === '/' && href === '/')) {
            link.style.color = 'var(--secondary-color)';
            link.style.fontWeight = 'bold';
        }
    });
}

updateActiveNav();

// Modo noturno (opcional)
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

// Carregar preferência de modo noturno
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
}

// Copiar para clipboard (útil para links)
function copiarParaClipboard(texto) {
    navigator.clipboard.writeText(texto).then(() => {
        alert('Copiado para o clipboard!');
    }).catch(err => {
        console.error('Erro ao copiar:', err);
    });
}

// Contar e exibir número de visitantes (armazenado localmente)
function atualizarContadorVisitas() {
    let visitas = localStorage.getItem('visitasPortfolio') || 0;
    visitas = parseInt(visitas) + 1;
    localStorage.setItem('visitasPortfolio', visitas);
    console.log('Número de visitas: ' + visitas);
}

atualizarContadorVisitas();

// Log de mensagem de boas-vindas no console
console.log('%c🚀 Bem-vindo ao Meu Portfólio!', 'color: #0066cc; font-size: 20px; font-weight: bold;');
console.log('%cVerifique meus projetos e entre em contato comigo!', 'color: #f39c12; font-size: 14px;');