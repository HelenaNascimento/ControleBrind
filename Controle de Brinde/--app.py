# app.py

from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session
import pyodbc as bd
from blueprints.entrada import entrada_bp
from blueprints.saida import saida_bp
from blueprints.brinde import brinde_bp
from blueprints.televendas import televendas_bp

# Iniciar o aplicativo Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Função de conexão ao banco de dados
def conexao():
    try:
        cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.71;DATABASE=BD_BRIND;UID=sa;PWD=Infarma@2016.')
        return cnxn
    except Exception as e:
        print(f"Erro de conexão ao banco de dados: {e}")
        return None

# Rota da API com Flask para login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        Login = data.get('username')
        Senha = data.get('password')

        conn = conexao()
        if conn is None:
            return jsonify({'success': False, 'message': 'Erro ao conectar ao banco de dados.'}), 500

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM LOGIN WHERE Login = ?', (Login,))
        user = cursor.fetchone()
        conn.close()

        if user:
            if user.Senha == Senha:
                session['user_id'] = user.IdUser
                
                next_page = None
                if Login == 'Entrada':
                    next_page = 'entrada'
                elif Login == 'Saida':
                    next_page = 'saida'
                elif Login == 'Brinde':
                    next_page = 'brinde'
                elif Login == 'Televendas':
                    next_page = 'televendas'

                return jsonify({
                    'success': True,
                    'message': 'Login realizado com sucesso!',
                    'next_page': next_page
                }), 200
            else:
                return jsonify({'success': False, 'message': 'Senha incorreta.'}), 401
        else:
            return jsonify({'success': False, 'message': 'Usuário não encontrado.'}), 404

    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro no servidor: {e}'}), 500

# Rota de logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({'success': True, 'message': 'Logout realizado com sucesso!'})

# Registrando os blueprints
app.register_blueprint(entrada_bp)
app.register_blueprint(saida_bp)
app.register_blueprint(brinde_bp)
app.register_blueprint(televendas_bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Executa o servidor Flask
