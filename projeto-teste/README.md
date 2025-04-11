# Tagon Framework 🚀

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

## 📜 Licença

Distribuído sob a licença MIT.

---

<div align="center">
  <p>Feito com ❤️ em Python</p>
</div>
