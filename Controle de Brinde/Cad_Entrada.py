import streamlit as st
import pyodbc as bd
import pandas as pd

st.set_page_config(
    page_title="Controle de Brind",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função de conexão ao banco de dados
def conexao():
    cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.71;DATABASE=BD_BRIND;UID=sa;PWD=Infarma@2016.')
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
def cad_NF_Entrada(cnxn, NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor):
    cursor = cnxn.cursor()
    cursor.execute("""
        INSERT INTO NF_CB_ENT (NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor)
        VALUES (?, ?, ?, ?, ?)
    """, (NF_ENT, Dat_Entrada, int(Qtd_Total), float(Vlr_Total), IdFornecedor))
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

def insert_data (cnxn, Fantasia, CNPJ_FORN):
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

# Interface Streamlit
st.title('Cadastrar Nota de Entrada')
st.divider()

st.subheader('Cadastrar Cabeçalho de Nota de Entrada')

columns = st.columns(2)

with columns[0]:

    col = st.columns(2)

    with st.container():

        with col[0]:
            NF_ENT = st.text_input('NF_ENT:')
        with col[1]:
            Dat_Entrada = st.date_input('Data:')

    with st.container():
        with col[0]:
            CNPJ_FORN = st.text_input('CNPJ:')

        with col[1]:
            Fantasia = st.text_input('Fantasia:')

    with st.container():
        with col[0]:
            Qtd_Total = st.number_input('Quantidade Nota')

        with col[1]:
            Vlr_Total = st.number_input('Valor Nota:')

    colum = st.columns(4)
    with st.container():

        with col[0]:
            with colum[0]:
                if st.button('Consultar Fornecedor'):
                    cnxn = conexao()
                    Consul_Forne = consult_fornecedor(cnxn, CNPJ_FORN)
                    st.dataframe(Consul_Forne)
                    cnxn.close()

            with colum[1]:
                if st.button ('Inserir Dados Fornecedor'):
                    cnxn = conexao()
                    insert_data (cnxn, Fantasia, CNPJ_FORN)
                    st.success('Dados Inseridos')
                    cnxn.close()

        with col[1]:
            with colum[2]:
                if st.button('Consultar Dados da Nota'):
                    cnxn = conexao()
                    Consul_NF = Consulta_NF_ENT(cnxn, CNPJ_FORN)
                    st.dataframe(Consul_NF)
                    cnxn.close()

            with colum[3]:
                if st.button('Inserir Dados na Nota'):
                    cnxn = conexao()
                    fornecedor_df = consult_fornecedor(cnxn, CNPJ_FORN)
                    if not fornecedor_df.empty:
                        IdFornecedor = fornecedor_df.loc[0, 'IdFornecedor']
                        cad_NF_Entrada(cnxn, NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor)
                        # Inserir os produtos
                        for produto in st.session_state.produtos:
                            cad_Produto(cnxn, NF_ENT, produto['EAN'], produto['Descrição'], produto['Quantidade'], produto['Valor Unitário'])
                        st.success('Dados da Nota e Produtos Inseridos')
                    else:
                        st.error('Fornecedor não encontrado.')
                    cnxn.close()

# Variável para armazenar os produtos adicionados
if 'produtos' not in st.session_state:
    st.session_state.produtos = []

with columns[1]:
    with st.form(key='produto_form'):
        st.subheader('Adicionar Produto')
        EAN = st.text_input('EAN')
        Descricao = st.text_input('Descrição')
        Quantidade = st.number_input('Quantidade', min_value=0)
        Vlr_Unit = st.number_input('Valor Unitário', min_value=0.0)

        if st.form_submit_button('Adicionar Produto'):
            st.session_state.produtos.append({
                "EAN": EAN,
                "Descrição": Descricao,
                "Quantidade": Quantidade,
                "Valor Unitário": Vlr_Unit
            })
            
            st.success('Produto Adicionado')

    # Mostrar a lista de produtos adicionados
    if st.session_state.produtos:
        st.subheader('Produtos Adicionados')
        for i, produto in enumerate(st.session_state.produtos):
            st.write(f"{i+1}. {produto['Descrição']} - {produto['Quantidade']} unidades - R${produto['Valor Unitário']}")
            if st.button(f"Excluir Produto {i+1}", key=f"excluir_{i}"):
                st.session_state.produtos.pop(i)
                st.experimental_rerun()

# Fechar a conexão ao banco de dados
# cnxn.close() <- Não feche a conexão aqui, pois ela já é fechada em cada operação acima.
