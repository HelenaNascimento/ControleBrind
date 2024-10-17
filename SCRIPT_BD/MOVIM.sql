USE [BD_BRIND]
GO

/****** Object:  Table [dbo].[MOVIM]    Script Date: 16/10/2024 18:40:33 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[MOVIM](
	[IdMov] [int] IDENTITY(1,1) NOT NULL,
	[IdNota_Ent] [int] NULL,
	[NF_Ent] [nvarchar](20) NULL,
	[Dat_Entrada] [date] NULL,
	[CNPJ_FORN] [char](14) NULL,
	[IdNota_Sai] [int] NULL,
	[NF_Sai] [nvarchar](20) NULL,
	[Dat_Saida] [date] NULL,
	[IdProduto] [int] NULL,
	[Qtd_Item] [int] NOT NULL,
	[Vlr_Item] [decimal](18, 2) NOT NULL,
	[IdVend] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[IdMov] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[MOVIM]  WITH CHECK ADD FOREIGN KEY([IdNota_Ent])
REFERENCES [dbo].[NF_CB_ENT] ([IdNota_Ent])
GO

ALTER TABLE [dbo].[MOVIM]  WITH CHECK ADD FOREIGN KEY([IdNota_Sai])
REFERENCES [dbo].[NF_CB_SAI] ([IdNota_Sai])
GO

ALTER TABLE [dbo].[MOVIM]  WITH CHECK ADD FOREIGN KEY([IdProduto])
REFERENCES [dbo].[PROD] ([IdProduto])
GO

ALTER TABLE [dbo].[MOVIM]  WITH CHECK ADD FOREIGN KEY([IdVend])
REFERENCES [dbo].[VEND] ([IdVend])
GO


