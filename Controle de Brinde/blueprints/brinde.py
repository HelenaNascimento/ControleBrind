from flask import Flask, Blueprint, render_template, session, redirect, url_for, flash, request
import pyodbc as bd
import pandas as pd


app = Flask(__name__)
app.secret_key = "supersecretkey"


def conexao():
    server = '192.186.11.15'
    database = 'BD_BRIND'
    
    #cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.71;DATABASE=BD_BRIND;UID=sa;PWD=Infarma@2016.')
    cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID=sa;PWD=senha@123; Connection Timeout=30')
    return cnxn


# Renomeando esta função para evitar conflito
def obter_produto_estoque(cnxn, ID_PROD):
    query = """
        SELECT 
            ID_PROD,
        FROM PRODU
        WHERE Descricao = ?
    """
    Dados_Produto = pd.read_sql_query(query, cnxn, params=[ID_PROD])
    return Dados_Produto

# Definindo o blueprint
brinde_bp = Blueprint('brinde', __name__)

@brinde_bp.route('/Dash_Brinde')
def Dash_Brinde():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('Brinde/brinde.html')

# Rota de Consulta de Produto
@brinde_bp.route('/consultar_produto_estoque', methods=['POST'])
def consultar_produto():
    try:
        CAD_PROD = request.form.get('ID_PROD', '')  # Utilizando .get para evitar KeyError
        if not CAD_PROD:
            raise ValueError("ID_PROD não fornecido.")
        
        cnxn = conexao()
        cad_produto = obter_produto_estoque(cnxn, CAD_PROD)
        cnxn.close()
        return {"cad_produto": cad_produto.to_dict()}  # Retorna JSON temporariamente
    except Exception as e:
        print(f"Erro ao consultar produto: {e}")
        return {"erro": str(e)}, 500


if __name__ == '__main__':
    app.register_blueprint(brinde_bp)  # Registrando o blueprint
    app.run(debug=True)
