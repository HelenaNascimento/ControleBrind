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
     --   WHERE Qtd_Dispon > 0        
    """
    produto = pd.read_sql_query(query, cnxn)
    return produto

# Função para obter produtos com nomes aproximados
def obter_produto_estoque(cnxn, descricao):
    query = """
        SELECT 
            ID_PROD,
            EAN,
            Descricao,
            Tel = NULL
        FROM PRODU
        WHERE Descricao LIKE ?
    """
    dados_produto = pd.read_sql_query(query, cnxn, params=[f"%{descricao}%"])
    return dados_produto

# Definindo o blueprint
brinde_bp = Blueprint('brinde', __name__)

# Rota principal da página de estoque
@brinde_bp.route('/Dash_Brinde')
def Dash_Brinde():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    
    # Renderiza a página sem carregar os dados de estoque diretamente
    return render_template('Brinde/brinde.html')

# Rota para fornecer estoque disponível em formato JSON
@brinde_bp.route('/estoque_disponivel', methods=['POST'])
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

# Rota para consultar produtos com nome aproximado
@brinde_bp.route('/consultar_produto_estoque', methods=['POST'])
def consultar_produto():
    descricao = request.form.get('Descricao', '')  # Usa .get para evitar KeyError
    if not descricao:
        return jsonify({"erro": "Descrição não fornecida."}), 400  # Responde com erro HTTP 400
    
    cnxn = conexao()
    if not cnxn:
        return jsonify({"erro": "Erro ao conectar ao banco de dados."}), 500

    try:
        cad_produto = obter_produto_estoque(cnxn, descricao)
        return jsonify({"cad_produto": cad_produto.to_dict(orient="records")})  # Retorna JSON com os dados dos produtos
    except Exception as e:
        print(f"Erro ao consultar produto: {e}")
        return jsonify({"erro": str(e)}), 500
    finally:
        cnxn.close()

# Configuração da aplicação principal
if __name__ == '__main__':
    app.register_blueprint(brinde_bp)  # Registrando o blueprint
    app.run(debug=True)
