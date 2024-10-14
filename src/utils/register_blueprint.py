import os
import importlib

def register_blueprints(app, package_name, package_path):
    """Registra automaticamente todos os blueprints de uma pasta"""
    for module_name in os.listdir(package_path):
        if module_name.endswith(".py") and module_name != "__init__.py":
            # Importa o módulo dinamicamente
            module = importlib.import_module(f"{package_name}.{module_name[:-3]}")
            # Verifica se o módulo contém o blueprint
            if hasattr(module, 'blueprint'):
                app.register_blueprint(getattr(module, 'blueprint'), url_prefix='/api')
