from flask import Flask, Blueprint, render_template, session, redirect, url_for, flash, request
import pyodbc as bd
import pandas as pd

app = Flask(__name__)
app.secret_key = "supersecretkey"

def conexao():
    try:
        server = 'WIN11\\DEV' #'WIN11\\DEV' #'SRVHOSTHPNEW'
        database = 'BD_BRIND'
        username = 'sa'
        password = 'senha@123' #'senha@123' #Infarma@2016.
        cnxn = bd.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        return cnxn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None



# Definindo o blueprint
saida_bp = Blueprint('saida', __name__)

@saida_bp.route('/Sai_CB')
def Sai_CB():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('Saida/saida.html')




if __name__ == '__main__':
    app.register_blueprint(saida_bp)  # Registrando o blueprint
    app.run(debug=True)

