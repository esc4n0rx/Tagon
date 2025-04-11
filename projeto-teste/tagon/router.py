import os
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
