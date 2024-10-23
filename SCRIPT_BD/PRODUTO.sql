

CREATE TABLE [dbo].[PRODU](
	[ID_PROD] INT IDENTITY(1,1) NOT NULL,
	[Descricao] VARCHAR(100) NOT NULL,
	[EAN] VARCHAR(14) NOT NULL,
	[ID_FORNE] INT  NULL,
	[Qtd_Dispon] [int] NULL,
	[Cust_Med] [decimal](10, 2) NULL,
	[UltVlrCompra] [decimal](10, 2) NULL,
	[Dat_UltComp] [smalldatetime] NULL,
	[ID_Marca] [varchar](50) NOT NULL,
	[Modelo] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_PROD] ASC
)) 