
CREATE TABLE [dbo].[NF_CB_SAI](
	[ID_CB_SAI] [int] IDENTITY(1,1) NOT NULL,
	[NUM_PED] [nvarchar](20) NOT NULL,
	[NUM_NOTA] [nvarchar](20) NOT NULL,
	[Dat_Saida] [date] NOT NULL,
	[ID_CLIEN] [int] NOT NULL,
	[Qtd_Total] [int] NOT NULL,	
	[Obs] [text] NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_CB_SAI] ASC
)) 

