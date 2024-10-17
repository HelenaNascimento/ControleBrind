USE [PROD_2023]
GO

/****** Object:  Table [dbo].[PDVCB]    Script Date: 17/10/2024 09:30:37 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[PDVCB](
	[Numero] [int] NOT NULL,
	[Tip_Pedido] [varchar](1) NULL,
	[Status1] [varchar](1) NULL,
	[Status2] [varchar](1) NULL,
	[Bloqueio] [varchar](2) NULL,
	[Flg_JaFechado] [bit] NULL,
	[Flg_Calc] [bit] NOT NULL,
	[Qtd_ImpPnt] [int] NULL,
	[Cod_OrigemPdv] [varchar](2) NULL,
	[Cod_PedRem] [int] NULL,
	[Cod_PedCli] [varchar](20) NULL,
	[Flg_ComisNormal] [bit] NULL,
	[Per_ComVnd] [numeric](18, 8) NULL,
	[Flg_TabProgres] [bit] NULL,
	[Tip_Faturamento] [varchar](3) NULL,
	[Tip_Vencimento] [varchar](1) NULL,
	[Dat_Pedido] [smalldatetime] NULL,
	[Cod_SerNfs] [varchar](3) NULL,
	[Cod_NumNfsIni] [int] NULL,
	[Cod_NumNfsFim] [int] NULL,
	[Cod_Cliente] [int] NULL,
	[Cod_Funcionario] [int] NULL,
	[Num_Lote] [int] NULL,
	[Consumidor] [varchar](35) NULL,
	[Tip_Consumidor] [varchar](1) NULL,
	[Qtd_PrzMed] [numeric](18, 8) NULL,
	[Qtd_Parcela] [int] NULL,
	[Qtd_Intervalo] [int] NULL,
	[Flg_PrzProm] [bit] NULL,
	[Flg_VlrFinanc] [bit] NULL,
	[Cod_VendTlmkt] [int] NULL,
	[Cod_Vendedor] [int] NULL,
	[Cod_Agente] [int] NULL,
	[Cod_Transportadora] [int] NULL,
	[Cod_Rota] [int] NULL,
	[Cod_MicroReg] [int] NULL,
	[Cod_RegTri] [int] NULL,
	[Qtd_Itens] [int] NULL,
	[Qtd_ItensProm] [int] NULL,
	[Vlr_BasDscCom] [numeric](18, 8) NULL,
	[Vlr_BasPar] [numeric](18, 8) NULL,
	[Vlr_LiqItens] [numeric](18, 8) NULL,
	[Vlr_RepIcms] [numeric](18, 8) NULL,
	[Vlr_SubsTrib] [numeric](18, 8) NULL,
	[Vlr_DscTri] [numeric](18, 8) NULL,
	[Tip_DscPdv] [varchar](1) NULL,
	[Per_DescontoCom] [numeric](18, 8) NULL,
	[Per_DescontoFin] [numeric](18, 8) NULL,
	[C_VlrDesconto] [numeric](18, 8) NULL,
	[C_VlrPedido] [numeric](18, 8) NULL,
	[Observacao] [text] NULL,
	[Qtd_Volumes] [int] NULL,
	[Qtd_Peso] [numeric](18, 8) NULL,
	[Hor_Entrada] [smalldatetime] NULL,
	[Hor_Prenota] [smalldatetime] NULL,
	[Hor_Fatura] [smalldatetime] NULL,
	[Hor_Saida] [smalldatetime] NULL,
	[Cod_FunSeparador] [int] NULL,
	[Cod_FunConferidor] [int] NULL,
	[Cod_FunEmbalador] [int] NULL,
	[Flg_Credito] [int] NULL,
	[Msg_Bloqueio] [varchar](30) NULL,
	[Msg_NF] [varchar](50) NULL,
	[Nom_UsuDesbloq] [varchar](15) NULL,
	[Msg_JustDesbloq] [varchar](50) NULL,
	[Cod_Propos] [int] NULL,
	[Per_SubFat] [numeric](18, 8) NULL,
	[Usuario] [varchar](15) NULL,
	[Transacao] [smalldatetime] NULL,
	[Per_DsdOrc] [numeric](18, 0) NULL,
	[Cod_Prz] [int] NULL,
	[Hor_ConferIni] [smalldatetime] NULL,
	[Hor_ConferFim] [smalldatetime] NULL,
	[Cod_Digitador] [int] NULL,
	[Cod_GrpCli] [int] NULL,
	[Per_DscPrz] [numeric](18, 4) NULL,
	[Per_DscVis] [numeric](18, 4) NULL,
	[Qtd_Prz] [int] NULL,
	[Cod_TabPrc] [int] NULL,
	[Num_Referencia] [int] NULL,
	[Flg_GerArqNf] [bit] NULL,
	[Obs_NotFis] [text] NULL,
	[Cod_TipPrp] [varchar](3) NULL,
	[Obs_IntCtaRec] [text] NULL,
	[Num_CotPdv] [int] NULL,
	[Per_Rnt] [numeric](18, 4) NULL,
	[Cod_BlqRnt] [char](1) NULL,
	[Nom_UsuDesbloqRnt] [varchar](15) NULL,
	[Des_LayoutPalm] [varchar](16) NULL,
	[Flg_WMS] [bit] NULL,
	[Flg_CalCom] [bit] NULL,
	[Vlr_Comissao] [numeric](18, 4) NULL,
	[Vlr_ComTlmkt] [numeric](18, 4) NULL,
	[Val_ComTra] [numeric](18, 4) NULL,
	[Cod_BlqLic] [char](1) NULL,
	[Nom_UsuDesbloqLic] [varchar](15) NULL,
	[Num_ConReg] [int] NULL,
	[Est_ConReg] [varchar](2) NULL,
	[Ide_NotEmp] [varchar](20) NULL,
	[Per_ComOpe] [numeric](18, 4) NULL,
	[Qtd_PesBru] [numeric](18, 4) NULL,
	[Hor_Fechamento] [smalldatetime] NULL,
	[Hor_Liberacao] [smalldatetime] NULL,
	[Hor_DbqFin] [smalldatetime] NULL,
	[Hor_DbqLic] [smalldatetime] NULL,
	[Hor_DbqRnt] [smalldatetime] NULL,
	[Dat_LimEnvPrp] [smalldatetime] NULL,
	[Vlr_Frete] [numeric](18, 4) NULL,
	[Cod_PolCom] [varchar](25) NULL,
	[Id_PolCom] [int] NULL,
	[Vlr_Verba] [numeric](18, 4) NULL,
	[Ide_Contra] [varchar](40) NULL,
	[Cod_Contrato] [int] NULL,
	[Num_SequenciaCtr] [int] NULL,
	[Flg_GerCtrFal] [bit] NULL,
	[Flg_CriIteFec] [bit] NULL,
	[Hor_Cancel] [smalldatetime] NULL,
	[Nom_UsuCancel] [varchar](15) NULL,
	[Msg_JustCancel] [varchar](80) NULL,
	[Vlr_FrePrv] [numeric](18, 4) NULL,
	[Flg_GerPdvBon] [bit] NULL,
	[Num_PdvLig] [int] NULL,
	[Cod_MtvRej] [varchar](3) NULL,
	[Des_MtvRej] [varchar](40) NULL,
	[Per_FrePrv] [numeric](18, 4) NULL,
	[Cod_Gerencia] [int] NULL,
	[Per_ComGer] [numeric](18, 4) NULL,
	[Vlr_ComGer] [numeric](18, 4) NULL,
	[Cod_Supervisor] [int] NULL,
	[Per_ComSup] [numeric](18, 4) NULL,
	[Vlr_ComSup] [numeric](18, 4) NULL,
	[Cod_GerOpe] [int] NULL,
	[Per_ComGerOpe] [numeric](18, 4) NULL,
	[Vlr_ComGerOpe] [numeric](18, 4) NULL,
	[Cod_SupOpe] [int] NULL,
	[Per_ComSupOpe] [numeric](18, 4) NULL,
	[Vlr_ComSupOpe] [numeric](18, 4) NULL,
	[Vlr_VrbPar] [numeric](18, 4) NULL,
	[Vlr_VrbBon] [numeric](18, 4) NULL,
	[Des_LayoutPde] [varchar](25) NULL,
	[Flg_GerRetBon] [bit] NULL,
	[Des_Convenio] [varchar](30) NULL,
	[UF_PlaVei] [varchar](2) NULL,
	[Cod_PlaVei] [varchar](10) NULL,
	[Flg_PriFat] [bit] NULL,
	[Cod_PrjPde] [varchar](12) NULL,
	[Hor_ImpEtq] [smalldatetime] NULL,
	[Num_PrtOri] [int] NULL,
	[Vlr_SbtRes] [numeric](18, 8) NULL,
	[Tip_SaiPdv] [varchar](1) NULL,
	[Flg_MarkupCusCom] [bit] NULL,
	[Vlr_DscBon] [numeric](18, 4) NULL,
	[Ide_NumPregao] [varchar](20) NULL,
	[CodAnt] [int] NULL,
	[NovoCodigo] [int] NULL,
	[Cod_PedCmpCli] [varchar](20) NULL,
	[Flg_CnvDscIteDscGlb] [bit] NULL,
	[Cod_Estabe] [int] NOT NULL,
	[Cod_LayoutPde] [int] NULL,
	[Tip_RatBon] [varchar](1) NULL,
	[Vlr_IcmFcpDes] [numeric](18, 4) NULL,
	[Vlr_Despes] [numeric](18, 4) NULL,
	[Vlr_IcmParDes] [numeric](18, 4) NULL,
	[Vlr_IcmParRem] [numeric](18, 4) NULL,
	[Flg_UsaPbm] [bit] NULL,
	[Obs_IntFecPdv] [text] NULL,
	[Num_PdvPai] [int] NULL,
	[Num_PdvFilho] [int] NULL,
	[Per_MarBru] [numeric](18, 4) NULL,
	[Per_RntBru] [numeric](18, 4) NULL,
	[Cod_RamAtv] [int] NULL,
	[Vlr_DscBonDup] [numeric](18, 4) NULL,
	[Sta_IntWms] [varchar](1) NULL,
	[Cod_MtvDbq] [varchar](6) NULL,
	[Flg_CtrUsuPdv] [bit] NULL,
	[Inscricao_Suframa] [varchar](9) NULL,
	[Vlr_IcmsDeson] [numeric](18, 4) NOT NULL,
	[Vlr_DscCalSuframa] [numeric](18, 4) NOT NULL,
	[Obs_Padrao] [text] NULL,
	[Tip_Frete] [varchar](1) NULL,
	[Tip_GerVrb] [varchar](1) NULL,
	[Vlr_VrbVdr] [numeric](18, 4) NULL,
	[Vlr_VrbOpe] [numeric](18, 4) NULL,
	[Vlr_VrbSup] [numeric](18, 4) NULL,
	[Sta_SepLot] [varchar](1) NULL,
	[Flg_BlqDebVrbNotBon] [bit] NULL,
	[Id_Consig] [int] NULL,
	[Num_SeqDev] [smallint] NULL,
	[Id_IncFis] [smallint] NULL,
	[Vlr_DspExt] [numeric](18, 4) NULL,
	[Vlr_Ipi] [numeric](18, 4) NULL,
	[Flg_AltUnvItePdv] [bit] NULL,
	[Vlr_BasIrf] [numeric](18, 4) NULL,
	[Vlr_Irf] [numeric](18, 4) NULL,
	[ID_PVMCB] [int] NULL,
	[Vlr_BasCsl] [numeric](18, 4) NULL,
	[Vlr_Csl] [numeric](18, 4) NULL,
 CONSTRAINT [PK_PDVCB] PRIMARY KEY CLUSTERED 
(
	[Cod_Estabe] ASC,
	[Numero] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 80, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_JaFechado]  DEFAULT (0) FOR [Flg_JaFechado]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_Calc]  DEFAULT (0) FOR [Flg_Calc]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_ImpPnt]  DEFAULT (1) FOR [Qtd_ImpPnt]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_ComisNormal]  DEFAULT (0) FOR [Flg_ComisNormal]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_ComVnd]  DEFAULT (0) FOR [Per_ComVnd]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_TabProgres]  DEFAULT (0) FOR [Flg_TabProgres]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_PrzMed]  DEFAULT (0) FOR [Qtd_PrzMed]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_Parcela]  DEFAULT (0) FOR [Qtd_Parcela]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_Intervalo]  DEFAULT (0) FOR [Qtd_Intervalo]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_PrzPrzProm]  DEFAULT (0) FOR [Flg_PrzProm]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_VlrFinanc]  DEFAULT (0) FOR [Flg_VlrFinanc]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_Itens]  DEFAULT (0) FOR [Qtd_Itens]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_ItensProm]  DEFAULT (0) FOR [Qtd_ItensProm]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_BasDscCom]  DEFAULT (0) FOR [Vlr_BasDscCom]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_BasPar]  DEFAULT (0) FOR [Vlr_BasPar]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_LiqItens]  DEFAULT (0) FOR [Vlr_LiqItens]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_RepIcms]  DEFAULT (0) FOR [Vlr_RepIcms]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_SubsTrib]  DEFAULT (0) FOR [Vlr_SubsTrib]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_DscTri]  DEFAULT (0) FOR [Vlr_DscTri]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_DescontoCom]  DEFAULT (0) FOR [Per_DescontoCom]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_DescontoFin]  DEFAULT (0) FOR [Per_DescontoFin]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_C_VlrDesconto]  DEFAULT (0) FOR [C_VlrDesconto]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_C_VlrPedido]  DEFAULT (0) FOR [C_VlrPedido]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_Volumes]  DEFAULT (0) FOR [Qtd_Volumes]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_Peso]  DEFAULT (0) FOR [Qtd_Peso]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_DsdOrc]  DEFAULT (0) FOR [Per_DsdOrc]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_Prz]  DEFAULT (0) FOR [Cod_Prz]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_Digitador]  DEFAULT (0) FOR [Cod_Digitador]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_GrpCli]  DEFAULT (0) FOR [Cod_GrpCli]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_DscPrz]  DEFAULT (0) FOR [Per_DscPrz]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_DscVis]  DEFAULT (0) FOR [Per_DscVis]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_Prz]  DEFAULT (0) FOR [Qtd_Prz]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_TabPrc]  DEFAULT (0) FOR [Cod_TabPrc]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Num_Referencia]  DEFAULT (0) FOR [Num_Referencia]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_GerArqNf]  DEFAULT (0) FOR [Flg_GerArqNf]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Num_CotPdv]  DEFAULT (0) FOR [Num_CotPdv]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_Rnt]  DEFAULT (0) FOR [Per_Rnt]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_WMS]  DEFAULT (0) FOR [Flg_WMS]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_CalCom]  DEFAULT (0) FOR [Flg_CalCom]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_Comissao]  DEFAULT (0) FOR [Vlr_Comissao]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_ComTlmkt]  DEFAULT (0) FOR [Vlr_ComTlmkt]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Val_ComTra]  DEFAULT (0) FOR [Val_ComTra]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Num_ConReg]  DEFAULT (0) FOR [Num_ConReg]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_ComOpe]  DEFAULT (0) FOR [Per_ComOpe]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Qtd_PesBru]  DEFAULT (0) FOR [Qtd_PesBru]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_Frete]  DEFAULT (0) FOR [Vlr_Frete]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Id_PolCom]  DEFAULT (0) FOR [Id_PolCom]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_Verba]  DEFAULT (0) FOR [Vlr_Verba]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_Contrato]  DEFAULT (0) FOR [Cod_Contrato]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Num_SequenciaCtr]  DEFAULT (0) FOR [Num_SequenciaCtr]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_GerCtrFal]  DEFAULT (0) FOR [Flg_GerCtrFal]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_CriIteFec]  DEFAULT (0) FOR [Flg_CriIteFec]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_FrePrv]  DEFAULT ((0)) FOR [Vlr_FrePrv]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_GerPdvBon]  DEFAULT ((0)) FOR [Flg_GerPdvBon]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Num_PdvLig]  DEFAULT ((0)) FOR [Num_PdvLig]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_FrePrv]  DEFAULT ((0)) FOR [Per_FrePrv]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_Gerencia]  DEFAULT ((0)) FOR [Cod_Gerencia]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_ComGer]  DEFAULT ((0)) FOR [Per_ComGer]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_ComGer]  DEFAULT ((0)) FOR [Vlr_ComGer]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_Supervisor]  DEFAULT ((0)) FOR [Cod_Supervisor]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_ComSup]  DEFAULT ((0)) FOR [Per_ComSup]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_ComSup]  DEFAULT ((0)) FOR [Vlr_ComSup]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_GerOpe]  DEFAULT ((0)) FOR [Cod_GerOpe]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_ComGerOpe]  DEFAULT ((0)) FOR [Per_ComGerOpe]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_ComGerOpe]  DEFAULT ((0)) FOR [Vlr_ComGerOpe]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_SupOpe]  DEFAULT ((0)) FOR [Cod_SupOpe]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_ComSupOpe]  DEFAULT ((0)) FOR [Per_ComSupOpe]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_ComSupOpe]  DEFAULT ((0)) FOR [Vlr_ComSupOpe]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_VrbPar]  DEFAULT ((0)) FOR [Vlr_VrbPar]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_VrbBon]  DEFAULT ((0)) FOR [Vlr_VrbBon]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_GerRetBon]  DEFAULT ((0)) FOR [Flg_GerRetBon]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_PriFat]  DEFAULT ((0)) FOR [Flg_PriFat]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Num_PrtOri]  DEFAULT ((0)) FOR [Num_PrtOri]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_SbtRes]  DEFAULT ((0)) FOR [Vlr_SbtRes]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_MarkupCusCom]  DEFAULT ((0)) FOR [Flg_MarkupCusCom]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_DscBon]  DEFAULT ((0)) FOR [Vlr_DscBon]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_CnvDscIteDscGlb]  DEFAULT ((0)) FOR [Flg_CnvDscIteDscGlb]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_Estabe]  DEFAULT ((0)) FOR [Cod_Estabe]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_LayoutPde]  DEFAULT ((0)) FOR [Cod_LayoutPde]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_IcmFcpDes]  DEFAULT ((0)) FOR [Vlr_IcmFcpDes]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_Despes]  DEFAULT ((0)) FOR [Vlr_Despes]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_IcmParDes]  DEFAULT ((0)) FOR [Vlr_IcmParDes]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_IcmParRem]  DEFAULT ((0)) FOR [Vlr_IcmParRem]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Num_PdvPai]  DEFAULT ((0)) FOR [Num_PdvPai]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Num_PdvFilho]  DEFAULT ((0)) FOR [Num_PdvFilho]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_MarBru]  DEFAULT ((0)) FOR [Per_MarBru]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Per_RntBru]  DEFAULT ((0)) FOR [Per_RntBru]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Cod_RamAtv]  DEFAULT ((0)) FOR [Cod_RamAtv]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Vlr_DscBonDup]  DEFAULT ((0)) FOR [Vlr_DscBonDup]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Flg_CtrUsuPdv]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Vlr_IcmsDeson]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Vlr_DscCalSuframa]
GO

ALTER TABLE [dbo].[PDVCB] ADD  CONSTRAINT [DF_PDVCB_Flg_BlqDebVrbNotBon]  DEFAULT ((0)) FOR [Flg_BlqDebVrbNotBon]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Vlr_DspExt]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Vlr_Ipi]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Vlr_BasIrf]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Vlr_Irf]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Vlr_BasCsl]
GO

ALTER TABLE [dbo].[PDVCB] ADD  DEFAULT ((0)) FOR [Vlr_Csl]
GO

ALTER TABLE [dbo].[PDVCB]  WITH NOCHECK ADD  CONSTRAINT [FK_PDVCB_AGCOB] FOREIGN KEY([Cod_Agente])
REFERENCES [dbo].[AGCOB] ([Codigo])
GO

ALTER TABLE [dbo].[PDVCB] CHECK CONSTRAINT [FK_PDVCB_AGCOB]
GO

ALTER TABLE [dbo].[PDVCB]  WITH NOCHECK ADD  CONSTRAINT [FK_PDVCB_CLIEN] FOREIGN KEY([Cod_Cliente])
REFERENCES [dbo].[CLIEN] ([Codigo])
ON UPDATE CASCADE
ON DELETE CASCADE
NOT FOR REPLICATION 
GO

ALTER TABLE [dbo].[PDVCB] CHECK CONSTRAINT [FK_PDVCB_CLIEN]
GO

ALTER TABLE [dbo].[PDVCB]  WITH NOCHECK ADD  CONSTRAINT [FK_PDVCB_TRANS] FOREIGN KEY([Cod_Transportadora])
REFERENCES [dbo].[TRANS] ([Codigo])
ON UPDATE CASCADE
ON DELETE CASCADE
NOT FOR REPLICATION 
GO

ALTER TABLE [dbo].[PDVCB] CHECK CONSTRAINT [FK_PDVCB_TRANS]
GO

ALTER TABLE [dbo].[PDVCB]  WITH NOCHECK ADD  CONSTRAINT [FK_PDVCB_VENDE] FOREIGN KEY([Cod_Vendedor])
REFERENCES [dbo].[VENDE] ([Codigo])
GO

ALTER TABLE [dbo].[PDVCB] CHECK CONSTRAINT [FK_PDVCB_VENDE]
GO


