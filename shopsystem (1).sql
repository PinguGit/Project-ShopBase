-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 09. Okt 2024 um 11:34
-- Server-Version: 10.4.28-MariaDB
-- PHP-Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `shopsystem`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `bestellung`
--

CREATE TABLE `bestellung` (
  `bestell_id` int(11) NOT NULL,
  `anzahl` int(11) NOT NULL,
  `gesamtpreis` double NOT NULL,
  `verkaeufer_produkt_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `bestellung`
--

INSERT INTO `bestellung` (`bestell_id`, `anzahl`, `gesamtpreis`, `verkaeufer_produkt_id`) VALUES
(1, 2, 1999.98, 1),
(2, 1, 899.99, 2),
(3, 1, 499.99, 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `hersteller`
--

CREATE TABLE `hersteller` (
  `hersteller_id` int(11) NOT NULL,
  `hersteller_name` varchar(100) NOT NULL,
  `laender_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `hersteller`
--

INSERT INTO `hersteller` (`hersteller_id`, `hersteller_name`, `laender_id`) VALUES
(1, 'Apple', 2),
(2, 'Samsung', 1),
(3, 'Sony', 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kunde`
--

CREATE TABLE `kunde` (
  `kunden_id` int(11) NOT NULL,
  `vorname` varchar(50) NOT NULL,
  `nachname` varchar(50) NOT NULL,
  `strasse` varchar(50) NOT NULL,
  `hausnummer` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `ort_id` int(11) NOT NULL,
  `laender_id` int(11) NOT NULL,
  `password_id` int(11) NOT NULL,
  `geburtsdatum` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `kunde`
--

INSERT INTO `kunde` (`kunden_id`, `vorname`, `nachname`, `strasse`, `hausnummer`, `email`, `ort_id`, `laender_id`, `password_id`, `geburtsdatum`) VALUES
(1, 'John', 'Doe', 'Main St', '123', 'john@example.com', 1, 1, 1, '1990-01-01'),
(2, 'Jane', 'Smith', 'Beverly Blvd', '456', 'jane@example.com', 2, 2, 2, '1985-02-15'),
(3, 'Pierre', 'Dupont', 'Rue de Rivoli', '789', 'pierre@example.com', 3, 3, 3, '1975-05-20');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kundenbestellungen`
--

CREATE TABLE `kundenbestellungen` (
  `kunden_id` int(11) NOT NULL,
  `bestell_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `kundenbestellungen`
--

INSERT INTO `kundenbestellungen` (`kunden_id`, `bestell_id`) VALUES
(1, 1),
(2, 2),
(3, 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `laender`
--

CREATE TABLE `laender` (
  `laender_id` int(11) NOT NULL,
  `land` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `laender`
--

INSERT INTO `laender` (`laender_id`, `land`) VALUES
(1, 'Germany'),
(2, 'USA'),
(3, 'France');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `orte`
--

CREATE TABLE `orte` (
  `ort_id` int(11) NOT NULL,
  `plz` int(11) NOT NULL,
  `ort_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `orte`
--

INSERT INTO `orte` (`ort_id`, `plz`, `ort_name`) VALUES
(1, 10115, 'Berlin'),
(2, 90210, 'Beverly Hills'),
(3, 75001, 'Paris');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `passwort`
--

CREATE TABLE `passwort` (
  `password_id` int(11) NOT NULL,
  `pasword` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `passwort`
--

INSERT INTO `passwort` (`password_id`, `pasword`) VALUES
(1, 'password123'),
(2, 'qwerty456'),
(3, 'welcome789');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `product`
--

CREATE TABLE `product` (
  `produkt_id` int(11) NOT NULL,
  `produkt_name` varchar(100) NOT NULL,
  `preis` double NOT NULL,
  `hersteller_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `product`
--

INSERT INTO `product` (`produkt_id`, `produkt_name`, `preis`, `hersteller_id`) VALUES
(1, 'iPhone', 999.99, 1),
(2, 'Galaxy S', 899.99, 2),
(3, 'PlayStation', 499.99, 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `verkaeufer`
--

CREATE TABLE `verkaeufer` (
  `verkaeufer_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `strasse` varchar(50) NOT NULL,
  `hausnummer` varchar(5) NOT NULL,
  `email` varchar(50) NOT NULL,
  `ort_id` int(11) NOT NULL,
  `laender_id` int(11) NOT NULL,
  `password_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `verkaeufer`
--

INSERT INTO `verkaeufer` (`verkaeufer_id`, `name`, `strasse`, `hausnummer`, `email`, `ort_id`, `laender_id`, `password_id`) VALUES
(1, 'Seller A', 'Street A', '111', 'sellerA@example.com', 1, 1, 1),
(2, 'Seller B', 'Street B', '222', 'sellerB@example.com', 2, 2, 2),
(3, 'Seller C', 'Street C', '333', 'sellerC@example.com', 3, 3, 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `verkaeufer_produkte`
--

CREATE TABLE `verkaeufer_produkte` (
  `verkaeufer_produkt_id` int(11) NOT NULL,
  `produkt_id` int(11) NOT NULL,
  `verkaeufer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `verkaeufer_produkte`
--

INSERT INTO `verkaeufer_produkte` (`verkaeufer_produkt_id`, `produkt_id`, `verkaeufer_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `bestellung`
--
ALTER TABLE `bestellung`
  ADD PRIMARY KEY (`bestell_id`,`verkaeufer_produkt_id`),
  ADD KEY `verkauefer_produkt_id` (`verkaeufer_produkt_id`);

--
-- Indizes für die Tabelle `hersteller`
--
ALTER TABLE `hersteller`
  ADD PRIMARY KEY (`hersteller_id`),
  ADD KEY `laender_id` (`laender_id`);

--
-- Indizes für die Tabelle `kunde`
--
ALTER TABLE `kunde`
  ADD PRIMARY KEY (`kunden_id`),
  ADD KEY `ort_id` (`ort_id`),
  ADD KEY `laender_id` (`laender_id`),
  ADD KEY `kunde_ibfk_3` (`password_id`);

--
-- Indizes für die Tabelle `kundenbestellungen`
--
ALTER TABLE `kundenbestellungen`
  ADD PRIMARY KEY (`kunden_id`,`bestell_id`),
  ADD KEY `bestell_id` (`bestell_id`);

--
-- Indizes für die Tabelle `laender`
--
ALTER TABLE `laender`
  ADD PRIMARY KEY (`laender_id`);

--
-- Indizes für die Tabelle `orte`
--
ALTER TABLE `orte`
  ADD PRIMARY KEY (`ort_id`);

--
-- Indizes für die Tabelle `passwort`
--
ALTER TABLE `passwort`
  ADD PRIMARY KEY (`password_id`);

--
-- Indizes für die Tabelle `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`produkt_id`),
  ADD KEY `product_ibfk_1` (`hersteller_id`);

--
-- Indizes für die Tabelle `verkaeufer`
--
ALTER TABLE `verkaeufer`
  ADD PRIMARY KEY (`verkaeufer_id`),
  ADD KEY `ort_id` (`ort_id`),
  ADD KEY `laender_id` (`laender_id`),
  ADD KEY `verkauefer_ibfk_3` (`password_id`);

--
-- Indizes für die Tabelle `verkaeufer_produkte`
--
ALTER TABLE `verkaeufer_produkte`
  ADD PRIMARY KEY (`verkaeufer_produkt_id`),
  ADD KEY `verkauefer_id` (`verkaeufer_id`),
  ADD KEY `verkauefer_produkte_ibfk_1` (`produkt_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `bestellung`
--
ALTER TABLE `bestellung`
  MODIFY `bestell_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT für Tabelle `hersteller`
--
ALTER TABLE `hersteller`
  MODIFY `hersteller_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT für Tabelle `kunde`
--
ALTER TABLE `kunde`
  MODIFY `kunden_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT für Tabelle `laender`
--
ALTER TABLE `laender`
  MODIFY `laender_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT für Tabelle `orte`
--
ALTER TABLE `orte`
  MODIFY `ort_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT für Tabelle `passwort`
--
ALTER TABLE `passwort`
  MODIFY `password_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT für Tabelle `product`
--
ALTER TABLE `product`
  MODIFY `produkt_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT für Tabelle `verkaeufer`
--
ALTER TABLE `verkaeufer`
  MODIFY `verkaeufer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT für Tabelle `verkaeufer_produkte`
--
ALTER TABLE `verkaeufer_produkte`
  MODIFY `verkaeufer_produkt_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `bestellung`
--
ALTER TABLE `bestellung`
  ADD CONSTRAINT `bestellung_ibfk_1` FOREIGN KEY (`verkaeufer_produkt_id`) REFERENCES `verkaeufer_produkte` (`verkaeufer_produkt_id`);

--
-- Constraints der Tabelle `hersteller`
--
ALTER TABLE `hersteller`
  ADD CONSTRAINT `hersteller_ibfk_1` FOREIGN KEY (`laender_id`) REFERENCES `laender` (`laender_id`);

--
-- Constraints der Tabelle `kunde`
--
ALTER TABLE `kunde`
  ADD CONSTRAINT `kunde_ibfk_1` FOREIGN KEY (`ort_id`) REFERENCES `orte` (`ort_id`),
  ADD CONSTRAINT `kunde_ibfk_2` FOREIGN KEY (`laender_id`) REFERENCES `laender` (`laender_id`),
  ADD CONSTRAINT `kunde_ibfk_3` FOREIGN KEY (`password_id`) REFERENCES `passwort` (`password_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints der Tabelle `kundenbestellungen`
--
ALTER TABLE `kundenbestellungen`
  ADD CONSTRAINT `kundenbestellungen_ibfk_1` FOREIGN KEY (`kunden_id`) REFERENCES `kunde` (`kunden_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `kundenbestellungen_ibfk_2` FOREIGN KEY (`bestell_id`) REFERENCES `bestellung` (`bestell_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints der Tabelle `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`hersteller_id`) REFERENCES `hersteller` (`hersteller_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints der Tabelle `verkaeufer`
--
ALTER TABLE `verkaeufer`
  ADD CONSTRAINT `verkaeufer_ibfk_1` FOREIGN KEY (`ort_id`) REFERENCES `orte` (`ort_id`),
  ADD CONSTRAINT `verkaeufer_ibfk_2` FOREIGN KEY (`laender_id`) REFERENCES `laender` (`laender_id`),
  ADD CONSTRAINT `verkaeufer_ibfk_3` FOREIGN KEY (`password_id`) REFERENCES `passwort` (`password_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints der Tabelle `verkaeufer_produkte`
--
ALTER TABLE `verkaeufer_produkte`
  ADD CONSTRAINT `verkaeufer_produkte_ibfk_1` FOREIGN KEY (`produkt_id`) REFERENCES `product` (`produkt_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `verkaeufer_produkte_ibfk_2` FOREIGN KEY (`verkaeufer_id`) REFERENCES `verkaeufer` (`verkaeufer_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
