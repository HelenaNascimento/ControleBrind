USE [BD_BRIND]
GO

/****** Object:  Table [dbo].[FORNE]    Script Date: 22/10/2024 12:41:53 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[FORNE](
	[IdFornecedor] [int] IDENTITY(1,1) NOT NULL,
	[Fantasia] [nvarchar](100) NOT NULL,
	[CNPJ_FORN] [char](14) NOT NULL,
	[Tip_Comp] [bit] NULL,
	[WEB] [text] NOT NULL,
	[Logradouro] [varchar](250) NULL,
	[Numero] [varchar](10) NULL,
	[Bairro] [varchar](50) NULL,
	[Cidade] [varchar](50) NULL,
	[UF] [char](2) NULL,
	[CEP] [int] NULL,
	[Complemento] [varchar](250) NULL,
PRIMARY KEY CLUSTERED 
(
	[IdFornecedor] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


