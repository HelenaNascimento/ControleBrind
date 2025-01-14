CREATE PROCEDURE PR_AtualizaEstoque
    @Qtd_Disp_Item INT,
	@ID_PROD INT
AS
BEGIN
    UPDATE PRODU
    SET Qtd_Dispon = @Qtd_Disp_Item
    WHERE
		ID_PROD = @ID_PROD
        
END;


