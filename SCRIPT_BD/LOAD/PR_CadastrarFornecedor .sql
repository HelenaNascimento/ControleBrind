USE BD_BRIND
GO
SET ANSI_NULLS, QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE PR_CadastrarFornecedor 
	(	@Razao_Social  Varchar(80),
		@CNPJ VARCHAR(14),
		@FLG_COMPRA BIT,
		@SITE VARCHAR(80) null, 
		@IdBair int, 
		@IdCid int, 
		@IdEst int, 
		@IdForne int,
		@Cidade varchar(80) null,
		@Bairro varchar (80) null,
		@UF VARCHAR(2) null,
		@Rua varchar(80) null, 
		@Numero int null, 
		@Complemento varchar(80) null)

WITH ENCRYPTION
AS

SET NOCOUNT ON 

IF(select top 1 1 from FORNE where CNPJ_FORN = @CNPJ) = 1 
	PRINT ('Fornecedor Cadastrado')

ELSE INSERT FORNE(Razao_Social, CNPJ_FORN, Tip_Comp)
		VALUES (@Razao_Social, @CNPJ, @FLG_COMPRA)

	SET @FLG_COMPRA = IsNull(@FLG_COMPRA, 0)

	IF @FLG_COMPRA = 0

		DECLARE C_Forne CURSOR FOR
			SELECT
			ID_FORNE = (Select max(ID_FORNE) from FORNE)
		OPEN C_Forne
		FETCH NEXT FROM C_Forne INTO @IdForne
		WHILE @@FETCH_STATUS = 0
		BEGIN

			INSERT INTO WEB (SITE, ID_FORNE)
			VALUES (@SITE, @IdForne)
			FETCH NEXT FROM C_Forne INTO @IdForne
		END;

		CLOSE C_Forne
		DEALLOCATE C_Forne

	IF @FLG_COMPRA = 1

		DECLARE C_Forne CURSOR FOR
			SELECT 
				BR.ID_BAIRRO,
				CD.ID_CIDADE,
				ES.ID_ESTADO,
				ID_FORNE = (Select max(ID_FORNE) from FORNE)
			FROM ESTADO ES
				LEFT JOIN CIDADE CD ON ES.ID_ESTADO = CD.ID_ESTADO
				LEFT JOIN BAIRRO BR ON CD.ID_CIDADE = BR.ID_CIDADE
			WHERE ES.UF = @UF
			AND CD.Nome_Cidade = @Cidade
			AND BR.Nome_Bairro = @Bairro


		OPEN C_Forne
		FETCH NEXT FROM C_Forne INTO @IdBair, @IdCid, @IdEst, @IdForne
		WHILE @@FETCH_STATUS = 0
		BEGIN
			INSERT INTO LOGRAD (BR.ID_BAIRRO, CD.ID_CIDADE, ES.ID_ESTADO, RUA, NUMER, Complemento, ID_FORNE)
			VALUES (@IdBair, @IdCid, @IdEst, @Rua, @Numero, @Complemento, @IdForne)

			FETCH NEXT FROM C_Forne INTO @IdBair, @IdCid, @IdEst, @IdForne
		END;

		CLOSE C_Forne
		DEALLOCATE C_Forne

		
		
		
	
GO

