
CREATE PROCEDURE PR_CadastrarFornecedor 
	(	@Razao_Social  Varchar(80),
		@CNPJ VARCHAR(14),
		@FLG_COMPRA BIT)

WITH ENCRYPTION
AS

SET NOCOUNT ON 

IF(select top 1 1 from FORNE where CNPJ_FORN = @CNPJ) = 1 
	PRINT ('Fornecedor Cadastrado')

ELSE INSERT FORNE(Razao_Social, CNPJ_FORN, Tip_Comp)
		VALUES (@Razao_Social, @CNPJ, @FLG_COMPRA)

	IF @FLG_COMPRA = 0
		DECLARE @SITE VARCHAR(80)

		INSERT WEB (SITE)
		VALUES (@SITE)

	IF @FLG_COMPRA = 0
		
		
	