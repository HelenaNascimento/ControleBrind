CREATE PROCEDURE  PR_InserirMovItem
    @ID_PROD INT,
    @Qtd_Ent INT, 
    @Qtd_Sai INT
  
AS
BEGIN
	DECLARE     
	@Dat_Mov SMALLDATETIME = GETDATE()


    INSERT INTO MOVIM(DAT_MOV, ID_PROD, QTD_ENT, QTD_SAI)
    VALUES (@Dat_Mov, @ID_PROD, @Qtd_Ent, @Qtd_Sai)
END




