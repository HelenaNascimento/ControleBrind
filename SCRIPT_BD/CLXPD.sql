CREATE TABLE CLXPD (
    [ID_CLXPD] INT IDENTITY(1,1) NOT NULL,
    [ID_PED] INT NOT NULL,
    [ID_CLIEN] INT NOT NULL

PRIMARY KEY CLUSTERED 
(
	[ID_CLXPD] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO