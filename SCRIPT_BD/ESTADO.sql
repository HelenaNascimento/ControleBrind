CREATE TABLE ESTADO (
    [ID_CIDADE] INT IDENTITY(1,1) NOT NULL,
    [UF] [VARCHAR](2) NOT NULL,
    [DESCRICAO] VARCHAR (80),
    [IBGE_EST] NUMERIC
PRIMARY KEY CLUSTERED 
(
	[ID_CIDADE] ASC
)) 