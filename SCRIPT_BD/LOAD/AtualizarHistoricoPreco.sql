USE dbo.BD_BRIND
GO

CREATE TRIGGER AtualizarHistoricoPreco
ON IT_ENT
AFTER INSERT
AS
BEGIN
    INSERT INTO HSPRC (ID_PROD, Dat_Entrada, Vlr_Ent, Vlr_Liq, Vlr_Desc, Cus_Med)
    SELECT 
        i.ID_IT_ENT, 
        i.Dat_Entrada, 
        i.Vlr_Bruto, 
        (i.Vlr_Bruto - i.Vlr_Desc), 
        i.Vlr_Desc,
        -- Cálculo do custo médio
        CASE 
            WHEN ISNULL(p.Qtd_Dispon, 0) = 0 THEN i.Vlr_Bruto -- Se não houver estoque anterior, o custo médio é o valor bruto
            ELSE 
                ((p.Qtd_Dispon * IsNull(h.Cus_Med, 0)) + (i.Qtd_Item * i.Vlr_Bruto)) / 
                (p.Qtd_Dispon + i.Qtd_Item) -- Fórmula de custo médio ponderado
        END AS Cus_Med
    FROM 
        Inserted i
    LEFT JOIN 
        PRODU p ON p.ID_PROD = i.ID_IT_ENT -- Relaciona com o estoque para obter quantidade e custo médio anteriores
	LEFT JOIN
		HSPRC h ON p.ID_PROD = h.ID_PROD 
END;
