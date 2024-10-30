from flask import Flask, render_template, request, redirect, url_for, flash, session
import pyodbc as bd
from werkzeug.security import check_password_hash

# Importando blueprints
from blueprints.entrada import entrada_bp
from blueprints.saida import saida_bp
from blueprints.brinde import brinde_bp
from blueprints.televendas import televendas_bp

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # para flash messages e sessões

# Função de conexão ao banco de dados
def conexao():
    server = 'WIN11\\DEV'
    database = 'BD_BRIND'

    try:
        #cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.71;DATABASE=BD_BRIND;UID=sa;PWD=Infarma@2016.')
        cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID=sa;PWD=senha@123; Connection Timeout=30')
        return cnxn

    except Exception as e:
        print(f"Erro de conexão ao banco de dados: {e}")
        return None

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Login = request.form['username']
        Senha = request.form['password']

        conn = conexao()
        if conn is None:
            flash('Erro ao conectar ao banco de dados.', 'danger')
            return redirect(url_for('login'))

        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM LOGIN WHERE Login = ?', (Login,))
            user = cursor.fetchone()
            conn.close()

            if user:
                if user.Senha == Senha:
                    session['user_id'] = user.IdUser  # Exemplo de ID do usuário
                    flash('Login realizado com sucesso!', 'success')

                    if Login == 'Entrada':
                        return redirect(url_for('entrada.Ent_CB'))
                    elif Login == 'Saida':
                        return redirect(url_for('saida.Sai_CB'))
                    elif Login == 'Brinde':
                        return redirect(url_for('brinde.Dash_Brinde'))
                    elif Login == 'Televendas':
                        return redirect(url_for('televendas.Pedido_Brinde'))
                else:
                    flash('Senha incorreta.', 'danger')
            else:
                flash('Usuário não encontrado.', 'danger')
        except Exception as e:
            flash(f'Erro na consulta ao banco de dados: {e}', 'danger')

    return render_template('login.html')

# Rota de logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))

# Registrando os blueprints
app.register_blueprint(entrada_bp)
app.register_blueprint(saida_bp)
app.register_blueprint(brinde_bp)
app.register_blueprint(televendas_bp)

if __name__ == '__main__':
    app.run(debug=True)
