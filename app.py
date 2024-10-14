from flask import Flask, render_template  
from dotenv import load_dotenv
from flask_migrate import Migrate  # Importar Flask-Migrate
from src.utils.register_blueprint import register_blueprints  # Importar a função separada
from src.models.user import db, User  # Importar o modelo User e a instância db
from src.utils.chat_routes import chat_bp  # Importar o blueprint de chat
import os

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar o Flask app
app = Flask(__name__, static_folder='src/static')

# Configuração do banco de dados com SQLAlchemy (PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar a instância do banco de dados com o app
db.init_app(app)

# Inicializar Flask-Migrate
migrate = Migrate(app, db)

# Registrar automaticamente todos os blueprints na pasta 'api'
register_blueprints(app, 'src.api', 'src/api')

# Registrar o blueprint do chat
app.register_blueprint(chat_bp)

@app.route('/')
def home():
    return "Servidor Flask rodando" 

if __name__ == '__main__':
    app.run(debug=True)
