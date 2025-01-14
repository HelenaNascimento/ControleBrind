CREATE PROCEDURE InserirItensNota
    @IdNota_Ent INT, 
    @NF_Ent INT, 
    @Dat_Entrada SMALLDATETIME, 
    @IdProduto INT, 
    @Qtd_Item INT, 
    @Vlr_Bruto DECIMAL(10,2), 
    @Vlr_Desc DECIMAL(10,2), 
    @Id_Marca VARCHAR(100), 
    @Modelo VARCHAR(100)
AS
BEGIN
    INSERT INTO IT_ENT(IdNota_Ent, NF_Ent, Dat_Entrada, IdProduto, Qtd_Item, Vlr_Bruto, Vlr_Desc, Id_Marca, Modelo)
    VALUES (@IdNota_Ent, @NF_Ent, @Dat_Entrada, @IdProduto, @Qtd_Item, @Vlr_Bruto, @Vlr_Desc, @Id_Marca, @Modelo);
END;


