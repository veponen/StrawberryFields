-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Gép: mariadb
-- Létrehozás ideje: 2020. Ápr 12. 23:50
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
-- Tábla szerkezet ehhez a táblához `corpses`
--

CREATE TABLE `corpses` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- A tábla adatainak kiíratása `corpses`
--

INSERT INTO `corpses` (`id`, `date`, `value`) VALUES
(1, '2020-07-01', 23.4583),
(2, '2020-07-02', 5.6931),
(3, '2020-07-03', 39.7034),
(4, '2020-07-04', 81.2784),
(5, '2020-07-05', 169.474),
(6, '2020-07-06', 178.762),
(7, '2020-07-07', 207.173),
(8, '2020-07-08', 265.782),
(9, '2020-07-09', 373.107),
(10, '2020-07-10', 875.612),
(11, '2020-07-11', 983.565),
(12, '2020-07-12', 792.942),
(13, '2020-07-13', 814.238),
(14, '2020-07-14', 747.498),
(15, '2020-07-15', 716.034),
(16, '2020-07-16', 706.636),
(17, '2020-07-17', 718.066),
(18, '2020-07-18', 698.391),
(19, '2020-07-19', 608.278),
(20, '2020-07-20', 596.679),
(21, '2020-07-21', 590.759),
(22, '2020-07-22', 582.024),
(23, '2020-07-23', 553.818),
(24, '2020-07-24', 521.588),
(25, '2020-07-25', 332.645),
(26, '2020-07-26', 300.972),
(27, '2020-07-27', 192.039),
(28, '2020-07-28', 84.7784),
(29, '2020-07-29', 51.3623),
(30, '2020-07-30', 28.4465),
(31, '2020-07-31', 23.1843),
(32, '2020-08-01', 7.78012);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `corpses`
--
ALTER TABLE `corpses`
  ADD PRIMARY KEY (`id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `corpses`
--
ALTER TABLE `corpses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
