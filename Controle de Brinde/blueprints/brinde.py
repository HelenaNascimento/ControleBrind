from flask import Flask, Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
import subprocess
import socket
import time
import pyodbc as bd
import pandas as pd

app = Flask(__name__)
app.secret_key = "supersecretkey"

def conexao():
    try:
        server = 'SRVHOSTHPNEW' #'WIN11\\DEV' #'SRVHOSTHPNEW' #'TECHNICAL\\DEV'
        database = 'BD_BRIND' #BD_BRIND
        username = 'sa'
        password = 'Infarma@2016.' #'senha@123' #Infarma@2016.
        cnxn = bd.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        return cnxn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para obter o estoque disponível
def estoque_disponivel(cnxn):
    query = """
        SELECT 
            ID_PROD,
            EAN,
            Descricao ,
            Qtd_Dispon,
            Marca
        FROM VW_ESTOQUE
        order by Descricao       
    """
    produto = pd.read_sql_query(query, cnxn)
    return produto

# Função para obter produtos com nomes aproximados
def retorna_consulta(cnxn, descricao):
    query = """
        SELECT 
            ID_PROD,
            EAN,
            Descricao ,
            Qtd_Dispon,
            Marca
        FROM VW_ESTOQUE
        WHERE Descricao like ?
        ORDER BY Qtd_Dispon desc   
    """
    dados_consulta = pd.read_sql_query(query, cnxn, params=[f"%{descricao}%"])
    return dados_consulta

def is_streamlit_running():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", 8501)) == 0

# Blueprint
brinde_bp = Blueprint('brinde', __name__)


# Rota principal da página de estoque
@brinde_bp.route('/Dados_Estoque=?0001')
def Dash_Brinde():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    
    # Renderiza a página sem carregar os dados de estoque diretamente
    return render_template('Brinde/brinde.html')

# Rota para fornecer estoque disponível em formato JSON
@brinde_bp.route('/Dados_Estoque=?0002', methods=['POST'])
def estoque_positivo():
    cnxn = conexao()
    if not cnxn:
        return jsonify({"erro": "Erro ao conectar ao banco de dados."}), 500
    
    try:
        estoque = estoque_disponivel(cnxn)
        return jsonify({"estoque": estoque.to_dict(orient="records")})
    except Exception as e:
        print(f"Erro ao carregar estoque: {e}")
        return jsonify({"erro": str(e)}), 500
    finally:
        cnxn.close()

# Rota para consultar produtos com nome aproximado
@brinde_bp.route('/Dados_Estoque=?0003', methods=['POST'])
def consultar_produto():
    descricao = request.form.get('Descricao', '')  # Usa .get para evitar KeyError
    if not descricao:
        return jsonify({"erro": "Descrição não fornecida."}), 400  # Responde com erro HTTP 400
    
    cnxn = conexao()
    if not cnxn:
        return jsonify({"erro": "Erro ao conectar ao banco de dados."}), 500

    try:
        cad_produto = estoque_disponivel(cnxn, descricao)
        return jsonify({"cad_produto": cad_produto.to_dict(orient="records")})  # Retorna JSON com os dados dos produtos
    except Exception as e:
        print(f"Erro ao consultar produto: {e}")
        return jsonify({"erro": str(e)}), 500
    finally:
        cnxn.close()

@brinde_bp.route('/Dados_Estoque=?0004')
def deashboard():
    # Iniciar o servidor Streamlit se ele não estiver rodando
    if not is_streamlit_running():
        subprocess.Popen(["streamlit", "run", "inicio.py"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        time.sleep(3)  # Pequena pausa para garantir que o servidor esteja iniciado

    # Redireciona para o Streamlit
    return redirect("http://localhost:8501")
    
@brinde_bp.route('/deash=1')
def retonadeash():
    pass

@brinde_bp.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))

# Configuração da aplicação principal
if __name__ == '__main__':
    app.register_blueprint(brinde_bp)  # Registrando o blueprint
    app.run(debug=True)
