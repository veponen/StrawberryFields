-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Gép: mariadb
-- Létrehozás ideje: 2020. Ápr 12. 23:49
-- Kiszolgáló verziója: 10.4.12-MariaDB-1:10.4.12+maria~bionic
-- PHP verzió: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `mydatabase`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `weather`
--

CREATE TABLE `weather` (
  `date` date NOT NULL DEFAULT current_timestamp(),
  `current_temp` float NOT NULL,
  `min_temp` float NOT NULL,
  `max_temp` float NOT NULL,
  `pressure` float NOT NULL,
  `humidity` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- A tábla adatainak kiíratása `weather`
--

INSERT INTO `weather` (`date`, `current_temp`, `min_temp`, `max_temp`, `pressure`, `humidity`) VALUES
('2020-04-12', 1, 1, 1, 979, 100);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `weather`
--
ALTER TABLE `weather`
  ADD PRIMARY KEY (`date`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
