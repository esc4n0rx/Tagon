def main():
    return {
        "html": """
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
        """,
        "css": """
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
        """
    }