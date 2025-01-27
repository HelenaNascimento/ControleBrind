
USE BD_BRIND
GO

CREATE PROCEDURE PR_InserirDadosTabPrec
    @ID_PROD INT,
	@Dat_Entrada INT,
    @Vlr_Ent DECIMAL(10,2),
    @Vlr_Liq DECIMAL(10,2),
    @Vlr_Desc DECIMAL(10,2)
AS
BEGIN
	INSERT INTO HSPRC (ID_PROD, Dat_Entrada, Vlr_Ent, Vlr_Liq, Vlr_Desc)
	VALUES(@ID_PROD, @Dat_Entrada, @Vlr_Ent, @Vlr_Liq, @Vlr_Desc)

END;


