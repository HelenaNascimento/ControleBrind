USE [BD_BRIND]
GO
CREATE TABLE [dbo].[MOVIM](
	[ID_MOV] INT IDENTITY(1,1) NOT NULL,
	[Dat_Mov] SMALLDATETIME NULL,
	[ID_PROD] INT NULL,
	[Qtd_Ent] INT NOT NULL,
	[Qtd_Sai] INT NOT NULL,
	[Qtd_Atual] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_MOV] ASC
)) 

