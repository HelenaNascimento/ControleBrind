from flask import Flask, Blueprint, render_template, session, redirect, url_for, flash, request
import pyodbc as bd
import pandas as pd

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Função de conexão ao banco de dados
def conexao():
    server = '192.186.11.15'
    database = 'BD_BRIND'
    
    #cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.71;DATABASE=BD_BRIND;UID=sa;PWD=Infarma@2016.')
    cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID=sa;PWD=senha@123; Connection Timeout=30')
    return cnxn

# Função para consultar fornecedor
def consult_fornecedor(cnxn, CNPJ_FORN):
    query = """
        SELECT 
            IdFornecedor,
            Fantasia 
        FROM FORNE
        WHERE CNPJ_FORN = ?
    """
    Dados_Fornecedor = pd.read_sql_query(query, cnxn, params=[CNPJ_FORN])
    return Dados_Fornecedor

# Função para cadastrar nota de entrada
def cad_NF_Entrada(cnxn, NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor, Vlr_Desc):
    cursor = cnxn.cursor()
    cursor.execute("""
        INSERT INTO NF_CB_ENT (NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor, Vlr_Desc)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (NF_ENT, Dat_Entrada, int(Qtd_Total), float(Vlr_Total), IdFornecedor, float(Vlr_Desc)))
    cnxn.commit()

# Função para consultar notas de entrada
def Consulta_NF_ENT(cnxn, CNPJ_FORN):
    query = """
        SELECT 
            NF_ENT,
            Dat_Entrada,
            Fantasia,
            Qtd_Total,
            Vlr_Total
        FROM FORNE FN
        INNER JOIN NF_CB_ENT NFE ON FN.IdFornecedor = NFE.IdFornecedor
        WHERE FN.CNPJ_FORN = ?                  
    """
    Consulta_Fornecedor = pd.read_sql_query(query, cnxn, params=[CNPJ_FORN])
    return Consulta_Fornecedor

def insert_data(cnxn, Fantasia, CNPJ_FORN):
    cursor = cnxn.cursor()
    cursor.execute("""
        INSERT INTO FORNE (Fantasia, CNPJ_FORN)
        VALUES(?, ?)""", (Fantasia, CNPJ_FORN))
    cnxn.commit()

# Função para cadastrar produto
def cad_Produto(cnxn, NF_ENT, EAN, Descricao, Quantidade, Vlr_Unit):
    cursor = cnxn.cursor()
    cursor.execute("""
        INSERT INTO PRODUTO (NF_ENT, EAN, Descricao, Quantidade, Vlr_Unit)
        VALUES (?, ?, ?, ?, ?)
    """, (NF_ENT, EAN, Descricao, int(Quantidade), float(Vlr_Unit)))
    cnxn.commit()

# Definindo o blueprint
entrada_bp = Blueprint('entrada', __name__)

@entrada_bp.route('/Ent_CB')
def Ent_CB():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('Entrada/entrada.html')

# Rotas de funções associadas ao blueprint
@entrada_bp.route('/consultar_fornecedor', methods=['POST'])
def consultar_fornecedor():
    CNPJ_FORN = request.form['CNPJ_FORN']
    cnxn = conexao()
    fornecedor_df = consult_fornecedor(cnxn, CNPJ_FORN)
    cnxn.close()
    return render_template('Entrada/entrada.html', fornecedor_df=fornecedor_df)
#Alterar para tipo alerta

@entrada_bp.route('/inserir_fornecedor', methods=['POST'])
def inserir_fornecedor():
    Fantasia = request.form['Fantasia']
    CNPJ_FORN = request.form['CNPJ_FORN']
    cnxn = conexao()
    insert_data(cnxn, Fantasia, CNPJ_FORN)
    cnxn.close()
    flash('Dados do fornecedor inseridos com sucesso!')
    return redirect(url_for('entrada.Ent_CB'))
#Alterar para tipo alerta

@entrada_bp.route('/consultar_nota', methods=['POST'])
def consultar_nota():
    CNPJ_FORN = request.form['CNPJ_FORN']
    cnxn = conexao()
    nota_df = Consulta_NF_ENT(cnxn, CNPJ_FORN)
    cnxn.close()
    return render_template('Entrada/entrada.html', nota_df=nota_df)

@entrada_bp.route('/inserir_nota', methods=['POST'])
def inserir_nota():
    NF_ENT = request.form['NF_ENT']
    Dat_Entrada = request.form['Dat_Entrada']
    CNPJ_FORN = request.form['CNPJ_FORN']
    Qtd_Total = request.form['Qtd_Total']
    Vlr_Total = request.form['Vlr_Total']
    Vlr_Desc = request.form['Vlr_Desc']
    
    cnxn = conexao()
    fornecedor_df = consult_fornecedor(cnxn, CNPJ_FORN)
    if not fornecedor_df.empty:
        IdFornecedor = fornecedor_df.loc[0, 'IdFornecedor']
        cad_NF_Entrada(cnxn, NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor, Vlr_Desc)
        # Inserir os produtos
        produtos = request.form.getlist('produtos')
        for produto in produtos:
            cad_Produto(cnxn, NF_ENT, produto['EAN'], produto['Descricao'], produto['Quantidade'], produto['Vlr_Unit'])
        flash('Dados da nota e produtos inseridos com sucesso!')
    else:
        flash('Fornecedor não encontrado.')
    cnxn.close()
    return redirect(url_for('entrada.Ent_CB'))

if __name__ == '__main__':
    app.register_blueprint(entrada_bp)  # Registrando o blueprint
    app.run(debug=True)