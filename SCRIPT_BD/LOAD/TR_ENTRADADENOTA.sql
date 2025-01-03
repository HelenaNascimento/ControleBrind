USE BD_BRIND
GO
SET ANSI_NULLS, QUOTED_IDENTIFIER ON
GO

CREATE TRIGGER [dbo].[TR_NFSCB_Insert] ON [dbo].[CB_ENT] WITH ENCRYPTION
FOR INSERT
NOT FOR REPLICATION
AS

-- comando p/ corrigir erro delphi/ado: record was changed by another user
SET NOCOUNT ON 

	DECLARE 
		@Num_Nota INT,
		@Chv_Acesso VARCHAR(44), 
		@Dat_Entrada SMALLDATETIME, 
		@ID_FORN INT, 
		@Valor_Bruto DECIMAL(10,2), 
		@Vlr_Desc DECIMAL(10,2), 
		@Per_Desconto DECIMAL(10,2), 
		@Outras_Dispesas DECIMAL(10,2), 
		@Qtd_Total INT, 
		@Vlr_Total DECIMAL(10,2), 
		@Observacao TEXT
	
	
	INSERT INTO CB_ENT (Num_Nota,Chv_Acesso, Dat_Entrada, ID_FORN, Valor_Bruto, Vlr_Desc, Per_Desconto, Outras_Dispesas, Qtd_Total, Vlr_Total, Observacao)
	VALUES (@Num_Nota, @Chv_Acesso, @Dat_Entrada, @ID_FORN, @Valor_Bruto, @Vlr_Desc, @Per_Desconto, @Outras_Dispesas, @Qtd_Total, @Vlr_Total, @Observacao)