INSERT INTO BD_BRIND.dbo.VEND(Nome_Guerra, COD_DMD)
SELECT 
	distinct
	Nome_Guerra, 
	Codigo
FROM PROD_2023.dbo.VENDE VD
	JOIN  PROD_2023.dbo.ENXES ES ON VD.Codigo = ES.Cod_Vendedor
WHERE Cod_Estabe = 1







