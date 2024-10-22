USE [BD_BRIND]
GO

/****** Object:  Table [dbo].[NF_CB_ENT]    Script Date: 22/10/2024 12:21:25 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[NF_CB_ENT](
	[IdNota_Ent] [int] IDENTITY(1,1) NOT NULL,
	[NF_ENT] [nvarchar](20) NOT NULL,
	[Dat_Entrada] [date] NOT NULL,
	[Qtd_Total] [int] NOT NULL,
	[Vlr_Total] [decimal](18, 2) NOT NULL,
	[IdFornecedor] [int] NULL,
	[Vlr_Desc] [decimal](10, 2) NULL,
	[Chv_Acesso] [nvarchar](44) NULL,
	[Valor_Bruto] [decimal](18, 2) NOT NULL,
	[Desconto] [decimal](18, 2) NULL,
	[Outras_Dispesas] [decimal](18, 2) NULL,
PRIMARY KEY CLUSTERED 
(
	[IdNota_Ent] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[NF_CB_ENT]  WITH CHECK ADD FOREIGN KEY([IdFornecedor])
REFERENCES [dbo].[FORNE] ([IdFornecedor])
GO


