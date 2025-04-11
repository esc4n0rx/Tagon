#!/usr/bin/env python3
import os
import sys
import argparse
import shutil
from pathlib import Path
import subprocess

BANNER = """
┌────────────────────────────────────────────┐
│                                            │
│   ████████╗ █████╗  ██████╗  ██████╗ ███╗   ██╗   │
│   ╚══██╔══╝██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║   │
│      ██║   ███████║██║  ███╗██║   ██║██╔██╗ ██║   │
│      ██║   ██╔══██║██║   ██║██║   ██║██║╚██╗██║   │
│      ██║   ██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║   │
│      ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   │
│                                            │
│  O framework web reativo 100% em Python    │
│                                            │
└────────────────────────────────────────────┘
"""

# Templates para arquivos básicos
LAYOUT_TEMPLATE = """def layout(content):
    html = content if isinstance(content, str) else content.get("html", "")
    css = "" if isinstance(content, str) else content.get("css", "")

    # CSS global com tema escuro e animações
    global_css = \"\"\"
        :root {
            --primary: #10B981;
            --secondary: #8B5CF6;
            --text-color: #E2E8F0;
            --bg-color: #0F172A;
            --card-bg: #1E293B;
            --radius: 8px;
            --glow-color: rgba(139, 92, 246, 0.6);
        }

        @keyframes glow {
            0% {
                text-shadow: 0 0 10px var(--glow-color);
            }
            50% {
                text-shadow: 0 0 20px var(--glow-color), 0 0 30px var(--glow-color);
            }
            100% {
                text-shadow: 0 0 10px var(--glow-color);
            }
        }
        
        @keyframes slideGlow {
            0% {
                background-position: -100% 0;
            }
            100% {
                background-position: 200% 0;
            }
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
            min-height: 100vh;
        }

        .layout {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        .navbar {
            background-color: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(10px);
            color: white;
            padding: 1rem 2rem;
            font-weight: bold;
            font-size: 1.25rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            align-items: center;
        }
        
        .navbar-brand {
            font-size: 1.5rem;
            font-weight: 700;
            position: relative;
            background: linear-gradient(90deg, 
                              transparent, 
                              rgba(139, 92, 246, 0.7), 
                              transparent);
            background-size: 200% 100%;
            -webkit-background-clip: text;
            background-clip: text;
            color: white;
            animation: slideGlow 3s infinite;
            display: inline-block;
        }
        
        .navbar-brand span {
            animation: glow 2s infinite;
        }
        
        .navbar-rocket {
            display: inline-block;
            margin-left: 5px;
            transform-origin: center;
            animation: rocketMove 3s infinite;
        }
        
        @keyframes rocketMove {
            0% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-3px) rotate(5deg); }
            100% { transform: translateY(0) rotate(0deg); }
        }

        .content {
            flex: 1;
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
            box-sizing: border-box;
        }
        
        /* Botões */
        .btn {
            transition: all 0.3s ease;
            transform: translateY(0);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        
        /* Cards e elementos */
        .card {
            background-color: var(--card-bg);
            border-radius: var(--radius);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
        }
    \"\"\"

    return f\"\"\"
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Tagon</title>
        <style>
            {global_css}
            {css}
        </style>
    </head>
    <body>
        <div class="layout">
            <nav class="navbar">
                <div class="navbar-brand"><span>Tagon</span> <span class="navbar-rocket">🚀</span></div>
            </nav>
            <main class="content">{html}</main>
        </div>
    </body>
    </html>
    \"\"\"
"""

INDEX_TEMPLATE = """def main():
    return {
        "html": \"\"\"
            <div class="home-container">
                <h1 class="title">Tagon <span class="atom">⚛️</span></h1>
                <p class="desc">O framework web reativo 100% em Python.</p>
                
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🐍</div>
                        <h3>100% Python</h3>
                        <p>Desenvolva aplicações web completas usando apenas Python</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">🎨</div>
                        <h3>CSS Isolado</h3>
                        <p>Cada componente com seu próprio escopo de estilos</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">⚡</div>
                        <h3>Reativo</h3>
                        <p>Interface dinâmica e responsiva para seus usuários</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">🚀</div>
                        <h3>Simples</h3>
                        <p>API intuitiva e fácil de aprender</p>
                    </div>
                </div>
                
                <a href="/HelloWorld" class="btn">Ver exemplo</a>
            </div>
        \"\"\",
        "css": \"\"\"
            .home-container {
                text-align: center;
                padding: 3rem 1rem;
                animation: fadeIn 0.8s ease-out;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .title {
                font-size: 4rem;
                font-weight: 800;
                background: linear-gradient(45deg, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                margin-bottom: 1rem;
                position: relative;
                display: inline-block;
            }
            
            .title::after {
                content: '';
                position: absolute;
                bottom: -10px;
                left: 50%;
                width: 40%;
                height: 4px;
                background: linear-gradient(90deg, var(--primary), var(--secondary));
                transform: translateX(-50%);
                border-radius: 2px;
            }
            
            .atom {
                display: inline-block;
                animation: spin 10s linear infinite;
                margin-left: 10px;
            }
            
            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
            
            .desc {
                font-size: 1.5rem;
                color: var(--text-color);
                opacity: 0.9;
                margin-bottom: 3rem;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 2rem;
                margin: 3rem 0;
            }
            
            .feature-card {
                background: rgba(30, 41, 59, 0.5);
                border-radius: var(--radius);
                padding: 2rem;
                border: 1px solid rgba(255, 255, 255, 0.1);
                transition: all 0.3s ease;
            }
            
            .feature-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
                border-color: rgba(var(--secondary), 0.4);
            }
            
            .feature-icon {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            
            .feature-card h3 {
                font-size: 1.5rem;
                margin-bottom: 0.5rem;
                color: var(--primary);
            }
            
            .feature-card p {
                opacity: 0.8;
                line-height: 1.6;
            }
            
            .btn {
                padding: 1rem 2.5rem;
                background: linear-gradient(45deg, var(--primary), var(--secondary));
                border-radius: var(--radius);
                color: white;
                text-decoration: none;
                display: inline-block;
                margin-top: 2rem;
                font-weight: 600;
                letter-spacing: 0.5px;
                transition: all 0.3s ease;
                box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.2);
            }
            
            .btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 20px 25px -5px rgba(16, 185, 129, 0.4);
            }
        \"\"\"
    }
"""

HELLO_WORLD_TEMPLATE = """def main():
    return {
        "html": \"\"\"
            <div class="hello-container">
                <div class="breadcrumbs">
                    <a href="/">Home</a> <span class="separator">/</span> <span class="current">Hello World</span>
                </div>
                
                <h1 class="hello-title">Hello World!</h1>
                <p class="hello-text">Este é um exemplo de componente no Tagon Framework.</p>
                
                <div class="card">
                    <div class="card-header">
                        <h3>Características do Tagon</h3>
                    </div>
                    <div class="card-body">
                        <ul class="features-list">
                            <li class="feature-item">
                                <span class="feature-icon">🐍</span>
                                <span class="feature-text">100% Python</span>
                            </li>
                            <li class="feature-item">
                                <span class="feature-icon">🎨</span>
                                <span class="feature-text">CSS isolado por componente</span>
                            </li>
                            <li class="feature-item">
                                <span class="feature-icon">⚡</span>
                                <span class="feature-text">Estrutura reativa</span>
                            </li>
                            <li class="feature-item">
                                <span class="feature-icon">📚</span>
                                <span class="feature-text">Fácil de aprender</span>
                            </li>
                        </ul>
                    </div>
                </div>
                
                <div class="code-example">
                    <div class="code-header">
                        <span>Exemplo de componente</span>
                    </div>
                    <pre class="code-block"><code>def hello_world():
    return {
        "html": \"\"\"
            <h1>Hello World!</h1>
            <p>Meu primeiro componente Tagon.</p>
        \"\"\",
        "css": \"\"\"
            h1 { color: var(--primary); }
            p { color: var(--text-color); }
        \"\"\"
    }</code></pre>
                </div>
                
                <a href="/" class="back-btn">
                    <span class="btn-icon">←</span>
                    <span class="btn-text">Voltar</span>
                </a>
            </div>
        \"\"\",
        "css": \"\"\"
            .hello-container {
                max-width: 800px;
                margin: 0 auto;
                padding: 1rem;
                animation: slideUp 0.6s ease-out;
            }
            
            @keyframes slideUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .breadcrumbs {
                display: flex;
                align-items: center;
                margin-bottom: 2rem;
                font-size: 0.9rem;
                opacity: 0.7;
            }
            
            .breadcrumbs a {
                color: var(--secondary);
                text-decoration: none;
                transition: color 0.3s;
            }
            
            .breadcrumbs a:hover {
                color: var(--primary);
            }
            
            .separator {
                margin: 0 0.5rem;
            }
            
            .current {
                font-weight: 500;
            }
            
            .hello-title {
                font-size: 3.5rem;
                background: linear-gradient(to right, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                margin-bottom: 1rem;
                text-align: center;
            }
            
            .hello-text {
                font-size: 1.2rem;
                text-align: center;
                margin-bottom: 3rem;
                color: var(--text-color);
                opacity: 0.9;
            }
            
            .card {
                background: var(--card-bg);
                border-radius: var(--radius);
                overflow: hidden;
                margin-bottom: 3rem;
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
                border: 1px solid rgba(255, 255, 255, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
            }
            
            .card-header {
                padding: 1.5rem;
                background: linear-gradient(45deg, var(--primary), var(--secondary));
                color: white;
            }
            
            .card-header h3 {
                margin: 0;
                font-size: 1.5rem;
            }
            
            .card-body {
                padding: 1.5rem;
            }
            
            .features-list {
                list-style: none;
                padding: 0;
                margin: 0;
            }
            
            .feature-item {
                display: flex;
                align-items: center;
                margin-bottom: 1rem;
                padding: 0.75rem;
                border-radius: var(--radius);
                transition: background 0.3s ease;
            }
            
            .feature-item:hover {
                background: rgba(255, 255, 255, 0.05);
            }
            
            .feature-icon {
                font-size: 1.5rem;
                margin-right: 1rem;
            }
            
            .feature-text {
                font-size: 1.1rem;
            }
            
            .code-example {
                margin-bottom: 3rem;
                border-radius: var(--radius);
                overflow: hidden;
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
            }
            
            .code-header {
                background: rgba(16, 185, 129, 0.1);
                padding: 0.75rem 1.5rem;
                border-bottom: 1px solid rgba(16, 185, 129, 0.2);
                color: var(--primary);
                font-weight: 500;
            }
            
            .code-block {
                margin: 0;
                padding: 1.5rem;
                background: rgba(15, 23, 42, 0.9);
                overflow-x: auto;
                font-family: monospace;
                font-size: 0.9rem;
                line-height: 1.5;
            }
            
            code {
                color: var(--text-color);
            }
            
            .back-btn {
                display: inline-flex;
                align-items: center;
                background: var(--primary);
                color: white;
                text-decoration: none;
                padding: 0.75rem 1.5rem;
                border-radius: var(--radius);
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            
            .back-btn:hover {
                transform: translateX(-5px);
                background: var(--secondary);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
            }
            
            .btn-icon {
                margin-right: 0.5rem;
                font-size: 1.2rem;
                transition: transform 0.3s ease;
            }
            
            .back-btn:hover .btn-icon {
                transform: translateX(-3px);
            }
        \"\"\"
    }
"""

RUN_TEMPLATE = """from tagon.server import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
"""

ROUTER_TEMPLATE = """import os
import importlib.util
from flask import render_template_string
from src.layout import layout

PAGES_DIR = "src/pages"

def register_routes(app):
    for filename in os.listdir(PAGES_DIR):
        if filename.endswith(".py"):
            route_name = "/" if filename == "index.py" else f"/{filename[:-3]}"
            module_path = os.path.join(PAGES_DIR, filename)
            
            # Gerando um nome de endpoint único baseado no nome do arquivo
            endpoint_name = filename[:-3].lower().replace('.', '_')
            if endpoint_name == "index":
                endpoint_name = "home"

            spec = importlib.util.spec_from_file_location("page", module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "main"):
                # Usando o nome do arquivo como parte da função para torná-la única
                def route_factory(component_func, page_name):
                    def render_page():
                        return render_template_string(layout(component_func()))
                    # Renomeando a função para um nome único
                    render_page.__name__ = f"render_{page_name}"
                    return render_page
                
                # Criando uma função com nome único para cada rota
                page_name = filename[:-3].lower()
                handler = route_factory(module.main, page_name)
                
                # Registrando a rota com endpoint único
                app.add_url_rule(
                    route_name, 
                    endpoint=f"render_{page_name}", 
                    view_func=handler
                )
"""

SERVER_TEMPLATE = """from flask import Flask
from tagon.router import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app
"""

INIT_TEMPLATE = """# Tagon Framework
# O framework web reativo 100% em Python
"""

REQUIREMENTS_TEMPLATE = """flask>=2.0.0
"""

README_TEMPLATE = """# Tagon Framework 🚀

Tagon é um framework web reativo 100% em Python, inspirado em React, mas utilizando apenas Python para criar aplicações web modernas e reativas.

## ✨ Características

- **100% Python**: Desenvolva aplicações web completas usando apenas Python
- **CSS Isolado**: Cada componente com seu próprio escopo de estilos
- **Reativo**: Interface dinâmica e responsiva para seus usuários
- **Simples**: API intuitiva e fácil de aprender
- **Zero Dependências Frontend**: Não requer Node.js, npm ou pacotes JavaScript

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/tagon.git
cd tagon

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python run.py
```

Acesse `http://localhost:5000` para ver a aplicação em funcionamento.

## 📋 Pré-requisitos

- Python 3.7+
- Flask

## 🔧 Estrutura do Projeto

```
tagon/
├── src/
│   ├── pages/
│   │   ├── index.py
│   │   ├── HelloWorld.py
│   │   └── ... (suas páginas)
│   └── layout.py
├── tagon/
│   ├── router.py
│   └── server.py
├── run.py
└── requirements.txt
```

## 📝 Como Usar

### Criando uma Página

Crie um arquivo Python em `src/pages/` com uma função `main()` que retorna um dicionário contendo `html` e `css`:

```python
def main():
    return {
        "html": \"\"\"
            <div>
                <h1>Minha Página</h1>
                <p>Conteúdo da página</p>
            </div>
        \"\"\",
        "css": \"\"\"
            h1 { color: var(--primary); }
            p { color: var(--text-color); }
        \"\"\"
    }
```

### Como as Rotas Funcionam

- O arquivo `index.py` é acessado na rota `/`
- Outros arquivos são acessados na rota `/{nome_do_arquivo}`
- Por exemplo, `HelloWorld.py` é acessado em `/HelloWorld`

## 📜 Licença

Distribuído sob a licença MIT.

---

<div align="center">
  <p>Feito com ❤️ em Python</p>
</div>
"""

def print_color(text, color=None):
    """Imprime texto colorido no terminal."""
    colors = {
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'red': '\033[91m',
        'bold': '\033[1m',
        'end': '\033[0m'
    }
    
    start_color = colors.get(color, '')
    end_color = colors['end'] if color else ''
    print(f"{start_color}{text}{end_color}")

def print_progress(message):
    """Imprime uma mensagem de progresso."""
    print_color(f"🚀 {message}", 'cyan')

def create_file(path, content):
    """Cria um arquivo com o conteúdo fornecido."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print_color(f"✅ Criado: {path}", 'green')

def create_directory(path):
    """Cria um diretório se ele não existir."""
    if not os.path.exists(path):
        os.makedirs(path)
        print_color(f"📁 Criado: {path}", 'blue')
    else:
        print_color(f"📁 Já existe: {path}", 'yellow')

def create_project_structure(project_name, template="dark"):
    """Cria a estrutura básica do projeto Tagon."""
    base_dir = os.path.join(os.getcwd(), project_name)
    
    # Cria diretórios
    create_directory(base_dir)
    create_directory(os.path.join(base_dir, "src"))
    create_directory(os.path.join(base_dir, "src", "pages"))
    create_directory(os.path.join(base_dir, "tagon"))
    
    # Cria arquivos principais
    create_file(os.path.join(base_dir, "run.py"), RUN_TEMPLATE)
    create_file(os.path.join(base_dir, "requirements.txt"), REQUIREMENTS_TEMPLATE)
    create_file(os.path.join(base_dir, "README.md"), README_TEMPLATE)
    
    # Cria arquivos do framework
    create_file(os.path.join(base_dir, "tagon", "__init__.py"), INIT_TEMPLATE)
    create_file(os.path.join(base_dir, "tagon", "router.py"), ROUTER_TEMPLATE)
    create_file(os.path.join(base_dir, "tagon", "server.py"), SERVER_TEMPLATE)
    
    # Cria arquivos da aplicação
    create_file(os.path.join(base_dir, "src", "layout.py"), LAYOUT_TEMPLATE)
    create_file(os.path.join(base_dir, "src", "pages", "index.py"), INDEX_TEMPLATE)
    create_file(os.path.join(base_dir, "src", "pages", "HelloWorld.py"), HELLO_WORLD_TEMPLATE)
    
    return base_dir

def initialize_git(project_dir):
    """Inicializa um repositório Git."""
    try:
        current_dir = os.getcwd()
        os.chdir(project_dir)
        
        # Inicializa o Git
        subprocess.run(["git", "init", "-q"], check=True)
        
        # Cria .gitignore
        gitignore_content = """# Arquivos Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Ambientes virtuais
venv/
ENV/
env/

# Configurações de IDE
.idea/
.vscode/
*.swp
*.swo

# Arquivos de sistema
.DS_Store
Thumbs.db
"""
        create_file(os.path.join(project_dir, ".gitignore"), gitignore_content)
        
        # Faz o commit inicial
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Inicialização do projeto Tagon", "-q"], check=True)
        
        os.chdir(current_dir)
        print_color("🎉 Repositório Git inicializado com commit inicial", 'green')
        return True
    except Exception as e:
        print_color(f"⚠️ Não foi possível inicializar o Git: {str(e)}", 'yellow')
        return False

def install_dependencies(project_dir):
    """Instala as dependências do projeto."""
    try:
        current_dir = os.getcwd()
        os.chdir(project_dir)
        
        print_color("📦 Instalando dependências...", 'cyan')
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        
        os.chdir(current_dir)
        print_color("✅ Dependências instaladas com sucesso", 'green')
        return True
    except Exception as e:
        print_color(f"⚠️ Não foi possível instalar as dependências: {str(e)}", 'red')
        return False

def print_next_steps(project_name):
    """Imprime os próximos passos para o usuário."""
    print_color("\n🎉 Projeto Tagon criado com sucesso! 🎉\n", 'green')
    print_color("Próximos passos:", 'blue')
    print_color(f"  1. cd {project_name}", 'bold')
    print_color("  2. python run.py", 'bold')
    print_color("  3. Abra http://localhost:5000 no navegador\n", 'bold')
    
    print_color("Para criar uma nova página:", 'blue')
    print_color(f"  1. Crie um arquivo em src/pages/", 'bold')
    print_color("  2. Defina uma função main() que retorne um dicionário com 'html' e 'css'", 'bold')
    print_color("  3. Acesse sua página em http://localhost:5000/NomeDaSuaPagina\n", 'bold')
    
    print_color("Documentação: https://github.com/seu-usuario/tagon", 'magenta')
    print_color("Divirta-se criando com o Tagon! 💖\n", 'cyan')

def create_custom_page(project_dir, page_name):
    """Cria uma página personalizada."""
    page_path = os.path.join(project_dir, "src", "pages", f"{page_name}.py")
    
    if os.path.exists(page_path):
        print_color(f"⚠️ A página {page_name} já existe!", 'yellow')
        return False
    
    page_content = f"""def main():
    return {{
        "html": \"\"\"
            <div class="page-container">
                <h1 class="page-title">{page_name}</h1>
                <p class="page-description">Sua nova página Tagon</p>
                
                <div class="content-area">
                    <p>Edite este arquivo para customizar sua página.</p>
                </div>
                
                <a href="/" class="back-btn">
                    <span class="btn-icon">←</span>
                    <span class="btn-text">Voltar</span>
                </a>
            </div>
        \"\"\",
        "css": \"\"\"
            .page-container {{
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem 1rem;
                animation: fadeIn 0.6s ease-out;
            }}
            
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            
            .page-title {{
                font-size: 3rem;
                background: linear-gradient(to right, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                margin-bottom: 1rem;
                text-align: center;
            }}
            
            .page-description {{
                font-size: 1.2rem;
                text-align: center;
                margin-bottom: 3rem;
                opacity: 0.8;
            }}
            
            .content-area {{
                background: var(--card-bg);
                border-radius: var(--radius);
                padding: 2rem;
                margin-bottom: 2rem;
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            
            .back-btn {{
                display: inline-flex;
                align-items: center;
                background: var(--primary);
                color: white;
                text-decoration: none;
                padding: 0.75rem 1.5rem;
                border-radius: var(--radius);
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            
            .back-btn:hover {{
                transform: translateX(-5px);
                background: var(--secondary);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
            }}
            
            .btn-icon {{
                margin-right: 0.5rem;
                font-size: 1.2rem;
                transition: transform 0.3s ease;
            }}
            
            .back-btn:hover .btn-icon {{
                transform: translateX(-3px);
            }}
        \"\"\"
    }}
"""
    
    create_file(page_path, page_content)
    print_color(f"🎉 Página {page_name} criada com sucesso!", 'green')
    print_color(f"   Acesse em: http://localhost:5000/{page_name}", 'cyan')
    return True

def main():
    """Função principal do CLI."""
    parser = argparse.ArgumentParser(description='Tagon - O framework web reativo 100% em Python')
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')
    
    # Comando create
    create_parser = subparsers.add_parser('create', help='Cria um novo projeto Tagon')
    create_parser.add_argument('project_name', help='Nome do projeto')
    create_parser.add_argument('--template', choices=['dark', 'light'], default='dark', help='Tema do projeto (padrão: dark)')
    create_parser.add_argument('--git', action='store_true', help='Inicializa um repositório Git')
    create_parser.add_argument('--install', action='store_true', help='Instala as dependências automaticamente')
    
    # Comando page
    page_parser = subparsers.add_parser('page', help='Cria uma nova página')
    page_parser.add_argument('page_name', help='Nome da página')
    page_parser.add_argument('--project', default='.', help='Diretório do projeto (padrão: diretório atual)')
    
    # Comando run
    run_parser = subparsers.add_parser('run', help='Executa o projeto')
    run_parser.add_argument('--project', default='.', help='Diretório do projeto (padrão: diretório atual)')
    run_parser.add_argument('--port', type=int, default=5000, help='Porta para executar o servidor (padrão: 5000)')
    
    # Comando info
    info_parser = subparsers.add_parser('info', help='Exibe informações sobre o Tagon')
    
    args = parser.parse_args()
    
    # Se nenhum comando for especificado, exibir o banner e a ajuda
    if not args.command:
        print(BANNER)
        parser.print_help()
        return
    
    # Comando create
    if args.command == 'create':
        print(BANNER)
        print_color(f"Criando projeto Tagon: {args.project_name}", 'blue')
        project_dir = create_project_structure(args.project_name, args.template)
        
        if args.git:
            initialize_git(project_dir)
        
        if args.install:
            install_dependencies(project_dir)
        
        print_next_steps(args.project_name)
    
    # Comando page
    elif args.command == 'page':
        project_dir = os.path.abspath(args.project)
        if not os.path.exists(os.path.join(project_dir, "src", "pages")):
            print_color("⚠️ Diretório do projeto Tagon não encontrado!", 'red')
            print_color("Certifique-se de estar no diretório raiz do projeto ou use --project para especificar o caminho.", 'yellow')
            return
        
        create_custom_page(project_dir, args.page_name)
    
    # Comando run
    elif args.command == 'run':
        project_dir = os.path.abspath(args.project)
        run_script = os.path.join(project_dir, "run.py")
        
        if not os.path.exists(run_script):
            print_color("⚠️ Arquivo run.py não encontrado!", 'red')
            print_color("Certifique-se de estar no diretório raiz do projeto ou use --project para especificar o caminho.", 'yellow')
            return
        
        print_color(f"🚀 Iniciando servidor Tagon na porta {args.port}...", 'green')
        try:
            env = os.environ.copy()
            env["FLASK_RUN_PORT"] = str(args.port)
            subprocess.run([sys.executable, run_script], env=env)
        except KeyboardInterrupt:
            print_color("\n👋 Servidor Tagon encerrado", 'cyan')
    
    # Comando info
    elif args.command == 'info':
        print(BANNER)
        print_color("Tagon - O framework web reativo 100% em Python", 'cyan')
        print_color("\nCaracterísticas:", 'blue')
        print_color("  • 100% Python", 'green')
        print_color("  • CSS isolado por componente", 'green')
        print_color("  • Estrutura reativa", 'green')
        print_color("  • Simples e fácil de aprender", 'green')
        
        print_color("\nComandos disponíveis:", 'blue')
        print_color("  • create: Cria um novo projeto", 'yellow')
        print_color("  • page: Cria uma nova página", 'yellow')
        print_color("  • run: Executa o projeto", 'yellow')
        print_color("  • info: Exibe informações sobre o Tagon", 'yellow')
        
        print_color("\nExemplos:", 'blue')
        print_color("  • tagon create meu-projeto", 'magenta')
        print_color("  • tagon page MinhaPagina", 'magenta')
        print_color("  • tagon run", 'magenta')

if __name__ == "__main__":
    main()