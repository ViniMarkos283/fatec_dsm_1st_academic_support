
--USE MASTER DROP DATABASE ProdutoTabelaPreco
CREATE  DATABASE  ProdutoTabelaPreco

USE ProdutoTabelaPreco

CREATE TABLE CLiente (
cd_cliente int not null,
nm_cliente VARCHAR(30) NOT NULL,
CONSTRAINT pk_cliente PRIMARY KEY (cd_cliente)
)

INSERT INTO Cliente (cd_cliente, nm_cliente) VALUES
(1, 'Jo�o Silva'),
(2, 'Mariana Chagas'),
(3, 'Carla Abreu'),
(4, 'Juka Ferreira'),
(5, 'Juliana Souza');

CREATE TABLE NaturezaOperacao (
cd_NaturezaOperacao int not null,
ds_NaturezaOperacao VARCHAR(30) NOT NULL,
CONSTRAINT pk_NaturezaOperacao PRIMARY KEY (cd_NaturezaOperacao)
)


-- Inserindo alguns dados de NaturezaOperacao (para uso nas Notas Fiscais)
INSERT INTO NaturezaOperacao (cd_NaturezaOperacao, ds_NaturezaOperacao) VALUES
(1, 'Venda'),
(2, 'Devolu��o'),
(3, 'Troca');


CREATE TABLE ClassificacaoProduto (
cd_ClassificacaoProduto int not null,
ds_ClassificacaoProduto VARCHAR(30) NOT NULL,
abr_ClassificacaoProduto  CHAR(2) NOT NULL,
CONSTRAINT pk_ClassificacaoProduto PRIMARY KEY (cd_ClassificacaoProduto)
)

INSERT INTO ClassificacaoProduto (cd_ClassificacaoProduto, ds_ClassificacaoProduto, abr_ClassificacaoProduto) VALUES
(1, 'Alimentos', 'AL'),  -- Classifica��o 1
(2, 'Eletrodom�sticos', 'ED'),  -- Classifica��o 2
(3, 'Eletr�nicos', 'EL'),  -- Classifica��o 3
(4, 'M�veis', 'MO'),  -- Classifica��o 4
(5, 'Vestu�rio', 'VE');  -- Classifica��o 5

CREATE TABLE UnidadeMedida (
cd_UnidadeMedida int not null,
ds_UnidadeMedida VARCHAR(30) NOT NULL,
abr_UnidadeMedida  CHAR(2) NOT NULL,
CONSTRAINT pk_UnidadeMedida PRIMARY KEY (cd_UnidadeMedida)
)

INSERT INTO UnidadeMedida (cd_UnidadeMedida, ds_UnidadeMedida, abr_UnidadeMedida) VALUES
(1, 'Kilograma', 'kg'),  -- Unidade de Medida de Peso
(2, 'Litro', 'L');       -- Unidade de Medida de Volume

CREATE TABLE Produto (
cd_Produto				int				not null,
nm_produto				varchar(30)		not null,
vlr_Peso                decimal(8,2)	not null,
cd_UnidadeMedidaPeso	int				not null,
vlr_Volume              decimal(8,2)	not null,
cd_UnidadeMedidaVolume	int				not null,
cd_ClassificacaoProduto int				not null,

CONSTRAINT pk_Produto                 PRIMARY KEY (cd_Produto),
CONSTRAINT fk_ProdutoUniMedPeso       FOREIGN KEY (cd_UnidadeMedidaPeso)
            REFERENCES  UnidadeMedida (cd_UnidadeMedida),
CONSTRAINT fk_ProdutoUniMedVolume      FOREIGN KEY (cd_UnidadeMedidaVolume)
            REFERENCES  UnidadeMedida (cd_UnidadeMedida),
CONSTRAINT fk_ProdutoClassificacaoProd FOREIGN KEY (cd_ClassificacaoProduto)
            REFERENCES  ClassificacaoProduto (cd_ClassificacaoProduto),
)
INSERT INTO Produto (cd_Produto, nm_produto, vlr_Peso, cd_UnidadeMedidaPeso, vlr_Volume, cd_UnidadeMedidaVolume, cd_ClassificacaoProduto) VALUES
(1, 'Arroz 5kg', 5.0, 1, 0.0, 2, 1),  -- Produto 1: Alimento - Arroz, Peso em kg
(2, 'Feij�o Preto 1kg', 1.0, 1, 0.0, 2, 1),  -- Produto 2: Alimento - Feij�o, Peso em kg
(3, 'Detergente Yp� 500ml', 0.0, 1, 0.5, 2, 4),  -- Produto 3: Limpeza - Detergente, Volume em Litros
(4, 'Refrigerante Coca-Cola 2L', 0.0, 1, 2.0, 2, 3),  -- Produto 4: Bebida - Refrigerante, Volume em Litros
(5, 'Leite Integral 1L', 1.0, 1, 1.0, 2, 1);  -- Produto 5: Alimento - Leite, Volume em Litros


CREATE TABLE ProdutoComposto (
cd_ProdutoComposto      int             not null,
cd_Produto				int				not null,
cd_ProdutoComposicao	int				not null,
qtde_produtocomposicao  int             not null,
CONSTRAINT pk_ProdutoComposto       PRIMARY KEY (cd_ProdutoComposto),
CONSTRAINT fk_ProdutoComposto_Prod  FOREIGN KEY (cd_Produto)
          REFERENCES Produto (cd_produto),
CONSTRAINT fk_ProdutoComposto_ProdComp  FOREIGN KEY (cd_ProdutoComposicao)
          REFERENCES Produto (cd_produto)
)



CREATE TABLE ProdutoTabelaPreco (
cd_ProdutoTabelaPreco   int             not null,
cd_Produto				int				not null,
vlr_Produto       		decimal(10,2)		not null,
dt_InicioValidade		smalldatetime      not null,
dt_FimValidade	        smalldatetime,
CONSTRAINT pk_ProdutoTabelaPreco       PRIMARY KEY (cd_ProdutoTabelaPreco),
CONSTRAINT fk_Produto  FOREIGN KEY (cd_Produto)
          REFERENCES Produto (cd_produto),
)

CREATE TABLE NF (
cd_NF				int not null,
dt_NF				smalldatetime not null,
vlr_NF				decimal (12,2) not null,
cd_cliente			int not null,
cd_NaturezaOperacao int not null,

CONSTRAINT pk_NF PRIMARY KEY (cd_NF),
CONSTRAINT fk_NFCliente FOREIGN KEY (cd_cliente) 
    REFERENCES cliente (cd_cliente),
CONSTRAINT fk_NFcd_NaturezaOperacao FOREIGN KEY (cd_NaturezaOperacao) 
    REFERENCES NaturezaOperacao (cd_NaturezaOperacao)
)

CREATE TABLE NFItens (
cd_NFItens				int				not null,
cd_nf					int				not null,
cd_ProdutoTabelaPreco   int				not null,
qtde_produto            decimal(10,2)	not null,
CONSTRAINT pk_NFItens primary key (cd_NFItens),
CONSTRAINT fk_pk_NFItensNF FOREIGN KEY (cd_nf)
     REFERENCES NF (cd_nf),
CONSTRAINT fk_pk_NFProdTabPreco FOREIGN KEY (cd_ProdutoTabelaPreco)
     REFERENCES ProdutoTabelaPreco (cd_ProdutoTabelaPreco)
)