-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 10.129.76.12
-- Tempo de geração: 03/04/2024 às 20:56
-- Versão do servidor: 5.6.26-log
-- Versão do PHP: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `notasmakschuh`
--
CREATE DATABASE IF NOT EXISTS `notasmakschuh` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `notasmakschuh`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `duplicatas`
--

CREATE TABLE `duplicatas` (
  `idDuplicata` int(11) NOT NULL,
  `idNota` int(11) NOT NULL,
  `numDuplicata` varchar(255) NOT NULL,
  `valor` varchar(255) NOT NULL,
  `venc` date NOT NULL,
  `pago` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `duplicatas`
--

INSERT INTO `duplicatas` (`idDuplicata`, `idNota`, `numDuplicata`, `valor`, `venc`, `pago`) VALUES
(45, 44, '000', '559.06', '2023-11-10', 1),
(46, 45, '000', '559.06', '2023-11-10', 1),
(47, 46, '000', '1502.06', '2023-11-10', 1),
(48, 47, '000', '339.16', '2023-11-10', 0),
(49, 48, '000', '1236.13', '2023-10-19', 0),
(50, 49, '000', '313.02', '2023-11-08', 0),
(51, 50, '000', '130.04', '2023-11-08', 1),
(52, 51, '000', '170.91', '2023-11-22', 0),
(53, 52, '000', '170.91', '2023-11-22', 1),
(54, 53, '000', '170.91', '2023-11-22', 1),
(55, 54, '000', '170.91', '2023-11-22', 1),
(56, 55, '000', '638.35', '2023-11-21', 1),
(57, 56, '000', '291.00', '2023-11-23', 0),
(58, 57, '001', '725.00', '2023-11-21', 1),
(59, 57, '002', '725.00', '2023-11-28', 1),
(60, 58, '000', '134.45', '2023-10-27', 0),
(61, 59, '000', '792.00', '2023-11-17', 0),
(62, 60, '000', '66.00', '2023-10-30', 0),
(63, 61, '000', '640.40', '2023-11-23', 1),
(64, 62, '001', '3272.00', '2023-11-26', 0),
(65, 62, '002', '3272.00', '2023-12-14', 1),
(66, 63, '000', '66.00', '2023-10-30', 0),
(67, 64, '000', '66.00', '2023-10-30', 0),
(68, 65, '000', '640.40', '2023-11-23', 0),
(69, 66, '001', '3272.00', '2023-11-26', 0),
(70, 66, '002', '3272.00', '2023-12-14', 1),
(71, 67, '000', '66.00', '2023-10-30', 0),
(72, 68, '000', '640.40', '2023-11-23', 0),
(73, 69, '001', '3272.00', '2023-11-26', 1),
(74, 69, '002', '3272.00', '2023-12-14', 0),
(75, 70, '000', '169.35', '2023-11-15', 0),
(76, 72, '000', '670.01', '2023-11-14', 0),
(77, 73, '000', '1924.00', '2023-10-18', 0),
(78, 74, '000', '172.75', '2023-11-15', 1),
(79, 75, '001', '517.34', '2023-11-16', 1),
(80, 75, '002', '516.00', '2023-11-22', 0),
(81, 76, '001', '722.54', '2023-12-14', 0),
(82, 76, '002', '720.38', '2023-12-21', 0),
(83, 76, '003', '720.38', '2023-12-28', 0),
(84, 77, '000', '364.37', '2023-12-14', 0),
(85, 78, '000', '316.63', '2023-12-08', 0),
(86, 79, '000', '733.60', '2023-12-22', 0),
(87, 80, '001', '1432.87', '2023-12-17', 0),
(88, 80, '002', '1012.00', '2024-01-14', 1),
(89, 80, '003', '1012.00', '2024-01-30', 1),
(90, 81, '000', '1269.14', '2023-12-19', 0),
(91, 82, '001', '1993.00', '2023-12-20', 0),
(92, 82, '002', '1993.00', '2024-01-19', 1),
(93, 83, '001', '752.86', '2023-12-18', 0),
(94, 83, '002', '752.86', '2023-12-25', 0),
(95, 84, '000', '453.75', '2023-12-07', 0),
(96, 85, '000', '425.14', '2023-12-26', 1),
(97, 86, '000', '264.00', '2024-01-08', 0),
(98, 87, '000', '180.60', '2023-12-26', 0),
(99, 88, '001', '561.53', '2023-12-25', 0),
(100, 88, '002', '559.86', '2024-01-01', 0),
(101, 88, '003', '559.86', '2024-01-08', 0),
(102, 89, '001', '701.48', '2023-12-27', 0),
(103, 89, '002', '699.39', '2024-01-03', 0),
(104, 89, '003', '699.39', '2024-01-10', 0),
(105, 90, '000', '1179.80', '2023-12-27', 0),
(106, 91, '000', '1079.00', '2024-04-16', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `empresas`
--

CREATE TABLE `empresas` (
  `idEmpresa` int(11) NOT NULL,
  `customNome` varchar(255) DEFAULT NULL,
  `nomeFantasia` varchar(255) DEFAULT NULL,
  `razaoSocial` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `empresas`
--

INSERT INTO `empresas` (`idEmpresa`, `customNome`, `nomeFantasia`, `razaoSocial`) VALUES
(1, 'WERK SCHOTT', 'WERK SCHOTT  NOVO HAMBURGO', 'WERK SCHOTT AUTOMATIZACAO PNEUMATICA LTDA'),
(2, 'UTILIDADES ELÉTRICAS', 'UE', 'UTILIDADES ELETRICAS COM. E IMP. LTDA'),
(3, 'WM', 'WM PNEUMATICA', 'WM PNEUMATICA LTDA'),
(4, 'REALIZA', NULL, 'REALIZA SERVICOS DE CROMAGEM LTDA ME'),
(5, NULL, 'METALURGICA JD', 'METALURGICA JD LTDA'),
(6, 'HIPPER TOOLS', 'HIPPER TOOLS IMPORTADORA', 'HIPPER TOOLS IMPORTADORA LTDA'),
(7, 'SULFRAN', 'SULFRAN AUTOMACAO INDL', 'SULFRAN IND COM SERV REPRES DE COMP ELETRICOS LTDA'),
(8, NULL, 'MERCADO ELETRONICO', 'MB3 - MERCADO ELETRONICO LTDA'),
(9, 'SAO JORGE', 'MULTIJATO SAO JORGE', 'JATO E PINTURA SAO JORGE EIRELI-EPP'),
(10, NULL, 'VEDASINOS', 'VEDASINOS COMERCIO DE VEDACOES EIRELI ME'),
(11, 'AÇOTEC', 'ACOTEC', 'ACOTEC INDUSTRIA DE PECAS PARA MAQUINAS LTDA.'),
(12, NULL, 'BEL AIR', 'BEL AIR PNEUMATICA LTDA'),
(13, 'DMBF', 'USMBRASIL', 'DMBF IND E COM DE PECAS E MAQUINAS EIRELI'),
(14, 'TECNOLAR', 'TECNOLAR-GM KASPER(IDEAL)', 'G M KASPER ELETROD.LTDA-TECNOLAR FILIAL 1'),
(15, 'MICRO', 'MICRO 01', 'MICROMECANICA IND. COM. IMP. E EXP. LTDA'),
(16, NULL, 'CHIPBYTE INFORMATICA LTDA', 'CHIPBYTE INFORMATICA LTDA'),
(17, NULL, 'TERMACO', 'TERMACO COM DE AC HID PNEU LTDA'),
(18, 'SISTEM', 'Sistem do Brasil Acessorios Pneumaticos Ltda.', 'Sistem do Brasil Acessorios Pneumaticos Ltda.'),
(19, 'CONTROL TECH', 'CONTROL TECH PORTO ALEGRE', 'CONTROL TECH INDUSTRIA E COMERCIO LTDA - FILIAL POA'),
(20, 'HAMBURGO', 'HAMBURGO PNEUMATICA', 'DAIANE BEATRIZ KUHN NUNES ME'),
(21, 'VISUS', 'VISUS INDUSTRIA ELETRONICA LTDA', 'VISUS INDUSTRIA ELETRONICA LTDA'),
(22, 'DIGITAL', 'DIGITAL PAINEIS E ETIQUETAS', 'DPE SOLUCOES GRAFICAS LTDA'),
(23, 'REALCENTER', NULL, 'REAL CENTER MATERIAIS E EQUIP. ELETR. LTDA');

-- --------------------------------------------------------

--
-- Estrutura para tabela `historicoPagamentos`
--

CREATE TABLE `historicoPagamentos` (
  `IDpg` int(11) NOT NULL,
  `IDduplicata` int(11) DEFAULT NULL,
  `idDupAdd` int(11) DEFAULT NULL,
  `adicionadoEm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `historicoPagamentos`
--

INSERT INTO `historicoPagamentos` (`IDpg`, `IDduplicata`, `idDupAdd`, `adicionadoEm`) VALUES
(3, 92, NULL, '2024-03-05 09:46:41'),
(4, 96, NULL, '2024-03-06 15:58:03'),
(5, 88, NULL, '2024-03-06 15:59:22'),
(6, 89, NULL, '2024-03-11 14:26:36');

-- --------------------------------------------------------

--
-- Estrutura para tabela `notaFiscalEntrada`
--

CREATE TABLE `notaFiscalEntrada` (
  `idNota` int(11) NOT NULL,
  `idEmail` int(11) NOT NULL,
  `remetente` varchar(255) NOT NULL,
  `assuntoEmail` varchar(255) NOT NULL,
  `dataEmail` datetime NOT NULL,
  `empresa` int(11) NOT NULL,
  `numeroNota` varchar(255) NOT NULL,
  `valorTotalNota` varchar(255) DEFAULT NULL,
  `natOp` int(11) NOT NULL,
  `dataEmissao` datetime NOT NULL,
  `adicionadoEm` datetime NOT NULL,
  `impresso` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `notaFiscalEntrada`
--

INSERT INTO `notaFiscalEntrada` (`idNota`, `idEmail`, `remetente`, `assuntoEmail`, `dataEmail`, `empresa`, `numeroNota`, `valorTotalNota`, `natOp`, `dataEmissao`, `adicionadoEm`, `impresso`) VALUES
(44, 19140, 'automatico.rs@werk-schott.com.br', 'ENVIO DE BOLETO 237 - Banco Bradesco', '2023-10-13 14:10:33', 1, '50662', '559.06', 3, '2023-10-13 14:01:08', '2023-10-24 10:58:02', 0),
(45, 19140, 'automatico.rs@werk-schott.com.br', 'ENVIO DE BOLETO 237 - Banco Bradesco', '2023-10-13 14:10:33', 1, '50662', '559.06', 3, '2023-10-13 14:01:08', '2023-10-24 10:58:38', 0),
(46, 19139, 'faturamento@utilidadeseletricas.com.br', 'NFe 83644', '2023-10-13 14:07:03', 2, '83644', '1502.06', 5, '2023-10-13 14:06:17', '2023-10-24 10:58:39', 0),
(47, 19137, 'faturamento.wmpneumatica@gmail.com', 'Emissão de NF-e nr 13674', '2023-10-13 11:22:29', 3, '13674', '339.16', 3, '2023-10-13 11:20:50', '2023-10-24 10:58:44', 0),
(48, 19134, 'nfe2022b@visualsul.com.br', 'Xmlnf 007522 de Realiza Serviços De Cromagem Ltda Me', '2023-10-12 15:07:59', 4, '7522', '3236.13', 7, '2023-10-12 15:07:13', '2023-10-24 10:58:46', 0),
(49, 19133, 'vendas@sul-ar.ind.br', 'Nota Fiscal Eletronica -      8181', '2023-10-11 17:11:30', 5, '8181', '313.02', 3, '2023-10-11 17:11:16', '2023-10-24 10:58:47', 0),
(50, 19129, 'nfe@hippertools.com.br', 'Emissão de NF-e - HIPPER TOOLS IMPORTADORA LTDA - 001000066389', '2023-10-11 14:46:33', 6, '66389', '130.04', 5, '2023-10-11 14:46:12', '2023-10-24 10:58:49', 0),
(51, 19226, 'nfe@hippertools.com.br', 'Emissão de NF-e - HIPPER TOOLS IMPORTADORA LTDA - 001000066653', '2023-10-25 13:56:38', 6, '66653', '170.91', 5, '2023-10-25 13:56:13', '2023-10-25 16:16:58', 0),
(52, 19226, 'nfe@hippertools.com.br', 'Emissão de NF-e - HIPPER TOOLS IMPORTADORA LTDA - 001000066653', '2023-10-25 13:56:38', 6, '66653', '170.91', 5, '2023-10-25 13:56:13', '2023-10-25 16:18:22', 0),
(53, 19226, 'nfe@hippertools.com.br', 'Emissão de NF-e - HIPPER TOOLS IMPORTADORA LTDA - 001000066653', '2023-10-25 13:56:38', 6, '66653', '170.91', 5, '2023-10-25 13:56:13', '2023-10-25 16:31:50', 0),
(54, 19226, 'nfe@hippertools.com.br', 'Emissão de NF-e - HIPPER TOOLS IMPORTADORA LTDA - 001000066653', '2023-10-25 13:56:38', 6, '66653', '170.91', 5, '2023-10-25 13:56:13', '2023-10-25 16:44:52', 0),
(55, 19220, 'logistica@sulfranautomacao.com.br', 'Emissão de NF-e - SULFRAN IND COM SERV REPR COMP E - 001000015665', '2023-10-24 17:14:39', 7, '15665', '638.35', 6, '2023-10-24 17:14:13', '2023-10-25 16:44:55', 0),
(56, 19215, 'contas@mb3me.com.br', 'NFe 092002', '2023-10-24 11:39:02', 8, '92002', '291.00', 5, '2023-10-24 11:38:43', '2023-10-25 16:44:56', 0),
(57, 19214, 'nfejatosaojorge@yahoo.com', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado 43231001918491000117550010000109901596688161', '2023-10-24 09:47:03', 9, '10990', '16450.00', 7, '2023-10-24 09:46:48', '2023-10-25 16:44:59', 0),
(58, 19207, 'sistema@vedasinos.com.br', 'VEDASINOS NFE Série 1 Número 72910 emitida no dia 20102023', '2023-10-20 17:13:14', 10, '72910', '134.45', 3, '2023-10-20 17:13:03', '2023-10-25 16:45:01', 0),
(59, 19206, 'gen@krafti.com.br', 'ACOTEC - NFe Número 1818', '2023-10-20 16:16:58', 11, '1818', '792.00', 3, '2023-10-20 16:16:56', '2023-10-25 16:45:03', 0),
(60, 19194, 'faturamento@belair.ind.br', 'Emissão de NF-e - BEL AIR PNEUMATICA LTDA - 001000190575', '2023-10-19 15:55:10', 12, '190575', '66.00', 3, '2023-10-19 15:55:04', '2023-10-25 17:34:18', 0),
(61, 19192, 'usmbrasil@gmail.com', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado 43231001972210000104550010000037741426428522', '2023-10-19 14:25:36', 13, '3774', '640.40', 3, '2023-10-19 14:21:56', '2023-10-25 17:34:19', 0),
(62, 19186, 'usmbrasil@gmail.com', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado 43231001972210000104550010000037721505238489', '2023-10-19 09:14:08', 13, '3772', '6544.00', 3, '2023-10-19 09:23:31', '2023-10-25 17:34:21', 0),
(63, 19194, 'faturamento@belair.ind.br', 'Emissão de NF-e - BEL AIR PNEUMATICA LTDA - 001000190575', '2023-10-19 15:55:10', 12, '190575', '66.00', 3, '2023-10-19 15:55:04', '2023-10-25 17:37:57', 0),
(64, 19194, 'faturamento@belair.ind.br', 'Emissão de NF-e - BEL AIR PNEUMATICA LTDA - 001000190575', '2023-10-19 15:55:10', 12, '190575', '66.00', 3, '2023-10-19 15:55:04', '2023-10-25 17:38:22', 0),
(65, 19192, 'usmbrasil@gmail.com', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado 43231001972210000104550010000037741426428522', '2023-10-19 14:25:36', 13, '3774', '640.40', 3, '2023-10-19 14:21:56', '2023-10-25 17:38:23', 0),
(66, 19186, 'usmbrasil@gmail.com', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado 43231001972210000104550010000037721505238489', '2023-10-19 09:14:08', 13, '3772', '6544.00', 3, '2023-10-19 09:23:31', '2023-10-25 17:38:25', 0),
(67, 19194, 'faturamento@belair.ind.br', 'Emissão de NF-e - BEL AIR PNEUMATICA LTDA - 001000190575', '2023-10-19 15:55:10', 12, '190575', '66.00', 3, '2023-10-19 15:55:04', '2023-10-25 17:39:07', 0),
(68, 19192, 'usmbrasil@gmail.com', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado 43231001972210000104550010000037741426428522', '2023-10-19 14:25:36', 13, '3774', '640.40', 3, '2023-10-19 14:21:56', '2023-10-25 17:39:08', 0),
(69, 19186, 'usmbrasil@gmail.com', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado 43231001972210000104550010000037721505238489', '2023-10-19 09:14:08', 13, '3772', '6544.00', 3, '2023-10-19 09:23:31', '2023-10-25 17:39:10', 0),
(70, 19179, 'nfe@hippertools.com.br', 'Emissão de NF-e - HIPPER TOOLS IMPORTADORA LTDA - 001000066509', '2023-10-18 14:20:11', 6, '66509', '169.35', 6, '2023-10-18 14:19:47', '2023-10-25 17:39:14', 0),
(71, 19176, 'nfefilial01@tecnolar.com.br', 'Emissão NF-e 6329', '2023-10-18 11:55:47', 14, '6329', '135.18', 5, '2023-10-18 11:54:50', '2023-10-25 17:39:16', 0),
(72, 19174, 'erp@microautomacao.com.br', 'MICRO 01 - NFe Nacional', '2023-10-18 10:34:04', 15, '55894', '670.01', 5, '2023-10-18 10:29:39', '2023-10-25 17:39:18', 0),
(73, 19173, 'chipbyte.pedidos.nfe@gmail.com', 'NFe 43231005467892000159550000000188211000159727 - CHIPBYTE INFORMATICA LTDA', '2023-10-18 10:23:12', 16, '18821', '1924.00', 5, '2023-10-18 10:23:04', '2023-10-25 17:39:19', 0),
(74, 19172, 'automatico.rs@werk-schott.com.br', 'ENVIO DE BOLETO 237 - Banco Bradesco', '2023-10-18 09:40:40', 1, '50818', '172.75', 3, '2023-10-18 09:38:17', '2023-10-25 17:39:21', 0),
(75, 19170, 'nfe.termaco@termaco.ind.br', 'Emissão de NF-e - TERMACO COM DE AC HID PNEU LTDA - 001000187312', '2023-10-18 08:39:11', 17, '187312', '1033.34', 6, '2023-10-18 08:38:52', '2023-10-25 17:39:22', 0),
(76, 19372, 'nfe@sistemdobrasil.com.br', 'Sistem do Brasil Acessorios Pneumaticos Ltda NF 33383100', '2023-11-16 10:29:17', 18, '33383', '2163.30', 3, '2023-11-16 10:29:09', '2023-11-16 12:52:15', 0),
(77, 19370, 'nfe@controltechnet.com.br', 'ARQUIVO XML E DANFE REF NF 9642 DE 16112023 DE CONTROL TECH INDUSTRIA E COMERCIO LTDA - FILIAL POA', '2023-11-16 08:46:33', 19, '9642', '364.37', 5, '2023-11-16 08:45:58', '2023-11-16 13:21:08', 0),
(78, 19349, 'sistema@vedasinos.com.br', 'VEDASINOS NFE Série 1 Número 73302 emitida no dia 10112023 ', '2023-11-10 14:20:34', 10, '73302', '316.63', 3, '2023-11-10 14:20:23', '2023-11-16 14:53:49', 0),
(79, 19389, 'usmbrasil@gmail.com', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado 43231101972210000104550010000039141215424213', '2023-11-17 07:28:03', 13, '3914', '733.60', 3, '2023-11-17 09:30:21', '2023-11-17 10:52:59', 0),
(80, 19414, 'automatico.rs@werk-schott.com.br', 'ENVIO DE BOLETO 237 - Banco Bradesco', '2023-11-21 02:41:28', 1, '52151', '3456.87', 5, '2023-11-20 15:37:53', '2023-11-21 14:01:40', 0),
(81, 19424, 'nfe.hamburgopneumatica@gmail.com', 'Emissão de NF-e nr 28916', '2023-11-21 14:42:16', 20, '28916', '1269.14', 3, '2023-11-21 14:41:57', '2023-11-22 10:19:05', 0),
(82, 19407, 'administrativo@visus.ind.br', 'Nota Fiscal Eletrônica nº 17411 De VISUS INDUSTRIA ELETRONICA LTDA', '2023-11-20 10:58:24', 21, '17411', '3986.00', 3, '2023-11-20 10:57:37', '2023-11-22 10:52:25', 0),
(83, 19395, 'nfe@digitalpainel.com.br', 'Nota Fiscal Eletrônica nº 17300 De DPE SOLUÇÕES GRAFICAS LTDA', '2023-11-20 09:21:33', 22, '17300', '1505.72', 3, '2023-11-20 09:20:38', '2023-11-22 11:13:00', 0),
(84, 19375, 'faturamento@belair.ind.br', 'Emissão de NF-e - BEL AIR PNEUMATICA LTDA - 001000191426', '2023-11-16 14:52:39', 12, '191426', '453.75', 5, '2023-11-16 14:52:33', '2023-11-22 12:41:22', 0),
(85, 19495, 'automatico.rs@werk-schott.com.br', 'ENVIO DE BOLETO 237 - Banco Bradesco', '2023-11-28 18:01:44', 1, '52536', '425.14', 3, '2023-11-28 17:30:37', '2023-11-29 14:22:52', 0),
(86, 19490, 'Faturamento - Utilidades Elétricas <faturamento@utilidadeseletricas.com.br>', 'NFe 85023', '2023-11-28 13:58:58', 2, '85023', '264.00', 5, '2023-11-28 13:53:00', '2023-11-29 14:47:47', 0),
(87, 19487, 'BEN HUR FELIPE BRUM OLIVEIRA <ben.oliveira@realcenter.com.br>', 'Nota Fiscal Eletronica - 229810', '2023-11-28 11:50:10', 23, '229810', '180.60', 5, '2023-11-28 11:50:03', '2023-11-29 15:35:28', 0),
(88, 19479, 'nfe@sistemdobrasil.com.br', 'Sistem do Brasil Acessorios Pneumaticos Ltda. NF 33462/100', '2023-11-27 14:58:33', 18, '33462', '1681.25', 3, '2023-11-27 14:58:26', '2023-11-29 15:39:17', 0),
(89, 19499, 'nfe@sistemdobrasil.com.br', 'Sistem do Brasil Acessorios Pneumaticos Ltda. NF 33483/100', '2023-11-29 14:53:21', 18, '33483', '2100.26', 3, '2023-11-29 14:53:14', '2023-11-29 15:39:38', 0),
(90, 19502, 'nfe@digitalpainel.com.br', 'Nota Fiscal Eletrônica nº 17397 De: DPE SOLUÇÕES GRAFICAS LTDA', '2023-11-29 16:17:00', 22, '17397', '1179.80', 3, '2023-11-29 16:11:45', '2023-11-30 10:03:41', 0),
(91, 20238, 'DMBF IND E COM DE PECAS E MAQUINAS EIRELI <usmbrasil@gmail.com>', 'Envio de Nota Fiscal Eletrônica, arquivo de nota fiscal anexado: 43240301972210000104550010000043391503053455', '2024-03-12 07:38:44', 13, '4339', '1079.00', 3, '2024-03-12 07:36:32', '2024-03-12 08:53:21', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `operacoes`
--

CREATE TABLE `operacoes` (
  `idOP` int(11) NOT NULL,
  `codigoOp` varchar(255) NOT NULL,
  `descricao` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `operacoes`
--

INSERT INTO `operacoes` (`idOP`, `codigoOp`, `descricao`) VALUES
(1, '5915', 'Remessa de mercadoria ou bem para conserto ou reparo'),
(2, '6915', 'Remessa de mercadoria ou bem para conserto ou reparo'),
(3, '5101', 'Venda de produção do estabelecimento'),
(4, '5656', 'Venda de combustível ou lubrificante adquirido ou recebido de terceiros destinado a consumidor ou usuário final'),
(5, '5102', 'Venda de mercadoria adquirida ou recebida de terceiros'),
(6, '5405', 'Venda de mercadoria adquirida ou recebida de terceiros em operação com mercadoria sujeita ao regime de substituição tributária, na condição de contribuinte substituído'),
(7, '5902', 'Retorno de mercadoria utilizada na industrialização por encomenda'),
(8, '6101', 'Venda de produção do estabelecimento'),
(9, '1120', 'Compra para industrialização, em venda à ordem, já recebida do vendedor remetente'),
(10, '6352', 'Prestação de serviço de transporte a estabelecimento industrial'),
(11, '6102', 'Venda de mercadoria adquirida ou recebida de terceiros'),
(12, '5124', 'Industrialização efetuada para outra empresa'),
(13, '5949', 'Outra saída de mercadoria ou prestação de serviço não especificado ');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pagamentosAdd`
--

CREATE TABLE `pagamentosAdd` (
  `idPagAdd` int(11) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `numero` varchar(255) DEFAULT NULL,
  `adicionadoEm` datetime DEFAULT NULL,
  `valor` varchar(255) NOT NULL,
  `vencimento` date NOT NULL,
  `pago` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `pagamentosAdd`
--

INSERT INTO `pagamentosAdd` (`idPagAdd`, `nome`, `numero`, `adicionadoEm`, `valor`, `vencimento`, `pago`) VALUES
(1, 'agua', NULL, '2024-04-01 21:51:45', '456', '2024-04-24', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `produtos`
--

CREATE TABLE `produtos` (
  `idItem` int(11) NOT NULL,
  `idNota` int(11) NOT NULL,
  `cProd` varchar(255) CHARACTER SET latin1 NOT NULL,
  `cEAN` varchar(255) CHARACTER SET latin1 NOT NULL,
  `xProd` varchar(255) CHARACTER SET latin1 NOT NULL,
  `CFOP` int(11) NOT NULL,
  `uCom` varchar(255) CHARACTER SET latin1 NOT NULL,
  `qCom` varchar(255) CHARACTER SET latin1 NOT NULL,
  `vUnCom` varchar(255) CHARACTER SET latin1 NOT NULL,
  `vProd` varchar(255) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Despejando dados para a tabela `produtos`
--

INSERT INTO `produtos` (`idItem`, `idNota`, `cProd`, `cEAN`, `xProd`, `CFOP`, `uCom`, `qCom`, `vUnCom`, `vProd`) VALUES
(1, 45, 'NCWE-A050A743810-0225-0000', 'SEM GTIN', 'CIL NCWE 50 DA DAM H.20 M20X1.5 MAGNETICO BASICO - 0225 - 0000', 3, 'PC', '2.0000', '279.53000000', '559.06'),
(2, 46, '004404', '4015082768454', 'CONTATOR DILM12-10 24VCC EATON', 5, 'PC', '4.0000', '131.93', '527.72'),
(3, 46, '000519', '4015080102137', 'CONTATOR DILEM-10-G 24VDC', 5, 'PC', '2.0000', '91.57', '183.14'),
(4, 46, '000921', '4015081479047', 'DISJUNTOR 4,5KA BFAZ4-C16/1-SA 16A UNIP. EATON', 5, 'PC', '2.0000', '11.94', '23.88'),
(5, 46, '014821', '7899112602218', 'BOTAO DUPLO ILUM. 24V 1NA+1NF P20IDL-Y7-1C METALTEX', 5, 'PC', '2.0000', '39.78', '79.56'),
(6, 46, '010565', '7899112600641', 'BOTAO RASO AZUL ILUM. 24VCC 1NA+1NF P20IGR-BL7-1C METALTEX', 5, 'PC', '1.0000', '49.51', '49.51'),
(7, 46, '010320', '7899112600504', 'BOTAO COGUMELO VERDE 1NA P20AMR-G-1A METALTEX', 5, 'PC', '1.0000', '27.29', '27.29'),
(8, 46, '005829', '7899912700893', 'CONTATO P/ BOTAO M20-1B 1NF METALTEX', 5, 'PC', '3.0000', '6.64', '19.92'),
(9, 46, '002840', '7899112600474', 'BOTAO EMERG. C/ RET. 1NF P20AKR-R-1B METALTEX', 5, 'PC', '1.0000', '23.03', '23.03'),
(10, 46, '008604', '7909158284214', 'RELE DE SEGURANCA CP-D EMERGENCIA WEG', 5, 'PC', '1.0000', '568.01', '568.01'),
(11, 47, '10076', 'SEM GTIN', 'CONEXAO RETA 1/8 X 10 - PLASTICA', 3, 'PC', '10.0000', '5.3700000000', '53.70'),
(12, 47, '15701', 'SEM GTIN', 'NIPLE 1/8 X 1/8 - ACO ZINCADO (XPSM 1/8 BSP)', 3, 'PC', '10.0000', '2.4600000000', '24.60'),
(13, 47, '15702', 'SEM GTIN', 'NIPLE 1/4 X 1/4 - LATAO', 3, 'PC', '10.0000', '4.4500000000', '44.50'),
(14, 47, '15609', 'SEM GTIN', 'BUCHA RED MF 1/2 X 3/8 - LATAO', 3, 'PC', '8.0000', '8.5900000000', '68.72'),
(15, 47, '26073', 'SEM GTIN', 'ESCAPE RAPIDO QUADRADO - 3/8', 3, 'PC', '4.0000', '32.8700000000', '131.48'),
(16, 47, '15801', 'SEM GTIN', 'LUVA 1/4 X 1/4 - LATAO', 3, 'PC', '4.0000', '4.0400000000', '16.16'),
(17, 48, '80', 'SEM GTIN', 'MAQUINA DE CONFORMAR CONTRAFORTES NF 3303', 7, 'UN', '1.0000', '2000.0000', '2000.00'),
(18, 48, 'M.OBRA', 'SEM GTIN', 'M.OBRA', 12, 'UN]', '1.0000', '1236.1300', '1236.13'),
(19, 49, '4', 'SEM GTIN', 'HASTE CROMADA 1045', 3, 'PC', '2.0000', '66.51000000', '133.02'),
(20, 49, '50027.02', 'SEM GTIN', 'EIXO O20X76 C/ROSC M8 PEG.CHAVE 17 1045', 3, 'PC', '6.0000', '30.00000000', '180.00'),
(21, 50, '2210014', 'SEM GTIN', 'ADESIVO TRAVA ROSCA 329 50GR - TORQUE ALTO', 5, 'UN', '1.000', '42.33', '42.33'),
(22, 50, '1015066', 'SEM GTIN', 'PORCA SEXTAVADA - M06 ZB', 6, 'CE', '1.000', '7.90', '7.90'),
(23, 50, '1015065', 'SEM GTIN', 'PORCA SEXTAVADA - M05 ZB', 6, 'CE', '1.000', '7.17', '7.17'),
(24, 50, '1016029', 'SEM GTIN', 'ARRUELA LISA M06 ZB', 5, 'CE', '1.000', '15.00', '15.00'),
(25, 50, '1016028', 'SEM GTIN', 'ARRUELA LISA M05 ZB', 5, 'CE', '1.000', '10.00', '10.00'),
(26, 50, '1013082', 'SEM GTIN', 'P SEXTAVADO M05X025 ZB RT', 6, 'CE', '0.200', '13.92', '2.78'),
(27, 50, '1013041', 'SEM GTIN', 'P SEXTAVADO 3/8X2 ZB RT', 6, 'CE', '0.080', '44.90', '3.59'),
(28, 50, '1015048', 'SEM GTIN', 'PORCA SEXTAVADA - 5/8\" ZB', 6, 'CE', '0.080', '160.00', '12.80'),
(29, 50, '1016058', 'SEM GTIN', 'ARRUELA PRESSAO M16 - 5/8 ZB', 5, 'CE', '0.080', '87.00', '6.96'),
(30, 50, '1010197', 'SEM GTIN', 'P ALLEN CILINDRICA M10X050', 6, 'CE', '0.160', '134.44', '21.51'),
(31, 51, '1350355', 'SEM GTIN', 'REBITE 3.2 X 12', 5, 'CE', '1.000', '9.90', '9.90'),
(32, 51, '1110640', 'SEM GTIN', 'BROCA 338 05.50 X 57 X 93 YG', 5, 'UN', '1.000', '13.90', '13.90'),
(33, 51, '1110158', 'SEM GTIN', 'BROCA 338 03.50 X 39 X 70 YG-1', 5, 'UN', '1.000', '7.50', '7.50'),
(34, 51, '1110206', 'SEM GTIN', 'BROCA 338 04.20 X 43 X 75 YG-1', 5, 'UN', '1.000', '9.00', '9.00'),
(35, 51, '1350268', 'SEM GTIN', 'PILHA ALCALINA AA C/2 - PEQUENA', 5, 'JG', '1.000', '12.00', '12.00'),
(36, 51, '1014015', 'SEM GTIN', 'P RM FENDA CHATA M04X012 ZB', 6, 'CE', '0.300', '9.00', '2.70'),
(37, 51, '1016010', 'SEM GTIN', 'ARRUELA LISA 04.76 - 3/16\" ZB', 5, 'CE', '0.500', '14.90', '7.45'),
(38, 51, '1015064', 'SEM GTIN', 'PORCA SEXTAVADA - M04 ZB', 6, 'CE', '1.000', '4.51', '4.51'),
(39, 51, '1016027', 'SEM GTIN', 'ARRUELA LISA M04 ZB', 5, 'CE', '1.000', '8.00', '8.00'),
(40, 51, '1111091', 'SEM GTIN', 'MACHO MANUAL M06 X 1.00 2PCS HT', 5, 'JG', '1.000', '84.00', '84.00'),
(41, 51, '1110266', 'SEM GTIN', 'BROCA 338 05.20 X 52 X 86 YG', 5, 'UN', '1.000', '11.9500', '11.95'),
(42, 52, '1350355', 'SEM GTIN', 'REBITE 3.2 X 12', 5, 'CE', '1.000', '9.90', '9.90'),
(43, 52, '1110640', 'SEM GTIN', 'BROCA 338 05.50 X 57 X 93 YG', 5, 'UN', '1.000', '13.90', '13.90'),
(44, 52, '1110158', 'SEM GTIN', 'BROCA 338 03.50 X 39 X 70 YG-1', 5, 'UN', '1.000', '7.50', '7.50'),
(45, 52, '1110206', 'SEM GTIN', 'BROCA 338 04.20 X 43 X 75 YG-1', 5, 'UN', '1.000', '9.00', '9.00'),
(46, 52, '1350268', 'SEM GTIN', 'PILHA ALCALINA AA C/2 - PEQUENA', 5, 'JG', '1.000', '12.00', '12.00'),
(47, 52, '1014015', 'SEM GTIN', 'P RM FENDA CHATA M04X012 ZB', 6, 'CE', '0.300', '9.00', '2.70'),
(48, 52, '1016010', 'SEM GTIN', 'ARRUELA LISA 04.76 - 3/16\" ZB', 5, 'CE', '0.500', '14.90', '7.45'),
(49, 52, '1015064', 'SEM GTIN', 'PORCA SEXTAVADA - M04 ZB', 6, 'CE', '1.000', '4.51', '4.51'),
(50, 52, '1016027', 'SEM GTIN', 'ARRUELA LISA M04 ZB', 5, 'CE', '1.000', '8.00', '8.00'),
(51, 52, '1111091', 'SEM GTIN', 'MACHO MANUAL M06 X 1.00 2PCS HT', 5, 'JG', '1.000', '84.00', '84.00'),
(52, 52, '1110266', 'SEM GTIN', 'BROCA 338 05.20 X 52 X 86 YG', 5, 'UN', '1.000', '11.9500', '11.95'),
(53, 53, '1350355', 'SEM GTIN', 'REBITE 3.2 X 12', 5, 'CE', '1.000', '9.90', '9.90'),
(54, 53, '1110640', 'SEM GTIN', 'BROCA 338 05.50 X 57 X 93 YG', 5, 'UN', '1.000', '13.90', '13.90'),
(55, 53, '1110158', 'SEM GTIN', 'BROCA 338 03.50 X 39 X 70 YG-1', 5, 'UN', '1.000', '7.50', '7.50'),
(56, 53, '1110206', 'SEM GTIN', 'BROCA 338 04.20 X 43 X 75 YG-1', 5, 'UN', '1.000', '9.00', '9.00'),
(57, 53, '1350268', 'SEM GTIN', 'PILHA ALCALINA AA C/2 - PEQUENA', 5, 'JG', '1.000', '12.00', '12.00'),
(58, 53, '1014015', 'SEM GTIN', 'P RM FENDA CHATA M04X012 ZB', 6, 'CE', '0.300', '9.00', '2.70'),
(59, 53, '1016010', 'SEM GTIN', 'ARRUELA LISA 04.76 - 3/16\" ZB', 5, 'CE', '0.500', '14.90', '7.45'),
(60, 53, '1015064', 'SEM GTIN', 'PORCA SEXTAVADA - M04 ZB', 6, 'CE', '1.000', '4.51', '4.51'),
(61, 53, '1016027', 'SEM GTIN', 'ARRUELA LISA M04 ZB', 5, 'CE', '1.000', '8.00', '8.00'),
(62, 53, '1111091', 'SEM GTIN', 'MACHO MANUAL M06 X 1.00 2PCS HT', 5, 'JG', '1.000', '84.00', '84.00'),
(63, 53, '1110266', 'SEM GTIN', 'BROCA 338 05.20 X 52 X 86 YG', 5, 'UN', '1.000', '11.9500', '11.95'),
(64, 54, '1350355', 'SEM GTIN', 'REBITE 3.2 X 12', 5, 'CE', '1.000', '9.90', '9.90'),
(65, 54, '1110640', 'SEM GTIN', 'BROCA 338 05.50 X 57 X 93 YG', 5, 'UN', '1.000', '13.90', '13.90'),
(66, 54, '1110158', 'SEM GTIN', 'BROCA 338 03.50 X 39 X 70 YG-1', 5, 'UN', '1.000', '7.50', '7.50'),
(67, 54, '1110206', 'SEM GTIN', 'BROCA 338 04.20 X 43 X 75 YG-1', 5, 'UN', '1.000', '9.00', '9.00'),
(68, 54, '1350268', 'SEM GTIN', 'PILHA ALCALINA AA C/2 - PEQUENA', 5, 'JG', '1.000', '12.00', '12.00'),
(69, 54, '1014015', 'SEM GTIN', 'P RM FENDA CHATA M04X012 ZB', 6, 'CE', '0.300', '9.00', '2.70'),
(70, 54, '1016010', 'SEM GTIN', 'ARRUELA LISA 04.76 - 3/16\" ZB', 5, 'CE', '0.500', '14.90', '7.45'),
(71, 54, '1015064', 'SEM GTIN', 'PORCA SEXTAVADA - M04 ZB', 6, 'CE', '1.000', '4.51', '4.51'),
(72, 54, '1016027', 'SEM GTIN', 'ARRUELA LISA M04 ZB', 5, 'CE', '1.000', '8.00', '8.00'),
(73, 54, '1111091', 'SEM GTIN', 'MACHO MANUAL M06 X 1.00 2PCS HT', 5, 'JG', '1.000', '84.00', '84.00'),
(74, 54, '1110266', 'SEM GTIN', 'BROCA 338 05.20 X 52 X 86 YG', 5, 'UN', '1.000', '11.9500', '11.95'),
(75, 55, '183', 'SEM GTIN', 'CS95-32 KIT DE REPARO KIT DE REPARO', 6, 'JG', '5.000', '50.5300', '252.65'),
(76, 55, '18664', 'SEM GTIN', 'CK95-32*BR KIT DE REPARO', 6, 'UN', '5.000', '77.1400', '385.70'),
(77, 56, 'MANGA224S', 'SEM GTIN', 'CABO MANGA  2X22AWG  1 PAR X 0,30MM SEM MALHA', 5, 'M', '50.0000', '3.1000000000', '155.00'),
(78, 56, 'Y-20', 'SEM GTIN', 'LUMINARIA ARTICULADA MAQUINA COSTURA 20 LEDS BIVOLT FIXACAO COM IMA  YOKE', 5, 'PC', '2.0000', '63.0000000000', '126.00'),
(79, 56, 'ANB10A', 'SEM GTIN', 'ADAPTADOR FEMEA 10A 2P+T X 2P NBR BRANCO', 5, 'PC', '2.0000', '5.0000000000', '10.00'),
(80, 57, '732', 'SEM GTIN', 'MAQUINA DE MONTAR BICOS', 7, 'PC', '1.0000', '15000.0000000000', '15000.00'),
(81, 57, '732', 'SEM GTIN', 'MAQUINA DE MONTAR BICOS', 12, 'PC', '1.0000', '1450.0000000000', '1450.00'),
(82, 58, '18549', 'SEM GTIN', '(RN438) GAXETA U', 3, 'PC', '2.0000', '20.0000000000', '40.00'),
(83, 58, '4161', 'SEM GTIN', '(F1799) RASPADOR PNEUMATICO 5/8\"\"', 3, 'PC', '2.0000', '11.0000000000', '22.00'),
(84, 58, '4316', 'SEM GTIN', '(8226) ANEL BACKUP', 6, 'CT', '0.0400', '233.5000000000', '9.34'),
(85, 58, '4145', 'SEM GTIN', '(F1778) GAXETA PNEUMATICA 2\"\"', 3, 'PC', '4.0000', '13.0000000000', '52.00'),
(86, 59, '130', 'SEM GTIN', 'EMBUCHAMENTO EIXO MARTELO.', 3, 'UND', '1.0000', '295.0000000000', '295.00'),
(87, 59, '1', 'SEM GTIN', 'USINADA EM REGUA COM GRAU', 3, 'UND', '1.0000', '75.0000000000', '75.00'),
(88, 59, '1', 'SEM GTIN', 'RECUPERAR PRATOS,SOLDA E USINAGEM', 3, 'UND', '2.0000', '30.0000000000', '60.00'),
(89, 59, '363', 'SEM GTIN', 'EIXO ROSCA M12 ACO 1045', 3, 'UND', '2.0000', '70.0000000000', '140.00'),
(90, 59, '12', 'SEM GTIN', 'PINO 20MM ROSCA M8', 3, 'UND', '6.0000', '26.0000000000', '156.00'),
(91, 59, '216', 'SEM GTIN', 'PINO BARRA ROSQUEADA M18 X 60', 3, 'UND', '3.0000', '22.0000000000', '66.00'),
(92, 60, '530188', 'SEM GTIN', 'KIT REP CIL MNI-ISO 025 KMI0251', 3, 'PC', '2.000', '33.0000', '66.00'),
(93, 61, '6817', 'SEM GTIN', 'CABECOTE OSCILANTE - CONS.', 3, 'PC', '1.0000', '236.0000000000', '236.00'),
(94, 61, '6706', 'SEM GTIN', 'CALCO DO CILINDRO', 3, 'PC', '1.0000', '62.6000000000', '62.60'),
(95, 61, '6707', 'SEM GTIN', 'CAMISA DO CILINDRO USM', 3, 'PC', '1.0000', '281.6000000000', '281.60'),
(96, 61, '6711', 'SEM GTIN', 'TAMPA CIL. CENTRO CINTA', 3, 'PC', '1.0000', '36.8000000000', '36.80'),
(97, 61, '6863', 'SEM GTIN', 'GUIA DA HASTE CIL. DA CINTA', 3, 'PC', '1.0000', '23.4000000000', '23.40'),
(98, 62, '6722', 'SEM GTIN', 'BLOCO INJETOR DE COLA', 3, 'PC', '2.0000', '1460.0000000000', '2920.00'),
(99, 62, '6816', 'SEM GTIN', 'SUPORTE DA FORMA SAPATO', 3, 'PC', '1.0000', '3624.0000000000', '3624.00'),
(100, 63, '530188', 'SEM GTIN', 'KIT REP CIL MNI-ISO 025 KMI0251', 3, 'PC', '2.000', '33.0000', '66.00'),
(101, 64, '530188', 'SEM GTIN', 'KIT REP CIL MNI-ISO 025 KMI0251', 3, 'PC', '2.000', '33.0000', '66.00'),
(102, 65, '6817', 'SEM GTIN', 'CABECOTE OSCILANTE - CONS.', 3, 'PC', '1.0000', '236.0000000000', '236.00'),
(103, 65, '6706', 'SEM GTIN', 'CALCO DO CILINDRO', 3, 'PC', '1.0000', '62.6000000000', '62.60'),
(104, 65, '6707', 'SEM GTIN', 'CAMISA DO CILINDRO USM', 3, 'PC', '1.0000', '281.6000000000', '281.60'),
(105, 65, '6711', 'SEM GTIN', 'TAMPA CIL. CENTRO CINTA', 3, 'PC', '1.0000', '36.8000000000', '36.80'),
(106, 65, '6863', 'SEM GTIN', 'GUIA DA HASTE CIL. DA CINTA', 3, 'PC', '1.0000', '23.4000000000', '23.40'),
(107, 66, '6722', 'SEM GTIN', 'BLOCO INJETOR DE COLA', 3, 'PC', '2.0000', '1460.0000000000', '2920.00'),
(108, 66, '6816', 'SEM GTIN', 'SUPORTE DA FORMA SAPATO', 3, 'PC', '1.0000', '3624.0000000000', '3624.00'),
(109, 67, '530188', 'SEM GTIN', 'KIT REP CIL MNI-ISO 025 KMI0251', 3, 'PC', '2.000', '33.0000', '66.00'),
(110, 68, '6817', 'SEM GTIN', 'CABECOTE OSCILANTE - CONS.', 3, 'PC', '1.0000', '236.0000000000', '236.00'),
(111, 68, '6706', 'SEM GTIN', 'CALCO DO CILINDRO', 3, 'PC', '1.0000', '62.6000000000', '62.60'),
(112, 68, '6707', 'SEM GTIN', 'CAMISA DO CILINDRO USM', 3, 'PC', '1.0000', '281.6000000000', '281.60'),
(113, 68, '6711', 'SEM GTIN', 'TAMPA CIL. CENTRO CINTA', 3, 'PC', '1.0000', '36.8000000000', '36.80'),
(114, 68, '6863', 'SEM GTIN', 'GUIA DA HASTE CIL. DA CINTA', 3, 'PC', '1.0000', '23.4000000000', '23.40'),
(115, 69, '6722', 'SEM GTIN', 'BLOCO INJETOR DE COLA', 3, 'PC', '2.0000', '1460.0000000000', '2920.00'),
(116, 69, '6816', 'SEM GTIN', 'SUPORTE DA FORMA SAPATO', 3, 'PC', '1.0000', '3624.0000000000', '3624.00'),
(117, 70, '1013152', 'SEM GTIN', 'P SEXTAVADO M10X020 ZB RT', 6, 'CE', '0.060', '98.80', '5.93'),
(118, 70, '1013158', 'SEM GTIN', 'P SEXTAVADO M10X030 ZB RT', 6, 'CE', '0.060', '79.90', '4.79'),
(119, 70, '1016053', 'SEM GTIN', 'ARRUELA PRESSAO M10 - 3/8 ZB', 5, 'CE', '0.300', '20.90', '6.27'),
(120, 70, '1212022', 'SEM GTIN', 'LIXA CORREIA 0440X035 #0036', 5, 'UN', '2.000', '6.50', '13.00'),
(121, 70, '1020049', 'SEM GTIN', 'BARRA ROSCADA M20 ZB', 5, 'UN', '1.000', '91.60', '91.60'),
(122, 70, '1015081', 'SEM GTIN', 'PORCA SEXTAVADA - M20 ZB', 6, 'CE', '0.060', '270.00', '16.20'),
(123, 70, '2612007', 'SEM GTIN', 'COPO PLASTICO AGUA 200ML/180ML C/100 BRANCO', 5, 'UN', '1.000', '7.76', '7.76'),
(124, 70, '2212019', 'SEM GTIN', 'OLEO DESENGRIPANTE HS 300ML', 5, 'UN', '2.000', '11.90', '23.80'),
(125, 71, '200542', '0606529661878', 'FITA P/SPLIT BRANCA PVC 10MT 100MM TECNOLAR ISOFITAS', 5, 'UN', '2.0000', '6.5000000000', '13.00'),
(126, 71, '12957', 'SEM GTIN', 'FITA ADESIVA SILVERTAPE 48MMX 5 MT PRATA', 5, 'UN', '2.0000', '10.0000000000', '20.00'),
(127, 71, '21645', 'SEM GTIN', 'FITA P/SPLIT ELASTOMERICA P/EMENDA C/10MT', 6, 'UN', '1.0000', '32.2500000000', '32.25'),
(128, 71, '336', '7898036318687', 'CANO COBRE 1/4', 6, 'KG', '0.5350', '99.9000000000', '53.45'),
(129, 71, '294', 'SEM GTIN', 'UNIAO BRONZE 1/4 X 1/4 SAE', 6, 'UN', '2.0000', '4.9900000000', '9.98'),
(130, 71, '200542', '0606529661878', 'FITA P/SPLIT BRANCA PVC 10MT 100MM TECNOLAR ISOFITAS', 5, 'UN', '1.0000', '6.5000000000', '6.50'),
(131, 72, '210005211001', 'SEM GTIN', 'VALV. 213 3/2 1/8 NF CONEX. LATERAL 10BAR 220V 50/60HZ', 5, 'UN', '1.0000', '314.42000000', '314.42'),
(132, 72, '103010264', 'SEM GTIN', 'VALVULA CORTE P/ CADEADO QBM4 1/2 GM', 5, 'UN', '1.0000', '355.59000000', '355.59'),
(133, 73, '000071', '7891230000716', 'BATERIA P/PLACA MAE CR2032 3V', 5, 'PC', '1.000', '3.600', '3.60'),
(134, 73, '161282', '842571111583', 'HD SSD HIKVISION 480GB HSSSDC100480G', 5, 'UN', '1.000', '179.100', '179.10'),
(135, 73, '168144', '735858445825', 'PROC. INTEL 1200 CORE I3-10100 3.6GHZ', 5, 'UN', '1.000', '755.100', '755.10'),
(136, 73, '171366', '7908414404199', 'MOUSE USB MULTILASER MO308 LARGE BOX PRETO', 5, 'UN', '1.000', '23.400', '23.40'),
(137, 73, '177399', '814914028797', 'MEMORIA DDR4 8GB 2666 PATRIOT VIPER ELITE II PVE248G266C6', 5, 'UN', '1.000', '152.100', '152.10'),
(138, 73, '181952', '7908639900285', 'GABINETE ATX C3TECH MT-31BK', 5, 'UN', '1.000', '161.100', '161.10'),
(139, 73, '183727', '4711081127765', 'PLACA MAE ASUS INTEL 1200 H510M-E PRIME', 5, 'UN', '1.000', '610.000', '610.00'),
(140, 73, '993425', '7898458703184', 'TECLADO USB MULTILASER TC065', 5, 'PC', '1.000', '39.600', '39.60'),
(141, 74, 'N18.3822-29', 'SEM GTIN', 'VAL.1/4 3V SOL DIF ATUAD PLAST 24 VCC CLASSE H', 3, 'PC', '1.0000', '106.82000000', '106.82'),
(142, 74, 'BMH024VCC', 'SEM GTIN', 'BOBINA MINI 024VCC IMPORTADA CLASSE H 5.5W', 5, 'PC', '5.0000', '12.18000000', '60.90'),
(143, 74, '20008', 'SEM GTIN', 'MOLA VALVULA SERIE 20.000', 3, 'PC', '5.0000', '0.91600000', '4.58'),
(144, 75, '775287', 'SEM GTIN', 'KIT MANG. 100R7/R14 C/ 700MM', 6, 'PC', '2.000', '66.18', '132.36'),
(145, 75, '68', 'SEM GTIN', 'KIT UNM 6X1/8 BSP COMPLETO', 6, 'PC', '2.000', '16.45', '32.90'),
(146, 75, '775355', 'SEM GTIN', 'KIT MANG. 100R7/R14 C/ 990MM', 6, 'PC', '8.000', '95.35', '762.80'),
(147, 75, '701585', 'SEM GTIN', 'AMJ4-MN4', 6, 'PC', '16.000', '6.58', '105.28'),
(148, 76, '104108', 'SEM GTIN', 'Con. reta 1/4\"BSP p/ mang 10mm', 3, 'UN', '5.0000', '7.1400000000', '35.70'),
(149, 76, '104088', 'SEM GTIN', 'Con. reta 1/4\"BSP p/ mang 8mm', 3, 'UN', '6.0000', '5.5000000000', '33.00'),
(150, 76, '204088', 'SEM GTIN', 'Con. em L 1/4\"BSP p/ mang 8mm', 3, 'UN', '20.0000', '10.5900000000', '211.80'),
(151, 76, '204108', 'SEM GTIN', 'Con. em L 1/4\"BSP p/ mang 10mm', 3, 'UN', '5.0000', '13.8200000000', '69.10'),
(152, 76, 'KD4068', 'SEM GTIN', 'Regulad.de Vel.p/Cilindro BSP 1/4 p/6mm', 3, 'UN', '20.0000', '17.0000000000', '340.00'),
(153, 76, '208068', 'SEM GTIN', 'Con. em L 1/8\"BSP p/ mang 6mm', 3, 'UN', '15.0000', '8.7900000000', '131.85'),
(154, 76, '108068', 'SEM GTIN', 'Con. reta 1/8\"BSP p/ mang 6mm', 3, 'UN', '5.0000', '4.8000000000', '24.00'),
(155, 76, '334088', 'SEM GTIN', 'Con. em T lateral 1/4\"BSP p/ mang 8mm', 3, 'UN', '10.0000', '15.2000000000', '152.00'),
(156, 76, 'S19040', 'SEM GTIN', 'Bujao cilindrico s/ oring 1/4\" sext ext.', 3, 'UN', '2.0000', '3.5600000000', '7.12'),
(157, 76, 'S10320', 'SEM GTIN', 'Nipel Conico 3/8 - 1/2', 3, 'UN', '2.0000', '9.1100000000', '18.22'),
(158, 76, 'Z32330', 'SEM GTIN', 'Con. em \"L\" macho-macho 3/8\"', 3, 'UN', '4.0000', '18.0800000000', '72.32'),
(159, 76, 'S14230', 'SEM GTIN', 'Reducao M conico- F cilindrica 1/2 - 3/8', 3, 'UN', '8.0000', '7.9000000000', '63.20'),
(160, 76, '203108', 'SEM GTIN', 'Con. em L 3/8\"BSP p/ mang 10mm', 3, 'UN', '16.0000', '15.4300000000', '246.88'),
(161, 76, 'Z30330', 'SEM GTIN', 'Con. em \"L\" Macho 3/8\"-F mea 3/8\"', 3, 'UN', '4.0000', '17.9300000000', '71.72'),
(162, 76, 'K188100', 'SEM GTIN', 'Distribuidor 5 Vias Tubo-Tubo 8-10mm', 3, 'UN', '5.0000', '8.7800000000', '43.90'),
(163, 76, 'K233100', 'SEM GTIN', 'Con. reta f mea 3/8 p/ mang 10mm', 3, 'UN', '8.0000', '7.0100000000', '56.08'),
(164, 76, 'K334107', 'SEM GTIN', 'Con. em T Lat. 1/4 p/ mang 10mm', 3, 'UN', '15.0000', '8.5200000000', '127.80'),
(165, 76, 'K700100', 'SEM GTIN', 'Uniao em T 10mm', 3, 'UN', '20.0000', '3.8400000000', '76.80'),
(166, 76, 'K334087', 'SEM GTIN', 'Con. em T Lat. 1/4 p/ mang 8mm', 3, 'UN', '15.0000', '7.0100000000', '105.15'),
(167, 76, 'K404087', 'SEM GTIN', 'Con. \"T\" Central BSP 1/4 p/ mang 8mm', 3, 'UN', '15.0000', '6.4600000000', '96.90'),
(168, 76, 'K203088', 'SEM GTIN', 'Con. em L 3/8 p/ mang 8mm', 3, 'UN', '30.0000', '4.7000000000', '141.00'),
(169, 77, '6197021653753263B', 'SEM GTIN', 'GAXETA MOLYTHANE 6043-B/66653 6197021653753263B', 5, 'UN', '20.00', '16.600000', '332.00'),
(170, 78, '15501', 'SEM GTIN', '(RN145) GAXETA U AN014 PK', 3, 'PC', '4.0000', '23.0000000000', '92.00'),
(171, 78, '4143', 'SEM GTIN', '(F1789) GAXETA PNEUMATICA 1.1/8\"\"', 3, 'PC', '2.0000', '18.2000000000', '36.40'),
(172, 78, '186', 'SEM GTIN', '(2214) ANEL ORING', 6, 'CT', '0.0200', '47.0000000000', '0.94'),
(173, 78, '4161', 'SEM GTIN', '(F1799) RASPADOR PNEUMATICO 5/8\"\"', 3, 'PC', '2.0000', '11.0000000000', '22.00'),
(174, 78, '93', 'SEM GTIN', '(2114) ANEL ORING', 6, 'CT', '0.0200', '22.0000000000', '0.44'),
(175, 78, '17415', 'SEM GTIN', '(8222) ANEL BACKUP', 6, 'CT', '0.0400', '180.0000000000', '7.20'),
(176, 78, '4517', 'SEM GTIN', '(92012) ANEL ORING D90', 6, 'CT', '0.3000', '25.0000000000', '7.50'),
(177, 78, '4160', 'SEM GTIN', '(F1532) RASPADOR PNEUMATICO 3/8\"\"', 3, 'PC', '2.0000', '15.5000000000', '31.00'),
(178, 78, '17', 'SEM GTIN', '(2011) ANEL ORING', 6, 'CT', '0.0200', '10.0000000000', '0.20'),
(179, 78, '4145', 'SEM GTIN', '(F1778) GAXETA PNEUMATICA 2\"\"', 3, 'PC', '2.0000', '13.5000000000', '27.00'),
(180, 78, '18549', 'SEM GTIN', '(RN438) GAXETA U', 3, 'PC', '1.0000', '20.0000000000', '20.00'),
(181, 78, '4161', 'SEM GTIN', '(F1799) RASPADOR PNEUMATICO 5/8\"\"', 3, 'PC', '1.0000', '11.0000000000', '11.00'),
(182, 78, '4316', 'SEM GTIN', '(8226) ANEL BACKUP', 6, 'CT', '0.0200', '233.5000000000', '4.67'),
(183, 78, '30501', 'SEM GTIN', '(RN1419) GAXETA UR7', 3, 'PC', '1.0000', '20.0000000000', '20.00'),
(184, 78, '20434', 'SEM GTIN', '(619701574-393) GAXETA 1812', 5, 'PC', '1.0000', '11.0000000000', '11.00'),
(185, 79, '6792', 'SEM GTIN', 'TAMPA DO CILINDRO DO ENCOSTO', 3, 'PC', '1.0000', '109.6000000000', '109.60'),
(186, 79, '116602', 'SEM GTIN', 'SUB-CONJ. PINCA C/DENTES M.CURVA', 3, 'CJ', '1.0000', '284.0000000000', '284.00'),
(187, 79, '4616', 'SEM GTIN', 'CABO DE COMANDO ABERT. PINCAS', 3, 'PC', '1.0000', '180.0000000000', '180.00'),
(188, 79, '108589', 'SEM GTIN', 'CINTA COURO P/CALC. MAQ. DVFZ', 3, 'PC', '2.0000', '80.0000000000', '160.00'),
(189, 80, 'RIP', 'SEM GTIN', 'VALVULA REDUTORA-REG PRESSAO MINI IMPORTADO', 5, 'PC', '80.0000', '40.87662500', '3270.13'),
(190, 80, 'BM210-14-1', 'SEM GTIN', 'VEDACAO BLOCO MANIFOLD 1/4', 3, 'PC', '24.0000', '3.02416667', '72.58'),
(191, 80, 'TGR314E', 'SEM GTIN', 'TORRE M14 GRANDE 3V IMPORT.', 5, 'PC', '2.0000', '55.19500000', '110.39'),
(192, 81, '70072', 'SEM GTIN', 'REGULADOR DE PRECISAO - 1/4 - 0,05 A 0,4 MPA', 3, 'PC', '2.0000', '455.6200000000', '911.24'),
(193, 81, '27016', 'SEM GTIN', 'PEDAL ELETRICO DRC-1M - SIMPLES SINAL', 3, 'PC', '5.0000', '55.5800000000', '277.90'),
(194, 81, '26024', 'SEM GTIN', 'DESLIZANTE 1/2 - VD 12', 3, 'PC', '2.0000', '40.0000000000', '80.00'),
(195, 82, '27972', 'SEM GTIN', 'CP432-030 (MAKSCHUH HORIZONTAL CONFORMAR ANIGER)', 3, 'UN', '2.0000', '1745.0000000000', '3490.00'),
(196, 82, '25853', 'SEM GTIN', 'REST-3,3_32VCC-5-250VCA', 3, 'PC', '8.0000', '62.0000000000', '496.00'),
(197, 83, '44426', 'SEM GTIN', 'MAKSCHUH 030', 3, 'PC', '1.0000', '139.4500000000', '139.45'),
(198, 83, '55228', 'SEM GTIN', 'MAKSCHUH 046', 3, 'PC', '1.0000', '45.0000000000', '45.00'),
(199, 83, '53271', 'SEM GTIN', 'MAKSCHUH 036B', 3, 'PC', '1.0000', '148.5000000000', '148.50'),
(200, 83, '44430', 'SEM GTIN', 'MAKSCHUH 037', 3, 'PC', '1.0000', '88.9000000000', '88.90'),
(201, 83, '55232', 'SEM GTIN', 'MAKSCHUH 045', 3, 'PC', '1.0000', '148.5000000000', '148.50'),
(202, 83, '44431', 'SEM GTIN', 'MAKSCHUH 038', 3, 'PC', '1.0000', '78.9000000000', '78.90'),
(203, 83, '55231', 'SEM GTIN', 'MAKSCHUH 044', 3, 'PC', '1.0000', '148.5000000000', '148.50'),
(204, 83, '55236', 'SEM GTIN', 'MAKSCHUH 1023', 3, 'PC', '60.0000', '3.5000000000', '210.00'),
(205, 83, '55237', 'SEM GTIN', 'MAKSCHUH 1024', 3, 'OC', '60.0000', '4.5000000000', '270.00'),
(206, 83, '55235', 'SEM GTIN', 'MAKSCHUH 2011', 3, 'CJ', '1.0000', '31.2000000000', '31.20'),
(207, 83, '61252', 'SEM GTIN', 'MAKSCHUH 1028', 3, 'PC', '1.0000', '8.8200000000', '8.82'),
(208, 83, '44196', 'SEM GTIN', 'MAKSCHUH 2002', 3, 'PC', '1.0000', '48.5000000000', '48.50'),
(209, 83, '44432', 'SEM GTIN', 'MAKSCHUH 039A', 3, 'PC', '1.0000', '139.4500000000', '139.45'),
(210, 84, '502237', 'SEM GTIN', 'VLV HDR 4/3V CT SOL/SOL 024VCC VH064333-2CT', 5, 'PC', '1.000', '453.7500', '453.75'),
(211, 85, 'SPN381N-29', 'SEM GTIN', 'VAL. SORVET. SOL./MOLA 3V 1/2 24 VCC CLASSE H', 3, 'PC', '2.0000', '212.57000000', '425.14'),
(212, 86, '007221', 'SEM GTIN', 'BOTAO DUPLO ILUM. 1NA+1NF 24V S2TR-P3WABD AUTONICS', 5, 'PC', '3.0000', '88.00', '264.00'),
(213, 87, '1347', 'SEM GTIN', 'CABO  COBRE CONTROLE 16X0,50MM2 500V VIAS COLORIDAS 70C PVC CL5 (RC210)(5601607PT)', 5, 'MT', '8.0000', '10.75', '86.00'),
(214, 87, '1337', 'SEM GTIN', 'CABO  COBRE CONTROLE 6X0,50MM2 VIAS COLORIDAS  (RC210)(C6X05CSB)', 5, 'MT', '11.0000', '4.45', '48.95'),
(215, 87, '66902', 'SEM GTIN', 'CABO  COBRE FLEXIVEL 4X1,0MM2 500V 70C PVC  (RC233)(B0175N-PT)', 5, 'MT', '11.0000', '4.15', '45.65'),
(216, 88, '104088', 'SEM GTIN', 'Con. reta 1/4\"BSP p/ mang 8mm', 3, 'UN', '30.0000', '5.5000000000', '165.00'),
(217, 88, '204088', 'SEM GTIN', 'Con. em L 1/4\"BSP p/ mang 8mm', 3, 'UN', '30.0000', '10.5900000000', '317.70'),
(218, 88, '104068', 'SEM GTIN', 'Con. reta 1/4\"BSP p/ mang 6mm', 3, 'UN', '20.0000', '5.4300000000', '108.60'),
(219, 88, 'FRL2210S20M', 'SEM GTIN', 'FRL Midi 1/2 10 BAR Dreno SA 20 m', 3, 'UN', '1.0000', '383.5000000000', '383.50'),
(220, 88, '104108', 'SEM GTIN', 'Con. reta 1/4\"BSP p/ mang 10mm', 3, 'UN', '10.0000', '7.1400000000', '71.40'),
(221, 88, '204108', 'SEM GTIN', 'Con. em L 1/4\"BSP p/ mang 10mm', 3, 'UN', '10.0000', '13.8200000000', '138.20'),
(222, 88, '334088', 'SEM GTIN', 'Con. em T lateral 1/4\"BSP p/ mang 8mm', 3, 'UN', '30.0000', '15.2000000000', '456.00'),
(223, 89, '408088', 'SEM GTIN', 'Con. em T central 1/8\"BSP p/ mang 8mm', 3, 'UN', '31.0000', '15.0600000000', '466.86'),
(224, 89, '208088', 'SEM GTIN', 'Con. em L 1/8\"BSP p/ mang 8mm', 3, 'UN', '25.0000', '10.3300000000', '258.25'),
(225, 89, '700100', 'SEM GTIN', 'Uniao em T p/ mang 10mm', 3, 'UN', '10.0000', '15.8800000000', '158.80'),
(226, 89, '204108', 'SEM GTIN', 'Con. em L 1/4\"BSP p/ mang 10mm', 3, 'UN', '16.0000', '13.8200000000', '221.12'),
(227, 89, '334068', 'SEM GTIN', 'Con. em T lateral 1/4\"BSP p/ mang 6mm', 3, 'UN', '13.0000', '14.3700000000', '186.81'),
(228, 89, '205068', 'SEM GTIN', 'Con. em L M5 p/ mang 6mm', 3, 'UN', '20.0000', '10.6400000000', '212.80'),
(229, 89, '958068', 'SEM GTIN', 'Valv. reguladora fluxo 1/8\"BSP 6mm', 3, 'UN', '12.0000', '45.5600000000', '546.72'),
(230, 90, '55235', 'SEM GTIN', 'MAKSCHUH 2011', 3, 'CJ', '1.0000', '31.2000000000', '31.20'),
(231, 90, '59313', 'SEM GTIN', 'MAKSCHUH 2002B', 3, 'CJ', '1.0000', '48.5000000000', '48.50'),
(232, 90, '59225', 'SEM GTIN', 'MAKSCHUH 050C', 3, 'PC', '1.0000', '135.0000000000', '135.00'),
(233, 90, '44426', 'SEM GTIN', 'MAKSCHUH 030', 3, 'PC', '1.0000', '139.4500000000', '139.45'),
(234, 90, '44430', 'SEM GTIN', 'MAKSCHUH 037', 3, 'PC', '1.0000', '88.9000000000', '88.90'),
(235, 90, '44431', 'SEM GTIN', 'MAKSCHUH 038', 3, 'PC', '1.0000', '78.9000000000', '78.90'),
(236, 90, '44432', 'SEM GTIN', 'MAKSCHUH 039A', 3, 'PC', '1.0000', '139.4500000000', '139.45'),
(237, 90, '55231', 'SEM GTIN', 'MAKSCHUH 044', 3, 'PC', '1.0000', '148.5000000000', '148.50'),
(238, 90, '55232', 'SEM GTIN', 'MAKSCHUH 045', 3, 'PC', '1.0000', '148.5000000000', '148.50'),
(239, 90, '55228', 'SEM GTIN', 'MAKSCHUH 046', 3, 'PC', '1.0000', '45.0000000000', '45.00'),
(240, 90, '61252', 'SEM GTIN', 'MAKSCHUH 1028', 3, 'PC', '20.0000', '8.8200000000', '176.40'),
(241, 91, '6707', 'SEM GTIN', 'CAMISA DO CILINDRO USM', 3, 'PC', '1.0000', '281.0000000000', '281.00'),
(242, 91, '6686', 'SEM GTIN', 'APOIO DA TESOURA - ESQUERDA - RB', 3, 'PC', '1.0000', '249.0000000000', '249.00'),
(243, 91, '6687', 'SEM GTIN', 'APOIO DE TESOURA - DIREITA - RB', 3, 'PC', '1.0000', '249.0000000000', '249.00'),
(244, 91, '6742', 'SEM GTIN', 'CUNHA DA PARADA MAQ. USM', 3, 'PC', '1.0000', '300.0000000000', '300.00');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `duplicatas`
--
ALTER TABLE `duplicatas`
  ADD PRIMARY KEY (`idDuplicata`),
  ADD KEY `fk_nota` (`idNota`);

--
-- Índices de tabela `empresas`
--
ALTER TABLE `empresas`
  ADD PRIMARY KEY (`idEmpresa`);

--
-- Índices de tabela `historicoPagamentos`
--
ALTER TABLE `historicoPagamentos`
  ADD PRIMARY KEY (`IDpg`),
  ADD UNIQUE KEY `IDduplicata` (`IDduplicata`),
  ADD KEY `fk_idPagAdd` (`idDupAdd`);

--
-- Índices de tabela `notaFiscalEntrada`
--
ALTER TABLE `notaFiscalEntrada`
  ADD PRIMARY KEY (`idNota`),
  ADD KEY `fk_natop` (`natOp`),
  ADD KEY `fk_empresa_idx` (`empresa`);

--
-- Índices de tabela `operacoes`
--
ALTER TABLE `operacoes`
  ADD PRIMARY KEY (`idOP`);

--
-- Índices de tabela `pagamentosAdd`
--
ALTER TABLE `pagamentosAdd`
  ADD PRIMARY KEY (`idPagAdd`);

--
-- Índices de tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`idItem`),
  ADD KEY `idNota` (`idNota`),
  ADD KEY `fk_cfop` (`CFOP`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `duplicatas`
--
ALTER TABLE `duplicatas`
  MODIFY `idDuplicata` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT de tabela `empresas`
--
ALTER TABLE `empresas`
  MODIFY `idEmpresa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de tabela `historicoPagamentos`
--
ALTER TABLE `historicoPagamentos`
  MODIFY `IDpg` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `notaFiscalEntrada`
--
ALTER TABLE `notaFiscalEntrada`
  MODIFY `idNota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=92;

--
-- AUTO_INCREMENT de tabela `operacoes`
--
ALTER TABLE `operacoes`
  MODIFY `idOP` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `pagamentosAdd`
--
ALTER TABLE `pagamentosAdd`
  MODIFY `idPagAdd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `idItem` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=245;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `duplicatas`
--
ALTER TABLE `duplicatas`
  ADD CONSTRAINT `fk_nota` FOREIGN KEY (`idNota`) REFERENCES `notaFiscalEntrada` (`idNota`);

--
-- Restrições para tabelas `historicoPagamentos`
--
ALTER TABLE `historicoPagamentos`
  ADD CONSTRAINT `FK_historico_duplicata` FOREIGN KEY (`IDduplicata`) REFERENCES `duplicatas` (`idDuplicata`),
  ADD CONSTRAINT `fk_idPagAdd` FOREIGN KEY (`idDupAdd`) REFERENCES `pagamentosAdd` (`idPagAdd`);

--
-- Restrições para tabelas `notaFiscalEntrada`
--
ALTER TABLE `notaFiscalEntrada`
  ADD CONSTRAINT `fk_empresa` FOREIGN KEY (`empresa`) REFERENCES `empresas` (`idEmpresa`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_natop` FOREIGN KEY (`natOp`) REFERENCES `operacoes` (`idOP`);

--
-- Restrições para tabelas `produtos`
--
ALTER TABLE `produtos`
  ADD CONSTRAINT `fk_cfop` FOREIGN KEY (`CFOP`) REFERENCES `operacoes` (`idOP`),
  ADD CONSTRAINT `idNota` FOREIGN KEY (`idNota`) REFERENCES `notaFiscalEntrada` (`idNota`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
