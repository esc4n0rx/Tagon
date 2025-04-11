# Tagon Framework 🚀

Tagon é um framework web reativo 100% em Python, inspirado em React, mas utilizando apenas Python para criar aplicações web modernas e reativas.

<div align="center">
  <img src="https://raw.githubusercontent.com/user/tagon/main/docs/tagon-logo.png" alt="Tagon Logo" width="200">
  <p><i>O framework web reativo 100% em Python</i></p>
</div>

## ✨ Características

- **100% Python**: Desenvolva aplicações web completas usando apenas Python
- **CSS Isolado**: Cada componente com seu próprio escopo de estilos
- **Reativo**: Interface dinâmica e responsiva para seus usuários
- **Simples**: API intuitiva e fácil de aprender
- **Zero Dependências Frontend**: Não requer Node.js, npm ou pacotes JavaScript

## 🚀 Instalação

### Via pip (Recomendado)

```bash
# Instale o pacote
pip install tagon

# Crie um novo projeto
tagon create meu-projeto

# Entre no diretório do projeto
cd meu-projeto

# Execute a aplicação
tagon run
```

### Manualmente

```bash
# Clone o repositório
git clone https://github.com/esc4n0rx/tagon.git
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

## 🛠️ Comandos do CLI

Tagon inclui uma ferramenta de linha de comando para facilitar o desenvolvimento:

```bash
# Criar um novo projeto
tagon create nome-do-projeto [--template dark|light] [--git] [--install]

# Criar uma nova página
tagon page NomeDaPagina

# Executar o servidor de desenvolvimento
tagon run [--port PORTA]

# Exibir informações sobre o Tagon
tagon info
```

## 🔧 Estrutura do Projeto

```
meu-projeto/
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

Você pode criar páginas de duas maneiras:

#### 1. Usando o CLI (Recomendado)

```bash
# Crie uma nova página chamada MinhaPagina
tagon page MinhaPagina
```

#### 2. Manualmente

Crie um arquivo Python em `src/pages/` com uma função `main()` que retorna um dicionário contendo `html` e `css`:

```python
def main():
    return {
        "html": """
            <div>
                <h1>Minha Página</h1>
                <p>Conteúdo da página</p>
            </div>
        """,
        "css": """
            h1 { color: var(--primary); }
            p { color: var(--text-color); }
        """
    }
```

### Como as Rotas Funcionam

- O arquivo `index.py` é acessado na rota `/`
- Outros arquivos são acessados na rota `/{nome_do_arquivo}`
- Por exemplo, `HelloWorld.py` é acessado em `/HelloWorld`

### Estilos Globais

O Tagon utiliza variáveis CSS para manter a consistência dos estilos:

```css
:root {
    --primary: #10B981;    /* Verde */
    --secondary: #8B5CF6;  /* Roxo */
    --text-color: #E2E8F0; /* Branco acinzentado */
    --bg-color: #0F172A;   /* Azul escuro */
    --card-bg: #1E293B;    /* Cinza azulado */
    --radius: 8px;         /* Arredondamento */
}
```

Você pode usar essas variáveis em seu CSS para manter a consistência com o tema da aplicação.

## 🎨 Temas

O Tagon vem com um tema escuro por padrão, com animações e efeitos modernos. Você pode personalizar o tema modificando as variáveis CSS no arquivo `layout.py` ou escolher o tema claro ao criar um projeto:

```bash
tagon create meu-projeto --template light
```

## 📚 Exemplos

### Exemplo Básico

```python
def main():
    return {
        "html": """
            <h1>Hello World!</h1>
            <p>Meu primeiro componente Tagon.</p>
        """,
        "css": """
            h1 { color: var(--primary); }
            p { color: var(--text-color); }
        """
    }
```

### Exemplo com Componentes Dinâmicos

```python
def main():
    items = ["Python", "Flask", "HTML", "CSS"]
    
    list_items = "".join([f"<li>{item}</li>" for item in items])
    
    return {
        "html": f"""
            <div class="container">
                <h1>Tecnologias</h1>
                <ul>{list_items}</ul>
            </div>
        """,
        "css": """
            .container { padding: 1rem; }
            ul { list-style-type: circle; }
            li { margin-bottom: 0.5rem; }
        """
    }
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## 📮 Contato

Paulo Oliveira - contato.paulooliver9@gmail.com

Link do Projeto: [https://github.com/esc4n0rx/tagon](https://github.com/esc4n0rx/tagon)

---

<div align="center">
  <p>Feito com ❤️ em Python</p>
</div>