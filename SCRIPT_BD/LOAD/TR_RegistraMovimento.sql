USE BD_BRIND
GO


CREATE TRIGGER RegistrarMovimento
ON IT_ENT
AFTER INSERT
AS
BEGIN
    INSERT INTO MOVIM(ID_PROD, Qtd_Ent, Dat_Mov, Qtd_Atual)
    SELECT 
        i.ID_IT_ENT, 
        i.Qtd_Item, 
        GETDATE(),
        dbo.FN_CalculaSaldoEstoque(i.ID_IT_ENT, i.Qtd_Item) -- Calcula o saldo acumulado
    FROM Inserted i;
END;
