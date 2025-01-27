USE BD_BRIND
GO


CREATE PROCEDURE PR_InserirNotaFiscal
	@Num_Nota INT,
	@Chv_Acesso VARCHAR(44),
	@Dat_Entrada SMALLDATETIME,
	@CNPJ VARCHAR(14),
	@VLR_B DECIMAL(10,2),
	@VLR_D DECIMAL(10,2),
	@PER_DES DECIMAL (10,2),
	@OUTR DECIMAL(10,2),
	@QTD_T INT,
	@VLR_T DECIMAL(10,2),
	@OBS TEXT,
    @IDNota INT OUTPUT
AS

DECLARE @ID_FORN INT = (select ID_FORNE from FORNE where CNPJ_FORN = @CNPJ)

BEGIN
    INSERT INTO CB_ENT(Num_Nota, Chv_Acesso, Dat_Entrada, ID_FORN, Valor_Bruto, Vlr_Desc, Per_Desconto, Outras_Dispesas, Qtd_Total, Vlr_Total, Observacao)
    VALUES (@Num_Nota, @Chv_Acesso, @Dat_Entrada, @ID_FORN,  @VLR_B, @VLR_D, @PER_DES, @OUTR, @QTD_T, @VLR_T, @OBS);
    
    SET @IDNota = SCOPE_IDENTITY(); -- Retorna o ID gerado
END;

