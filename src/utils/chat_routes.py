from flask import Blueprint, render_template, request, redirect, url_for

# Definir um blueprint para o chat
chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        # Lógica para receber a mensagem e exibir no chat (simulado)
        message = request.form['message']
        print(f"Mensagem recebida: {message}")
        # Você pode adicionar a lógica para salvar as mensagens no banco de dados ou exibi-las
        return redirect(url_for('chat_bp.chat'))
    return render_template('chat.html')
