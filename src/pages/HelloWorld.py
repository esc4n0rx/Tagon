def main():
    return {
        "html": """
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
        """,
        "css": """
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
        """
    }