

CREATE TABLE [dbo].[CB_ENT](
	[ID_CB_ENT] [int] IDENTITY(1,1) NOT NULL,
	[Num_Nota] [nvarchar](20) NOT NULL,
	[Chv_Acesso] [nvarchar](44) NULL,
	[Dat_Entrada] [date] NOT NULL,
	[ID_FORN] [int] NULL,
	[Valor_Bruto] [decimal](18, 2) NOT NULL,
	[Vlr_Desc] [decimal](10, 2) NULL,
	[Per_Desconto] [decimal](18, 2) NULL,
	[Outras_Dispesas] [decimal](18, 2) NULL,
	[Qtd_Total] [int] NOT NULL,
	[Vlr_Total] [decimal](18, 2) NOT NULL,
	[Observacao] [text]
PRIMARY KEY CLUSTERED 
(
	[ID_CB_ENT] ASC
))