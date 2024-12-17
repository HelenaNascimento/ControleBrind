CREATE TRIGGER [dbo].TR_CadWeb_Fornecedor ON [dbo].WEB WITH ENCRYPTION
FOR INSERT
NOT FOR REPLICATION
AS

-- comando p/ corrigir erro delphi/ado: record was changed by another user
SET NOCOUNT ON 
DECLARE @SITE VARCHAR(80)

	INSERT WEB (SITE)
	VALUES (@SITE)
