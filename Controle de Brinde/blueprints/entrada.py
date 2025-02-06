from flask import (
    Flask,
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    flash,
    request,
    jsonify,
)
import pyodbc as bd
import pandas as pd
import xml as xml


app = Flask(__name__)
app.secret_key = "supersecretkey"


def conexao():
    try:
        server = "TECHNICAL\\DEV"  #'WIN11\\DEV' #'SRVHOSTHPNEW' #'TECHNICAL\\DEV'
        database = "BD_BRIND"  # BD_BRINDE
        username = "sa"
        password = "senha@123"  #'senha@123' #Infarma@2016.
        cnxn = bd.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        )
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
    cursor = cnxn.cursor()
    cursor.execute(
        """
        SELECT 
            IdFornecedor,
            Fantasia 
        FROM FORNE
        WHERE CNPJ_FORN = ?
    """
    )
    cnxn.commit()
    Dados_Fornecedor = pd.read_sql_query(cnxn, params=[CNPJ_FORN])
    return Dados_Fornecedor


# Inserir Dados de Fornecedor
def insert_data(cnxn, FLG_COMPRA):
    def insert_data():
        """Função para coletar dados adicionais dependendo da compra."""
        if FLG_COMPRA == 1:  # Compra online
            print("Compra online selecionada.")
            site = input("Digite o site: ")
            complemento = input("Digite o complemento: ")
        else:  # Compra física
            print("Compra física selecionada.")
            site = None
            complemento = input("Digite o complemento: ")
        return site, complemento

    # Coleta os dados adicionais
    site, complemento = insert_data()

    # Outros dados necessários
    razao_social = input("Digite a razão social: ")
    cnpj = input("Digite o CNPJ: ")
    nome_bairro = input("Digite o ID do bairro: ")
    nome_cidade = input("Digite o ID da cidade: ")
    uf = input("Digite a UF: ")
    rua = input("Digite a rua: ")
    numero = input("Digite o número: ")

    # Insere os dados no banco
    cursor = cnxn.cursor()
    cursor.execute(
        """
        exec PR_CadastrarFornecedor 
        @Razao_Social = ?, @CNPJ = ?, @FLG_COMPRA = ?, 
        @SITE = ?, @IdBair = ?, @IdCid = ?, 
        @IdEst = ?, @UF = ?, @Rua = ?, @Numero = ?, 
        @Complemento = ?
    """,
        (
            razao_social,
            cnpj,
            FLG_COMPRA,
            site,
            nome_bairro,
            nome_cidade,
            uf,
            rua,
            numero,
            complemento,
        ),
    )
    cnxn.commit()
    print("Dados inseridos com sucesso!")


# Função para consultar Produtos
def bus_Produto(cnxn, Descricao):
    cursor = cnxn.cursor()
    cursor.execute(
        """
        SELECT 
            ID_PROD,
            Descricao, 
            EAN, 
            MARCA,
            MODELO 
        FROM [VW_ESTOQUE]
        WHERE 
          Descricao = ?
        """
    )
    cnxn.commit()
    Dados_Produto = pd.read_sql_query(cnxn, params=[Descricao])
    return Dados_Produto


# Função para cadastrar produto
def cad_Produto(cnxn, NF_ENT, EAN, Descricao, Quantidade, Vlr_Unit):
    cursor = cnxn.cursor()
    cursor.execute(
        """
        INSERT INTO PRODUTO (NF_ENT, EAN, Descricao, Quantidade, Vlr_Unit)
        VALUES (?, ?, ?, ?, ?)
    """,
        (NF_ENT, EAN, Descricao, int(Quantidade), float(Vlr_Unit)),
    )
    cnxn.commit()


def insert_itens(
    cnxn,
    NF_ENT,
    Dat_Entrada,
    IdProduto,
    Qtd_Item,
    Vlr_Bruto,
    Vlr_Desc,
    Id_Marca,
    Modelo,
):
    cursor = cnxn.cursor()
    cursor.execute(
        """                    
                    exec dbo.PR_InserirItensNota @IdNota_Ent = ?, @NF_Ent = ?, @Dat_Entrada = ?, @IdProduto = ?, @Qtd_Item = ?, @Vlr_Bruto = ?, @Vlr_Desc = ?, @Id_Marca = ?, @Modelo = ?
                   """,
        (
            NF_ENT,
            Dat_Entrada,
            int(IdProduto),
            int(Qtd_Item),
            float(Vlr_Bruto),
            float(Vlr_Desc),
            int(Id_Marca),
            Modelo,
        ),
    )
    cnxn.commit()


# Função para cadastrar nota de entrada
def cad_NF_Entrada(
    cnxn, NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor, Vlr_Desc
):
    cursor = cnxn.cursor()
    cursor.execute(
        """
            exec dbo.PR_InserirNotaFiscal @Num_Nota = ?, @Chv_Acesso = ?, @Dat_Entrada = ?, @ID_FORN = ?,  @VLR_B = ?, @VLR_D = ?, @PER_DES = ?, @OUTR = ?, @QTD_T = ?, @VLR_T = ?, @OBS = ?
    """,
        (
            NF_ENT,
            Dat_Entrada,
            int(Qtd_Total),
            float(Vlr_Total),
            IdFornecedor,
            float(Vlr_Desc),
        ),
    )
    cnxn.commit()


# Definindo o blueprint
entrada_bp = Blueprint("EntradaNota", __name__)


@entrada_bp.route("/0001")
def Ent_CB():
    if "user_id" not in session:
        flash("Por favor, faça o login primeiro.", "warning")
        return redirect(url_for("login"))
    dados = {  # Variável inicializada com valores padrão
        "NF_ENT": "",
        "Dat_Entrada": "",
        "CNPJ_FORN": "",
        "Fantasia": "",
    }
    return render_template("Entrada/entrada.html", dados=dados)


@entrada_bp.route("/0002", methods=["POST"])
def consultar_fornecedor():
    chave_acesso = request.form.get("chave_acesso")  # Verifica se "Sim" ou "Não"
    dados = {
        "NF_ENT": "",
        "Dat_Entrada": "",
        "CNPJ_FORN": "",
        "Fantasia": "",
    }  # Inicializa com valores vazios

    if chave_acesso == "sim":
        # Se chave de acesso for fornecida, buscar os dados
        CHV_ACESSO = request.form.get("CHV_ACESSO")
        if CHV_ACESSO:  # Apenas tenta consultar se a chave foi preenchida
            cnxn = conexao()
            try:
                chave_df = consult_chave(cnxn, CHV_ACESSO)
            finally:
                cnxn.close()

            # Preenche os dados retornados pela consulta
            if not chave_df.empty:
                dados.update(
                    {
                        "NF_ENTRADA": chave_df.iloc[0]["NF_ENTRADA"],
                        "CNPJ_FORN": chave_df.iloc[0]["CNPJ_FORN"],
                        "Fantasia": chave_df.iloc[0]["Razao_Social"],
                    }
                )
            else:
                dados["Fantasia"] = "Fornecedor não encontrado."
    else:
        # Caso "Não", os dados serão preenchidos manualmente (mantêm-se vazios)
        pass

    return render_template("Entrada/entrada.html", dados=dados)


@entrada_bp.route("/0003", methods=["POST"])
def insert_data():
    try:
        # Validate and convert input data
        if not all(
            field in request.form for field in ["FLG_COMPRA", "Razao_Social", "CNPJ"]
        ):
            return jsonify({"erro": "Campos obrigatórios faltando"}), 400

        FLG_COMPRA = int(request.form.get("FLG_COMPRA", 0))
        razao_social = request.form.get("Razao_Social").strip()
        cnpj = request.form.get("CNPJ").strip()
        site = request.form.get("SITE").strip() if FLG_COMPRA == 1 else None
        id_bair = int(request.form.get("IdBair", 0))
        id_cid = int(request.form.get("IdCid", 0))
        id_est = int(request.form.get("IdEst", 0))
        uf = request.form.get("UF", "").strip()
        rua = request.form.get("Rua", "").strip()
        numero = request.form.get("Numero", "").strip()
        complemento = request.form.get("Complemento", "").strip()

        # Validate CNPJ format
        if (
            not cnpj
            or len(cnpj.replace(".", "").replace("/", "").replace("-", "")) != 14
        ):
            return jsonify({"erro": "CNPJ inválido"}), 400

        with conexao() as cnxn:
            with cnxn.cursor() as cursor:
                cursor.execute(
                    """
                    exec PR_CadastrarFornecedor 
                    @Razao_Social = ?, @CNPJ = ?, @FLG_COMPRA = ?, 
                    @SITE = ?, @IdBair = ?, @IdCid = ?, 
                    @IdEst = ?, @UF = ?, @Rua = ?, @Numero = ?, 
                    @Complemento = ?
                """,
                    (
                        razao_social,
                        cnpj,
                        FLG_COMPRA,
                        site,
                        id_bair,
                        id_cid,
                        id_est,
                        uf,
                        rua,
                        numero,
                        complemento,
                    ),
                )
                cnxn.commit()

        return jsonify({"mensagem": "Fornecedor cadastrado com sucesso!"}), 201

    except ValueError as ve:
        return jsonify({"erro": f"Erro de validação: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro ao cadastrar fornecedor: {str(e)}"}), 500


@entrada_bp.route("/0004", methods=["POST"])
def inserir_item():
    try:
        # Validate required fields
        required_fields = ["NF_ENT", "EAN", "Descricao", "Quantidade", "Vlr_Unit"]
        if not all(field in request.form for field in required_fields):
            return jsonify({"erro": "Campos obrigatórios faltando"}), 400

        # Convert and validate numeric inputs
        NF_ENT = request.form["NF_ENT"].strip()
        EAN = request.form["EAN"].strip()
        Descricao = request.form["Descricao"].strip()
        Quantidade = float(request.form["Quantidade"])
        Vlr_Unit = float(request.form["Vlr_Unit"])

        with conexao() as cnxn:
            cad_Produto(cnxn, NF_ENT, EAN, Descricao, Quantidade, Vlr_Unit)

        return jsonify({"mensagem": "Item cadastrado com sucesso!"}), 201

    except ValueError as ve:
        return jsonify({"erro": f"Erro de validação: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro ao cadastrar item: {str(e)}"}), 500


@entrada_bp.route("/0005", methods=["POST"])
def inserir_nota():
    NF_ENT = request.form["NF_ENT"]
    Dat_Entrada = request.form["Dat_Entrada"]
    CNPJ_FORN = request.form["CNPJ_FORN"]
    Qtd_Total = request.form["Qtd_Total"]
    Vlr_Total = request.form["Vlr_Total"]
    Vlr_Desc = request.form["Vlr_Desc"]

    cnxn = conexao()
    fornecedor_df = consult_fornecedor(cnxn, CNPJ_FORN)
    if not fornecedor_df.empty:
        IdFornecedor = fornecedor_df.loc[0, "IdFornecedor"]
        cad_NF_Entrada(
            cnxn, NF_ENT, Dat_Entrada, Qtd_Total, Vlr_Total, IdFornecedor, Vlr_Desc
        )
        # Inserir os produtos
        produtos = request.form.getlist("produtos")
        for produto in produtos:
            cad_Produto(
                cnxn,
                NF_ENT,
                produto["EAN"],
                produto["Descricao"],
                produto["Quantidade"],
                produto["Vlr_Unit"],
            )
        flash("Dados da nota e produtos inseridos com sucesso!")
    else:
        flash("Fornecedor não encontrado.")
    cnxn.close()
    return redirect(url_for("entrada.Ent_CB"))


@entrada_bp.route("/0006", methods=["POST"])
def buscar_produto():
    Descricao = request.form["Descricao"]
    cnxn = conexao()
    produtos_df = bus_Produto(cnxn, Descricao)
    cnxn.close()
    return produtos_df.to_json(orient="records")


@entrada_bp.route("/logout")
def logout():
    logout_user()
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for("login"))


@entrada_bp.route("/logoff")
def logoff():
    return redirect(url_for("login.log_CB"))


if __name__ == "__main__":
    app.register_blueprint(entrada_bp)  # Registrando o blueprint
    app.run(debug=True)
