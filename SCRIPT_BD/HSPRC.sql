CREATE TABLE [dbo].[HSPRC](
	[ID_HSPRC] [int] IDENTITY(1,1) NOT NULL,
	[ID_PROD] [int] NULL,
	[Dat_Entrada] [smalldatetime] NULL,
	[Vlr_Ent] [decimal](10, 2) NULL,
	[Vlr_Liq] [decimal](10, 2) NULL,
	[Vlr_Desc] [decimal](10, 2) NULL,
	[Cus_Med] [decimal] (10,2) NULL
PRIMARY KEY CLUSTERED 
(
	[ID_HSPRC] ASC
))
GO