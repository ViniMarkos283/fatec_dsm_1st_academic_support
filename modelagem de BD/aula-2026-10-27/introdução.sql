
-- =============================================
-- AULA 01 - INTRODUÇÃO AO SQL SERVER
-- =============================================


-- =============================================
-- 1. CRIAÇÃO DO BANCO DE DADOS
-- =============================================

CREATE DATABASE _Aula01;
GO

USE _Aula01;
GO


-- =============================================
-- 2. CRIAÇÃO DAS TABELAS
-- =============================================

-- TABELA: PAIS

CREATE TABLE pais (
    cd_pais INT NOT NULL,
    nm_pais VARCHAR(30) NOT NULL,
    abr_pais CHAR(5) NOT NULL,

    CONSTRAINT pk_pais PRIMARY KEY (cd_pais)
);
GO


-- TABELA: UF

CREATE TABLE uf (
    cd_uf INT NOT NULL,
    nm_uf VARCHAR(30) NOT NULL,
    abr_uf CHAR(2) NOT NULL,
    cd_pais INT NOT NULL,

    CONSTRAINT pk_uf PRIMARY KEY (cd_uf),

    CONSTRAINT fk_uf_pais FOREIGN KEY (cd_pais)
        REFERENCES pais(cd_pais)
);
GO


-- TABELA: CIDADE

CREATE TABLE cidade (
    cd_cidade INT NOT NULL,
    nm_cidade VARCHAR(30) NOT NULL,
    qtde_habitantes BIGINT NOT NULL,
    vlr_areaCidade DECIMAL(10,2),
    dt_criacaoCidade SMALLDATETIME,
    cd_uf INT NOT NULL,

    CONSTRAINT pk_cidade PRIMARY KEY (cd_cidade),

    CONSTRAINT fk_cidade_uf FOREIGN KEY (cd_uf)
        REFERENCES uf(cd_uf)
);
GO


-- TABELA: BAIRRO

CREATE TABLE bairro (
    cd_bairro INT NOT NULL,
    nm_bairro VARCHAR(30) NOT NULL,
    cd_cidade INT NOT NULL,

    CONSTRAINT pk_bairro PRIMARY KEY (cd_bairro),

    CONSTRAINT fk_bairro_cidade FOREIGN KEY (cd_cidade)
        REFERENCES cidade(cd_cidade)
);
GO


-- =============================================
-- 3. INSERÇÃO DE DADOS - INSERT
-- =============================================

-- INSERÇÕES INDIVIDUAIS

INSERT INTO pais (cd_pais, nm_pais, abr_pais)
VALUES (100, 'Brasil', 'BR');

INSERT INTO pais (cd_pais, nm_pais, abr_pais)
VALUES (110, 'Chile', 'CHL');

INSERT INTO pais (cd_pais, nm_pais, abr_pais)
VALUES (120, 'Australia', 'AUS');


-- VÁRIAS INSERÇÕES DE UMA VEZ

INSERT INTO pais (cd_pais, nm_pais, abr_pais)
VALUES
    (130, 'Uruguai', 'URU'),
    (140, 'Paraguai', 'PAR'),
    (150, 'Canadá', 'CAN'),
    (160, 'México', 'MEX');


-- INSERÇÃO SEM INFORMAR AS COLUNAS

INSERT INTO pais
VALUES (170, 'Japão', 'JPN');


-- =============================================
-- 4. CONSULTA DE DADOS - SELECT
-- =============================================

-- CONSULTAR TODOS OS PAÍSES

SELECT * FROM pais;

-- CONSULTAR TODOS OS ESTADOS

SELECT * FROM uf;

-- CONSULTAR TODOS OS REGISTROS DE UMA CIDADE

SELECT * FROM cidade;

-- CONSULTAR TODOS OS BAIRROS

SELECT * FROM bairro;


-- =============================================
-- 5. ATUALIZAÇÃO DE DADOS - UPDATE
-- =============================================

-- ATUALIZAR UM REGISTRO ESPECÍFICO

UPDATE pais
SET nm_pais = 'Brasil Atualizado'
WHERE cd_pais = 100;


-- ATUALIZAR TODOS OS REGISTROS

-- UPDATE pais
-- SET abr_pais = 'XXX';


-- =============================================
-- 6. REMOÇÃO DE DADOS - DELETE
-- =============================================

-- REMOVER UM REGISTRO ESPECÍFICO

DELETE FROM pais
WHERE cd_pais = 170;


-- REMOVER TODOS OS REGISTROS

-- DELETE FROM pais;


-- =============================================
-- 7. ALTERAÇÃO DE ESTRUTURA - ALTER TABLE
-- =============================================

-- ADICIONAR UMA COLUNA

ALTER TABLE bairro
ADD cd_teste INT;


-- ALTERAR O TIPO DE UMA COLUNA

ALTER TABLE bairro
ALTER COLUMN cd_teste BIGINT;


-- REMOVER UMA COLUNA

ALTER TABLE bairro
DROP COLUMN cd_teste;


-- =============================================
-- 8. EXCLUSÃO DE TABELAS - DROP TABLE
-- =============================================

-- DROP TABLE bairro;


-- =============================================
-- 9. EXCLUSÃO DO BANCO DE DADOS
-- =============================================

-- USE master;
-- GO
-- DROP DATABASE _Aula01;
