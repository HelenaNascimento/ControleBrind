from flask import Flask, Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
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


# Função para obter o estoque disponível
def todo_estoque_positivo(cnxn):
    query = """
        SELECT 
            ID_PROD,
            Descricao,
            Qtd_Dispon,
            MR.Nome AS Marca
        FROM PRODU PR
            JOIN MARCA MR ON PR.ID_Marca = MR.ID_Marca
        WHERE Qtd_Dispon > 0        
    """
    produto = pd.read_sql_query(query, cnxn)
    return produto


# Definindo o blueprint
televendas_bp = Blueprint('televendas', __name__)

@televendas_bp.route('/Pedido_Brinde')
def Pedido_Brinde():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('Televendas/televendas.html')


# Rota para fornecer estoque disponível em formato JSON
@televendas_bp.route('/estoque_disponivel', methods=['POST'])
def estoque_positivo():
    cnxn = conexao()
    if not cnxn:
        return jsonify({"erro": "Erro ao conectar ao banco de dados."}), 500
    
    try:
        estoque = todo_estoque_positivo(cnxn)
        return jsonify({"estoque": estoque.to_dict(orient="records")})
    except Exception as e:
        print(f"Erro ao carregar estoque: {e}")
        return jsonify({"erro": str(e)}), 500
    finally:
        cnxn.close()

if __name__ == '__main__':
    app.register_blueprint(televendas_bp)  # Registrando o blueprint
    app.run(debug=True)