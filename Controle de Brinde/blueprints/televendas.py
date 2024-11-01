from flask import Flask, Blueprint, render_template, session, redirect, url_for, flash, request
import pyodbc as bd
import pandas as pd

app = Flask(__name__)
app.secret_key = "supersecretkey"

def conexao():
    server = '192.186.11.15'
    database = 'BD_BRIND'
    
    cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.71;DATABASE=BD_BRIND;UID=sa;PWD=Infarma@2016.')
    #cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID=sa;PWD=senha@123; Connection Timeout=30')

    return cnxn



# Definindo o blueprint
televendas_bp = Blueprint('televendas', __name__)

@televendas_bp.route('/Pedido_Brinde')
def Pedido_Brinde():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('Televendas/televendas.html')

if __name__ == '__main__':
    app.register_blueprint(televendas_bp)  # Registrando o blueprint
    app.run(debug=True)