
USE BD_BRIND
GO

CREATE FUNCTION FN_CalculaSaldoEstoque
(
    @ItemID INT,
    @NovaQuantidade DECIMAL(10, 2)
)
RETURNS DECIMAL(10, 2)
AS
BEGIN
    DECLARE @SaldoAnterior DECIMAL(10, 2);
    
    -- Obtém o saldo anterior do item (ou 0 se não houver registros anteriores)
    SELECT @SaldoAnterior = ISNULL(MAX(Qtd_Atual), 0)
    FROM MOVIM
    WHERE ID_PROD = @ItemID;
    
    -- Retorna o saldo atualizado
    RETURN @SaldoAnterior + @NovaQuantidade;
END;
