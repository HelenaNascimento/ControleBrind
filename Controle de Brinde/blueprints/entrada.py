from flask import Flask, Blueprint, render_template, session, redirect, url_for, flash, request
import pyodbc as bd
import pandas as pd
import xml as xml


app = Flask(__name__)
app.secret_key = "supersecretkey"

def conexao():
    try:
        server = 'SRVHOSTHPNEW' #'WIN11\\DEV' #'SRVHOSTHPNEW'
        database = 'BD_BRIND'
        username = 'sa'
        password = 'Infarma@2016.' #'senha@123' #Infarma@2016.
        cnxn = bd.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        return cnxn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# PR_RetornaDadosFonecedor
def consult_chave(cnxn, CHV_ACESSO):
    query = """
        exec dbo.PR_RetornaDadosFonecedor @CHV_ACESSO = ?
    """
    # Obtenção de dados como DataFrame
    Dados_ChvAcesso = pd.read_sql_query(query, cnxn, params=[CHV_ACESSO])
    return Dados_ChvAcesso



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
    

def insert_itens(cnxn, NF_ENT, Dat_Entrada, IdProduto, Qtd_Item, Vlr_Bruto, Vlr_Desc, Id_Marca, Modelo):
    cursor = cnxn.cursor()
    cursor.execute("""
                   INSERT INTO ID_IT_ENT (NF_ENT, Dat_Entrada, IdProduto, Qtd_Item, Vlr_Bruto, Vlr_Desc, Id_Marca, Modelo)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                   """, (NF_ENT, Dat_Entrada, int(IdProduto), int(Qtd_Item), float(Vlr_Bruto), float(Vlr_Desc), int(Id_Marca), Modelo))
    cnxn.commit()


# Função para cadastrar nota de entrada
def cad_NF_Entrada(cnxn, NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor, Vlr_Desc):
    cursor = cnxn.cursor()
    cursor.execute("""
        INSERT INTO CB_ENT (NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor, Vlr_Desc)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (NF_ENT, Dat_Entrada, int(Qtd_Total), float(Vlr_Total), IdFornecedor, float(Vlr_Desc)))
    cnxn.commit()


# Definindo o blueprint
entrada_bp = Blueprint('entrada', __name__)

@entrada_bp.route('/EntradaNota=?0001')
def Ent_CB():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    dados = {  # Variável inicializada com valores padrão
        'NF_ENT': '',
        'Dat_Entrada': '',
        'CNPJ_FORN': '',
        'Fantasia': ''
    }
    return render_template('Entrada/entrada.html', dados=dados)



@entrada_bp.route('/EntradaNota=?0002', methods=['POST'])
def consultar_fornecedor():
    chave_acesso = request.form.get('chave_acesso')  # Verifica se "Sim" ou "Não"
    dados = {
        'NF_ENT': '',
        'Dat_Entrada': '',
        'CNPJ_FORN': '',
        'Fantasia': ''
    }  # Inicializa com valores vazios

    if chave_acesso == 'sim':
        # Se chave de acesso for fornecida, buscar os dados
        CHV_ACESSO = request.form.get('CHV_ACESSO')
        if CHV_ACESSO:  # Apenas tenta consultar se a chave foi preenchida
            cnxn = conexao()
            try:
                chave_df = consult_chave(cnxn, CHV_ACESSO)
            finally:
                cnxn.close()

            # Preenche os dados retornados pela consulta
            if not chave_df.empty:
                dados.update({
                    'NF_ENTRADA': chave_df.iloc[0]['NF_ENTRADA'],
                    'CNPJ_FORN': chave_df.iloc[0]['CNPJ_FORN'],
                    'Fantasia': chave_df.iloc[0]['Razao_Social']
                })
            else:
                dados['Fantasia'] = "Fornecedor não encontrado."
    else:
        # Caso "Não", os dados serão preenchidos manualmente (mantêm-se vazios)
        pass

    return render_template('Entrada/entrada.html', dados=dados)



@entrada_bp.route('/EntradaNota=?0003', methods=['POST'])
def inserir_fornecedor():
    Fantasia = request.form['Fantasia']
    CNPJ_FORN = request.form['CNPJ_FORN']
    cnxn = conexao()
    insert_data(cnxn, Fantasia, CNPJ_FORN)
    cnxn.close()
    flash('Dados do fornecedor inseridos com sucesso!')
    return redirect(url_for('entrada.Ent_CB'))
#Alterar para tipo alerta

@entrada_bp.route('/EntradaNota=?0004', methods=['POST'])
def inserir_item():
    NF_ENT = request.form['NF_ENT']
    EAN = request.form['EAN']
    Descricao = request.form['Descricao']
    Quantidade = request.form['Quantidade']
    Vlr_Unit = request.form['Vlr_Unit']
    
    cnxn = conexao()
    cad_Produto(cnxn, NF_ENT, EAN, Descricao, Quantidade, Vlr_Unit)
    cnxn.close()
    
    flash('Item inserido com sucesso!')
    return redirect(url_for('entrada.Ent_CB'))


@entrada_bp.route('/EntradaNota=?0005', methods=['POST'])
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


@entrada_bp.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.register_blueprint(entrada_bp)  # Registrando o blueprint
    app.run(debug=True)