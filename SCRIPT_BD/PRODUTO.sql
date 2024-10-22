USE [BD_BRIND]
GO

/****** Object:  Table [dbo].[PROD]    Script Date: 22/10/2024 12:48:30 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[PROD](
	[IdProduto] [int] IDENTITY(1,1) NOT NULL,
	[Descricao] [nvarchar](100) NOT NULL,
	[EAN] [char](13) NOT NULL,
	[IdForne] [int] NULL,
	[Qtd_Dispon] [int] NULL,
	[Cust_Med] [decimal](10, 2) NULL,
	[UltVlrCompra] [decimal](10, 2) NULL,
	[Dat_UltComp] [smalldatetime] NULL,
	[Marca] [varchar](50) NOT NULL,
	[Modelo] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[IdProduto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[PROD]  WITH CHECK ADD FOREIGN KEY([IdForne])
REFERENCES [dbo].[FORNE] ([IdFornecedor])
GO


