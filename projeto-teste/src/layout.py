def layout(content):
    html = content if isinstance(content, str) else content.get("html", "")
    css = "" if isinstance(content, str) else content.get("css", "")

    # CSS global com tema escuro e animações
    global_css = """
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
    """

    return f"""
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
    """
