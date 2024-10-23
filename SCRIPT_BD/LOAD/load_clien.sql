INSERT INTO BD_BRIND.dbo.CLIEN (Razao_Social, CNPJ_CLIEN, COD_DMD, Tip_Cliente)
SELECT 
	distinct
	Razao_Social, 
	cnpj = 
		case 
			when Cgc_Cpf <> '' then Cgc_Cpf
			when Cgc_Cpf = '' then Cgf
		end,
	Codigo,
	Tipo_Consumidor
FROM PROD_2023.dbo.CLIEN CL
	JOIN  PROD_2023.dbo.ENXES ES ON CL.Codigo = ES.Cod_Client
WHERE Cod_Estabe = 1






