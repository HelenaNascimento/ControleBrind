USE [BD_BRIND]
GO

/****** Object:  Table [dbo].[HSPRC]    Script Date: 17/10/2024 14:29:25 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[HSPRC](
	[IdHSPRC] [int] IDENTITY(1,1) NOT NULL,
	[IdProduto] [int] NULL,
	[Dat_Entrada] [smalldatetime] NULL,
	[Vlr_Ent] [decimal](10, 2) NULL,
	[Vlr_Liq] [decimal](10, 2) NULL,
	[Vlr_Desc] [decimal](10, 2) NULL,
	[Cus_Med] [decimal] (10,2) NULL
PRIMARY KEY CLUSTERED 
(
	[IdHSPRC] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


