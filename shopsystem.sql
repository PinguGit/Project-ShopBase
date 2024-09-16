-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 16. Sep 2024 um 12:14
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
  `verkauefer_produkt_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `hersteller`
--

CREATE TABLE `hersteller` (
  `hersteller_id` int(11) NOT NULL,
  `hersteller_name` varchar(100) NOT NULL,
  `laender_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `laender`
--

CREATE TABLE `laender` (
  `laender_id` int(11) NOT NULL,
  `land` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `orte`
--

CREATE TABLE `orte` (
  `ort_id` int(11) NOT NULL,
  `plz` int(11) NOT NULL,
  `ort_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `passwort`
--

CREATE TABLE `passwort` (
  `password_id` int(11) NOT NULL,
  `pasword` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `produkte`
--

CREATE TABLE `produkte` (
  `produkt_id` int(11) NOT NULL,
  `produkt_name` varchar(100) NOT NULL,
  `preis` double NOT NULL,
  `hersteller_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `verkauefer`
--

CREATE TABLE `verkauefer` (
  `verkauefer_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `strasse` varchar(50) NOT NULL,
  `hausnummer` varchar(5) NOT NULL,
  `email` varchar(50) NOT NULL,
  `ort_id` int(11) NOT NULL,
  `laender_id` int(11) NOT NULL,
  `password_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `verkauefer_produkte`
--

CREATE TABLE `verkauefer_produkte` (
  `verkauefer_produkt_id` int(11) NOT NULL,
  `produkt_id` int(11) NOT NULL,
  `verkauefer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `bestellung`
--
ALTER TABLE `bestellung`
  ADD PRIMARY KEY (`bestell_id`,`verkauefer_produkt_id`),
  ADD KEY `verkauefer_produkt_id` (`verkauefer_produkt_id`);

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
  ADD KEY `password_id` (`password_id`);

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
-- Indizes für die Tabelle `produkte`
--
ALTER TABLE `produkte`
  ADD PRIMARY KEY (`produkt_id`),
  ADD KEY `hersteller_id` (`hersteller_id`);

--
-- Indizes für die Tabelle `verkauefer`
--
ALTER TABLE `verkauefer`
  ADD PRIMARY KEY (`verkauefer_id`),
  ADD KEY `ort_id` (`ort_id`),
  ADD KEY `laender_id` (`laender_id`),
  ADD KEY `password_id` (`password_id`);

--
-- Indizes für die Tabelle `verkauefer_produkte`
--
ALTER TABLE `verkauefer_produkte`
  ADD PRIMARY KEY (`verkauefer_produkt_id`),
  ADD KEY `produkt_id` (`produkt_id`),
  ADD KEY `verkauefer_id` (`verkauefer_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `bestellung`
--
ALTER TABLE `bestellung`
  MODIFY `bestell_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `hersteller`
--
ALTER TABLE `hersteller`
  MODIFY `hersteller_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `kunde`
--
ALTER TABLE `kunde`
  MODIFY `kunden_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `laender`
--
ALTER TABLE `laender`
  MODIFY `laender_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `orte`
--
ALTER TABLE `orte`
  MODIFY `ort_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `passwort`
--
ALTER TABLE `passwort`
  MODIFY `password_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `produkte`
--
ALTER TABLE `produkte`
  MODIFY `produkt_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `verkauefer`
--
ALTER TABLE `verkauefer`
  MODIFY `verkauefer_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `verkauefer_produkte`
--
ALTER TABLE `verkauefer_produkte`
  MODIFY `verkauefer_produkt_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `bestellung`
--
ALTER TABLE `bestellung`
  ADD CONSTRAINT `bestellung_ibfk_1` FOREIGN KEY (`verkauefer_produkt_id`) REFERENCES `verkauefer_produkte` (`verkauefer_produkt_id`);

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
  ADD CONSTRAINT `kunde_ibfk_3` FOREIGN KEY (`password_id`) REFERENCES `passwort` (`password_id`);

--
-- Constraints der Tabelle `produkte`
--
ALTER TABLE `produkte`
  ADD CONSTRAINT `produkte_ibfk_1` FOREIGN KEY (`hersteller_id`) REFERENCES `hersteller` (`hersteller_id`);

--
-- Constraints der Tabelle `verkauefer`
--
ALTER TABLE `verkauefer`
  ADD CONSTRAINT `verkauefer_ibfk_1` FOREIGN KEY (`ort_id`) REFERENCES `orte` (`ort_id`),
  ADD CONSTRAINT `verkauefer_ibfk_2` FOREIGN KEY (`laender_id`) REFERENCES `laender` (`laender_id`),
  ADD CONSTRAINT `verkauefer_ibfk_3` FOREIGN KEY (`password_id`) REFERENCES `passwort` (`password_id`);

--
-- Constraints der Tabelle `verkauefer_produkte`
--
ALTER TABLE `verkauefer_produkte`
  ADD CONSTRAINT `verkauefer_produkte_ibfk_1` FOREIGN KEY (`produkt_id`) REFERENCES `produkte` (`produkt_id`),
  ADD CONSTRAINT `verkauefer_produkte_ibfk_2` FOREIGN KEY (`verkauefer_id`) REFERENCES `verkauefer` (`verkauefer_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
