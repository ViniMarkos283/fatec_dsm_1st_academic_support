/*
    BANCO DE DADOS: ProdutoTabelaPreco
    Aula: INSERT, UPDATE, operadores logicos, filtros e datas
    SGBD: Microsoft SQL Server

    ATENCAO:
    - Execute em um banco novo.
    - O script cria o banco se ele ainda nao existir.
    - A atividade de promocao esta em uma secao separada e pode ser
      executada uma unica vez depois da carga inicial.
*/

-- ============================================================
-- 1. CRIACAO DO BANCO DE DADOS
-- ============================================================

-- USE MASTER;
-- DROP DATABASE ProdutoTabelaPreco;

IF DB_ID('ProdutoTabelaPreco') IS NULL
    CREATE DATABASE ProdutoTabelaPreco;


USE ProdutoTabelaPreco;


-- ============================================================
-- 2. CRIACAO DAS TABELAS
-- ============================================================

CREATE TABLE Cliente (
    cd_cliente INT NOT NULL,
    nm_cliente VARCHAR(30) NOT NULL,
    CONSTRAINT pk_cliente PRIMARY KEY (cd_cliente)
);


CREATE TABLE NaturezaOperacao (
    cd_NaturezaOperacao INT NOT NULL,
    ds_NaturezaOperacao VARCHAR(30) NOT NULL,
    CONSTRAINT pk_NaturezaOperacao PRIMARY KEY (cd_NaturezaOperacao)
);


CREATE TABLE ClassificacaoProduto (
    cd_ClassificacaoProduto INT NOT NULL,
    ds_ClassificacaoProduto VARCHAR(30) NOT NULL,
    abr_ClassificacaoProduto CHAR(2) NOT NULL,
    CONSTRAINT pk_ClassificacaoProduto PRIMARY KEY (cd_ClassificacaoProduto)
);


CREATE TABLE UnidadeMedida (
    cd_UnidadeMedida INT NOT NULL,
    ds_UnidadeMedida VARCHAR(30) NOT NULL,
    abr_UnidadeMedida CHAR(2) NOT NULL,
    CONSTRAINT pk_UnidadeMedida PRIMARY KEY (cd_UnidadeMedida)
);


CREATE TABLE Produto (
    cd_Produto INT NOT NULL,
    nm_produto VARCHAR(30) NOT NULL,
    vlr_Peso DECIMAL(8,2) NOT NULL,
    cd_UnidadeMedidaPeso INT NOT NULL,
    vlr_Volume DECIMAL(8,2) NOT NULL,
    cd_UnidadeMedidaVolume INT NOT NULL,
    cd_ClassificacaoProduto INT NOT NULL,

    CONSTRAINT pk_Produto PRIMARY KEY (cd_Produto),

    CONSTRAINT fk_ProdutoUniMedPeso
        FOREIGN KEY (cd_UnidadeMedidaPeso)
        REFERENCES UnidadeMedida (cd_UnidadeMedida),

    CONSTRAINT fk_ProdutoUniMedVolume
        FOREIGN KEY (cd_UnidadeMedidaVolume)
        REFERENCES UnidadeMedida (cd_UnidadeMedida),

    CONSTRAINT fk_ProdutoClassificacaoProd
        FOREIGN KEY (cd_ClassificacaoProduto)
        REFERENCES ClassificacaoProduto (cd_ClassificacaoProduto)
);


CREATE TABLE ProdutoComposto (
    cd_ProdutoComposto INT NOT NULL,
    cd_Produto INT NOT NULL,
    cd_ProdutoComposicao INT NOT NULL,
    qtde_produtocomposicao INT NOT NULL,

    CONSTRAINT pk_ProdutoComposto PRIMARY KEY (cd_ProdutoComposto),

    CONSTRAINT fk_ProdutoComposto_Prod
        FOREIGN KEY (cd_Produto)
        REFERENCES Produto (cd_Produto),

    CONSTRAINT fk_ProdutoComposto_ProdComp
        FOREIGN KEY (cd_ProdutoComposicao)
        REFERENCES Produto (cd_Produto)
);


CREATE TABLE ProdutoTabelaPreco (
    cd_ProdutoTabelaPreco INT NOT NULL,
    cd_Produto INT NOT NULL,
    vlr_Produto DECIMAL(10,2) NOT NULL,
    dt_InicioValidade SMALLDATETIME NOT NULL,
    dt_FimValidade SMALLDATETIME NULL,

    CONSTRAINT pk_ProdutoTabelaPreco
        PRIMARY KEY (cd_ProdutoTabelaPreco),

    CONSTRAINT fk_Produto
        FOREIGN KEY (cd_Produto)
        REFERENCES Produto (cd_Produto)
);


CREATE TABLE NF (
    cd_NF INT NOT NULL,
    dt_NF SMALLDATETIME NOT NULL,
    vlr_NF DECIMAL(12,2) NOT NULL,
    cd_cliente INT NOT NULL,
    cd_NaturezaOperacao INT NOT NULL,

    CONSTRAINT pk_NF PRIMARY KEY (cd_NF),

    CONSTRAINT fk_NFCliente
        FOREIGN KEY (cd_cliente)
        REFERENCES Cliente (cd_cliente),

    CONSTRAINT fk_NFcd_NaturezaOperacao
        FOREIGN KEY (cd_NaturezaOperacao)
        REFERENCES NaturezaOperacao (cd_NaturezaOperacao)
);


CREATE TABLE NFItens (
    cd_NFItens INT NOT NULL,
    cd_nf INT NOT NULL,
    cd_ProdutoTabelaPreco INT NOT NULL,
    qtde_produto DECIMAL(10,2) NOT NULL,

    CONSTRAINT pk_NFItens PRIMARY KEY (cd_NFItens),

    CONSTRAINT fk_pk_NFItensNF
        FOREIGN KEY (cd_nf)
        REFERENCES NF (cd_nf),

    CONSTRAINT fk_pk_NFProdTabPreco
        FOREIGN KEY (cd_ProdutoTabelaPreco)
        REFERENCES ProdutoTabelaPreco (cd_ProdutoTabelaPreco)
);


-- ============================================================
-- 3. INSERCAO DOS DADOS - INSERT
-- ============================================================

-- Clientes
INSERT INTO Cliente (cd_cliente, nm_cliente) VALUES
(1, 'Joao Silva'),
(2, 'Mariana Chagas'),
(3, 'Carla Abreu'),
(4, 'Juka Ferreira'),
(5, 'Juliana Souza');


-- Naturezas de operacao
INSERT INTO NaturezaOperacao (cd_NaturezaOperacao, ds_NaturezaOperacao) VALUES
(1, 'Venda'),
(2, 'Devolucao'),
(3, 'Troca');


-- Classificacoes dos produtos
INSERT INTO ClassificacaoProduto
(cd_ClassificacaoProduto, ds_ClassificacaoProduto, abr_ClassificacaoProduto) VALUES
(1, 'Alimentos', 'AL'),
(2, 'Eletrodomesticos', 'ED'),
(3, 'Eletronicos', 'EL'),
(4, 'Moveis', 'MO'),
(5, 'Vestuario', 'VE');


-- Unidades de medida
INSERT INTO UnidadeMedida
(cd_UnidadeMedida, ds_UnidadeMedida, abr_UnidadeMedida) VALUES
(1, 'Kilograma', 'kg'),
(2, 'Litro', 'L');


-- Produtos
INSERT INTO Produto
(cd_Produto, nm_produto, vlr_Peso, cd_UnidadeMedidaPeso,
 vlr_Volume, cd_UnidadeMedidaVolume, cd_ClassificacaoProduto) VALUES
(1, 'Arroz 5kg', 5.0, 1, 0.0, 2, 1),
(2, 'Feijao Preto 1kg', 1.0, 1, 0.0, 2, 1),
(3, 'Detergente Ype 500ml', 0.0, 1, 0.5, 2, 4),
(4, 'Refrigerante Coca-Cola 2L', 0.0, 1, 2.0, 2, 3),
(5, 'Leite Integral 1L', 1.0, 1, 1.0, 2, 1);


-- Composicoes de produtos
INSERT INTO ProdutoComposto
(cd_ProdutoComposto, cd_Produto, cd_ProdutoComposicao, qtde_produtocomposicao) VALUES
(1, 1, 2, 2),
(2, 1, 5, 1);


-- ============================================================
-- 4. INSERCAO NA TABELA DE PRECOS
-- ============================================================

INSERT INTO ProdutoTabelaPreco
(cd_ProdutoTabelaPreco, cd_Produto, vlr_Produto,
 dt_InicioValidade, dt_FimValidade) VALUES
(1, 1, 25.90, GETDATE(), NULL),
(2, 2, 8.50, GETDATE(), NULL),
(3, 3, 3.99, GETDATE(), NULL),
(4, 4, 9.90, GETDATE(), NULL),
(5, 5, 5.50, GETDATE(), NULL);


-- Conferindo os precos cadastrados
SELECT *
FROM ProdutoTabelaPreco;


-- ============================================================
-- 5. UPDATE - ATUALIZANDO PRECOS E DATAS
-- ============================================================

-- Atualizando o preco e a data de inicio do feijao
UPDATE ProdutoTabelaPreco
SET vlr_Produto = 8.90,
    dt_InicioValidade = GETDATE()
WHERE cd_ProdutoTabelaPreco = 2;


-- Atualizando somente o preco do detergente
UPDATE ProdutoTabelaPreco
SET vlr_Produto = 4.50
WHERE cd_ProdutoTabelaPreco = 3;


-- Atualizando somente a data de inicio do refrigerante
UPDATE ProdutoTabelaPreco
SET dt_InicioValidade = GETDATE()
WHERE cd_ProdutoTabelaPreco = 4;


-- Conferindo as alteracoes
SELECT *
FROM ProdutoTabelaPreco;


-- IMPORTANTE:
-- Nunca execute UPDATE ou DELETE sem WHERE quando a intencao
-- for alterar ou excluir somente registros especificos.
--
-- Exemplo de comando perigoso (nao executar):
-- UPDATE ProdutoTabelaPreco
-- SET vlr_Produto = 10.00;
--
-- Exemplo correto:
UPDATE ProdutoTabelaPreco
SET vlr_Produto = 10.00
WHERE cd_ProdutoTabelaPreco = 5;


-- ============================================================
-- 6. ATIVIDADE EXTRA - PROMOCAO DE UM DIA
-- ============================================================
-- Esta secao deve ser executada uma unica vez, depois da carga
-- inicial. O preco padrao do arroz e R$ 25,90 e o promocional
-- e R$ 19,90.
--
-- O preco normal termina no inicio da promocao.
-- O preco promocional termina amanha.
-- O preco normal volta a valer amanha, sem precisar de outro UPDATE.

DECLARE @Ara SMALLDATETIME = GETDATE();

DECLARE @Amanha SMALLDATETIME =
    DATEADD(DAY, 1, CONVERT(DATE, @Ara));

-- 1. Encerrando a validade do preco padrao
UPDATE ProdutoTabelaPreco
SET dt_FimValidade = @Ara
WHERE cd_ProdutoTabelaPreco = 1;

-- 2. Inserindo o preco promocional
INSERT INTO ProdutoTabelaPreco
(cd_ProdutoTabelaPreco, cd_Produto, vlr_Produto,
 dt_InicioValidade, dt_FimValidade)
VALUES
(6, 1, 19.90, @Ara, @Amanha);

-- 3. Cadastrando o preco padrao para o dia seguinte
INSERT INTO ProdutoTabelaPreco
(cd_ProdutoTabelaPreco, cd_Produto, vlr_Produto,
 dt_InicioValidade, dt_FimValidade)
VALUES
(7, 1, 25.90, @Amanha, NULL);


-- Historico de precos do arroz
SELECT *
FROM ProdutoTabelaPreco
WHERE cd_Produto = 1;


-- ============================================================
-- 7. AND, OR E NOT - OPERADORES LOGICOS
-- ============================================================

-- AND: as duas condicoes precisam ser verdadeiras
SELECT *
FROM Produto
WHERE vlr_Peso >= 1
AND cd_ClassificacaoProduto = 1;


-- OR: pelo menos uma condicao precisa ser verdadeira
SELECT *
FROM Produto
WHERE cd_ClassificacaoProduto = 1
OR cd_ClassificacaoProduto = 3;


-- NOT: inverte a condicao
SELECT *
FROM Produto
WHERE NOT cd_ClassificacaoProduto = 1;


-- ============================================================
-- 8. BETWEEN E NOT BETWEEN - INTERVALOS
-- ============================================================

-- BETWEEN: precos entre 5 e 20, incluindo os limites
SELECT *
FROM ProdutoTabelaPreco
WHERE vlr_Produto BETWEEN 5 AND 20;


-- NOT BETWEEN: precos fora do intervalo
SELECT *
FROM ProdutoTabelaPreco
WHERE vlr_Produto NOT BETWEEN 5 AND 20;


-- ============================================================
-- 9. IN E NOT IN - LISTA DE VALORES
-- ============================================================

-- IN: produtos das classificacoes 1, 3 e 5
SELECT *
FROM Produto
WHERE cd_ClassificacaoProduto IN (1, 3, 5);


-- NOT IN: produtos fora dessas classificacoes
SELECT *
FROM Produto
WHERE cd_ClassificacaoProduto NOT IN (1, 3, 5);


-- ============================================================
-- 10. LIKE E NOT LIKE - PESQUISA DE TEXTOS
-- ============================================================

-- Nomes que comecam com "Arroz"
SELECT *
FROM Produto
WHERE nm_produto LIKE 'Arroz%';


-- Nomes que terminam com "1kg"
SELECT *
FROM Produto
WHERE nm_produto LIKE '%1kg';


-- Nomes que contem "Coca" em qualquer posicao
SELECT *
FROM Produto
WHERE nm_produto LIKE '%Coca%';


-- Nomes que nao contem "Leite"
SELECT *
FROM Produto
WHERE nm_produto NOT LIKE '%Leite%';


-- Segundo caractere igual a "e"
SELECT *
FROM Produto
WHERE nm_produto LIKE '_e%';


-- ============================================================
-- 11. DATEDIFF - DIFERENCA ENTRE DATAS
-- ============================================================

-- Diferenca em dias
SELECT DATEDIFF(DAY, '2026-01-01', GETDATE()) AS diferenca_dias;


-- Diferenca em meses
SELECT DATEDIFF(MONTH, '2026-01-01', GETDATE()) AS diferenca_meses;


-- Diferenca em anos
SELECT DATEDIFF(YEAR, '2020-01-01', GETDATE()) AS diferenca_anos;


-- Consultando a validade dos precos em dias
SELECT
    cd_ProdutoTabelaPreco,
    vlr_Produto,
    dt_InicioValidade,
    dt_FimValidade,
    DATEDIFF(DAY, dt_InicioValidade, dt_FimValidade) AS dias_validade
FROM ProdutoTabelaPreco
WHERE dt_FimValidade IS NOT NULL;


-- ============================================================
-- 12. CONSULTAS COMPLEMENTARES DA TABELA DE PRECOS
-- ============================================================

-- Produtos com seus respectivos precos
SELECT
    Produto.cd_Produto,
    Produto.nm_produto,
    ProdutoTabelaPreco.vlr_Produto,
    ProdutoTabelaPreco.dt_InicioValidade,
    ProdutoTabelaPreco.dt_FimValidade
FROM Produto
INNER JOIN ProdutoTabelaPreco
    ON Produto.cd_Produto = ProdutoTabelaPreco.cd_Produto;


-- Precos atualmente validos
-- A data final e tratada como limite exclusivo.
SELECT *
FROM ProdutoTabelaPreco
WHERE GETDATE() >= dt_InicioValidade
AND (
    GETDATE() < dt_FimValidade
    OR dt_FimValidade IS NULL
);


-- Produtos com preco promocional vigente
SELECT
    Produto.nm_produto,
    ProdutoTabelaPreco.vlr_Produto,
    ProdutoTabelaPreco.dt_InicioValidade,
    ProdutoTabelaPreco.dt_FimValidade
FROM Produto
INNER JOIN ProdutoTabelaPreco
    ON Produto.cd_Produto = ProdutoTabelaPreco.cd_Produto
WHERE GETDATE() >= ProdutoTabelaPreco.dt_InicioValidade
AND GETDATE() < ProdutoTabelaPreco.dt_FimValidade;


-- ============================================================
-- 13. GENERALIZACAO E ESPECIALIZACAO - CONCEITO
-- ============================================================
-- Conteudo conceitual de modelagem de dados; nao e um comando SQL.
--
-- Generalizacao: reunir entidades semelhantes em uma entidade
-- mais abrangente.
--
-- Especializacao: dividir uma entidade generalista em entidades
-- mais especificas.
--
-- Heranca: entidades especialistas herdam os atributos da
-- entidade generalista e podem possuir atributos proprios.
--
-- Exemplo:
--
--                  Pessoa
--                     |
--             -----------------
--             |               |
--       Pessoa Fisica   Pessoa Juridica
