import streamlit as st
import pyodbc as bd

#funcão conecta banco

def conexao():
    cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.71;DATABASE=BD_BRIND;UID=sa;PWD=Infarma@2016.')
    return cnxn


cnxn = conexao()

#Funcao para inserir dados no banco

def insert_data (cnxn, Fantasia, CNPJ_FORN):
    cursor = cnxn.cursor()
    cursor.execute("""
        INSERT INTO FORNE (Fantasia, CNPJ_FORN)
        VALUES(?, ?)""", (Fantasia, CNPJ_FORN))
    cnxn.commit()

#Interface Streamlit

st.title('Cadastrar Fornecedor')

Fantasia = st.text_input('Fantasia: ' )
CNPJ_FORN = st.number_input('CNPJ: ', min_value=0)

if st.button ('Inserir'):
    cnxn = conexao()
    insert_data (cnxn, Fantasia, CNPJ_FORN)
    st.success('Dados Inseridos')
    cnxn.close()