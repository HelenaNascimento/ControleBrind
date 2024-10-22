CREATE TABLE ITEN_ENT(
		IdItem_Ent INT IDENTITY(1,1) NOT NULL 
	  ,	[IdNota_Ent] INT NULL
      ,	[NF_Ent] INT NULL
      ,	[Dat_Entrada] SMALLDATETIME NULL
	  , [IdProduto] INT NULL
      , [Qtd_Item] INT NULL
	  , [Vlr_Bruto] DECIMAL(10,2) NULL
	  , [Vlr_Desc] DECIMAL (10,2) NULL
	  , [Id_Marca] Varchar(100) NULL
	  , [Modelo] Varchar (100)NUll
	  )