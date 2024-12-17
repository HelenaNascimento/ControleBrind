
CREATE PROCEDURE PR_CadastrarFornecedor 
	(	@Razao_Social  Varchar(80),
		@CNPJ VARCHAR(14),
		@FLG_COMPRA BIT,
		@SITE VARCHAR(80), 
		@IdBair int, 
		@IdCid int, 
		@IdEst int, 
		@UF VARCHAR(2),
		@Rua varchar(80), 
		@Numero int, 
		@Complemento varchar(80))

WITH ENCRYPTION
AS

SET NOCOUNT ON 

IF(select top 1 1 from FORNE where CNPJ_FORN = @CNPJ) = 1 
	PRINT ('Fornecedor Cadastrado')

ELSE INSERT FORNE(Razao_Social, CNPJ_FORN, Tip_Comp)
		VALUES (@Razao_Social, @CNPJ, @FLG_COMPRA)

	IF @FLG_COMPRA = 1
		
		EXEC TR_CadWeb_Fornecedor @SITE

	IF @FLG_COMPRA = 0

		DECLARE C_idEnt CURSOR FOR
			SELECT 
				BR.ID_BAIRRO,
				CD.ID_CIDADE,
				ES.ID_ESTADO
			FROM ESTADO ES
				LEFT JOIN CIDADE CD ON ES.ID_ESTADO = CD.ID_ESTADO
				LEFT JOIN BAIRRO BR ON CD.ID_CIDADE = BR.ID_CIDADE
			WHERE ES.UF = @UF

		OPEN C_idEnt
		FETCH NEXT FROM CursorProd INTO @IdBair, @IdCid, @IdEst
		WHILE @@FETCH_STATUS = 0
		BEGIN
			INSERT INTO LOGRAD (BR.ID_BAIRRO, CD.ID_CIDADE, ES.ID_ESTADO, RUA, NUMER, Complemento)
			VALUES (@IdBair, @IdCid, @IdEst, @Rua, @Numero, @Complemento)

			FETCH NEXT FROM CursorProd INTO @IdBair, @IdCid, @IdEst
		END;

		CLOSE C_idEnt
		DEALLOCATE C_idEnt

		
		
		
	