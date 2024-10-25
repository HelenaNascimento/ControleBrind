import pyodbc as bd

def conexao():
    server = r'WIN11\DEV'  # ou 'WIN11\\\\DEV'
    database = 'BD_BRIND'
    try:
        cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID=sa;PWD=senha@123')
        print("Conexão bem-sucedida!")
        cnxn.close()
    except Exception as e:
        print(f"Erro de conexão: {e}")

conexao()
