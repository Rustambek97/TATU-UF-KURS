-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               10.3.22-MariaDB - mariadb.org binary distribution
-- Операционная система:         Win64
-- HeidiSQL Версия:              12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Дамп структуры базы данных uquv_markaz
CREATE DATABASE IF NOT EXISTS `uquv_markaz` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `uquv_markaz`;

-- Дамп структуры для таблица uquv_markaz.kurslar
CREATE TABLE IF NOT EXISTS `kurslar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kurs_nomi` varchar(50) DEFAULT NULL,
  `narxi` decimal(10,2) DEFAULT NULL,
  `davomiyligi` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

-- Дамп данных таблицы uquv_markaz.kurslar: ~11 rows (приблизительно)
INSERT IGNORE INTO `kurslar` (`id`, `kurs_nomi`, `narxi`, `davomiyligi`) VALUES
	(1, 'python-asoslari', 300000.00, '2 oy'),
	(2, 'ingliz tili', 250000.00, '6 oy'),
	(3, 'matematika', 200000.00, '9 oy'),
	(4, 'tarix', 200000.00, '9 oy'),
	(5, 'Django backend', 400000.00, '4 oy'),
	(6, 'Front-end', 300000.00, '6 oy'),
	(7, 'Mobil dasturlash', 500000.00, '9 oy'),
	(8, 'SMM', 400000.00, '3 oy'),
	(9, 'Kompyuter grafikasi', 500000.00, '6 oy'),
	(10, 'ona-tili', 200000.00, '9 oy'),
	(11, 'Kompyuter savodxonligi', 200000.00, '1 oy');

-- Дамп структуры для таблица uquv_markaz.tulovlar
CREATE TABLE IF NOT EXISTS `tulovlar` (
  `uquvchi_id` int(11) DEFAULT NULL,
  `tulov` decimal(10,2) DEFAULT NULL,
  `kurs_id` int(11) DEFAULT NULL,
  `vaqti` datetime DEFAULT NULL,
  KEY `talaba_id` (`uquvchi_id`),
  KEY `FK_tulovlar_kurslar` (`kurs_id`),
  CONSTRAINT `FK_tulovlar_kurslar` FOREIGN KEY (`kurs_id`) REFERENCES `kurslar` (`id`),
  CONSTRAINT `tulovlar_ibfk_1` FOREIGN KEY (`uquvchi_id`) REFERENCES `uquvchilar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Дамп данных таблицы uquv_markaz.tulovlar: ~7 rows (приблизительно)
INSERT IGNORE INTO `tulovlar` (`uquvchi_id`, `tulov`, `kurs_id`, `vaqti`) VALUES
	(2, 200000.00, 11, '2024-01-04 11:32:05'),
	(5, 300000.00, 1, '2024-01-10 13:55:14'),
	(1, 200000.00, 4, '2023-12-05 09:18:20'),
	(3, 400000.00, 8, '2024-01-09 20:16:03'),
	(6, 200000.00, 11, '2024-01-04 15:47:45'),
	(2, 200000.00, 10, '2023-12-11 10:22:47'),
	(3, 300000.00, 6, '2024-01-13 09:05:36');

-- Дамп структуры для таблица uquv_markaz.uqituvchilar
CREATE TABLE IF NOT EXISTS `uqituvchilar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ism` varchar(20) DEFAULT NULL,
  `familiya` varchar(20) DEFAULT NULL,
  `yunalishi` varchar(100) DEFAULT NULL,
  `tel_raqami` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- Дамп данных таблицы uquv_markaz.uqituvchilar: ~13 rows (приблизительно)
INSERT IGNORE INTO `uqituvchilar` (`id`, `ism`, `familiya`, `yunalishi`, `tel_raqami`) VALUES
	(1, 'Sardorbek', 'Davletboyev', 'backend dasturlash', '+998914872323'),
	(2, 'Janar', 'Yusupova', 'backend dasturlash', '+998905476585'),
	(3, 'Feruza', 'Adambayeva', 'ingliz tili', '+998990965959'),
	(4, 'Oybek', 'Aliyev', 'office dasturlarda ishlash', '+998914568585'),
	(5, 'Firnafas', 'Yusupov', 'dasturlash texnologiyalari', '+998918956746'),
	(6, 'Anvar', 'Abdullayev', 'Android dasturchi va matematik', '+998994557557'),
	(7, 'Azizbek', 'Xaitboyev', '3D loyihalarida ishlash', '+998913547889'),
	(8, 'Shavkat', 'Ismailov', 'SMM dizayner', '+998954872111'),
	(9, 'Fazliddin', 'Jumaniyazov', 'Falsafashunoslik', '+998905743225'),
	(10, 'Mahmudjon', 'Sodiqov', 'ingliz tili va IT savodxonlik', '+998918788898'),
	(11, 'Rahmonbergan', 'Salayev', 'Tilshunoslik', '+998881186565'),
	(12, 'Iroda', 'Hajiyeva', 'Tarixchi va psixolog', '+998981232525'),
	(13, 'O\'ktamboy', 'Yo\'ldoshev', 'Frontend dasturchi', '+998914143223'),
	(14, 'Islom', 'Husainov', 'matematik', '+998906881441');

-- Дамп структуры для таблица uquv_markaz.uqituvchi_kurslari
CREATE TABLE IF NOT EXISTS `uqituvchi_kurslari` (
  `uqituvchi_id` int(11) DEFAULT NULL,
  `kurs_id` int(11) DEFAULT NULL,
  `vaqti` time DEFAULT NULL,
  KEY `FK__uqituvchilar` (`uqituvchi_id`),
  KEY `FK__kurslar` (`kurs_id`),
  CONSTRAINT `FK__kurslar` FOREIGN KEY (`kurs_id`) REFERENCES `kurslar` (`id`),
  CONSTRAINT `FK__uqituvchilar` FOREIGN KEY (`uqituvchi_id`) REFERENCES `uqituvchilar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы uquv_markaz.uqituvchi_kurslari: ~14 rows (приблизительно)
INSERT IGNORE INTO `uqituvchi_kurslari` (`uqituvchi_id`, `kurs_id`, `vaqti`) VALUES
	(2, 1, '14:00:00'),
	(3, 2, '09:00:00'),
	(4, 11, '09:00:00'),
	(6, 7, '10:00:00'),
	(7, 9, '16:00:00'),
	(8, 8, '18:00:00'),
	(9, 4, '11:00:00'),
	(10, 2, '10:00:00'),
	(10, 11, '12:00:00'),
	(11, 10, '12:30:00'),
	(12, 4, '13:00:00'),
	(13, 6, '13:20:00'),
	(14, 3, '08:00:00'),
	(6, 3, '11:30:00');

-- Дамп структуры для таблица uquv_markaz.uquvchilar
CREATE TABLE IF NOT EXISTS `uquvchilar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ism` varchar(20) DEFAULT NULL,
  `familiya` varchar(20) DEFAULT NULL,
  `tugilgan_sana` date DEFAULT NULL,
  `tel_raqam` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

-- Дамп данных таблицы uquv_markaz.uquvchilar: ~16 rows (приблизительно)
INSERT IGNORE INTO `uquvchilar` (`id`, `ism`, `familiya`, `tugilgan_sana`, `tel_raqam`) VALUES
	(1, 'Saidmurod', 'Ismoilov', '1998-02-24', '+998915673641'),
	(2, 'Abror', 'Habibullayev', '2000-08-04', '+998973212587'),
	(3, 'Asadbek', 'Bekchanov', '1997-03-29', '+998901325689'),
	(4, 'Dastonbek', 'Sotliqov', '2004-08-22', '+998935261122'),
	(5, 'Dilshodbek', 'Kuchkarov', '1999-06-11', '+998915542484'),
	(6, 'Doniyor', 'Artikov', '2001-05-28', '+998941196582'),
	(7, 'Egamberdi', 'Samandarov', '2000-12-03', '+998941389998'),
	(8, 'Nilufar', 'Abdullayeva', '1999-06-03', '+998889485574'),
	(9, 'Orzigul', 'Abdullayeva', '2002-09-07', '+998994402002'),
	(10, 'Ro\'zimboy', 'Norimbetov', '2002-07-10', '+998914488797'),
	(11, 'Shohista', 'Kamolova', '1999-02-13', '+998992011001'),
	(12, 'Temur', 'Nurullayev', '2002-09-25', '+998884041787'),
	(13, 'Temurbek', 'Raximberganov', '2001-10-05', '+998908707780'),
	(14, 'Umida', 'Tajiyeva', '1999-10-25', '+998972335569'),
	(15, 'Xalilla', 'O\'rinov', '2000-01-10', '+998978779090'),
	(16, 'Sanjar', 'Rahimboyev', '2001-06-07', '+998937078911');

-- Дамп структуры для таблица uquv_markaz.uquvchi_kurslari
CREATE TABLE IF NOT EXISTS `uquvchi_kurslari` (
  `uquvchi_id` int(11) DEFAULT NULL,
  `kurs_id` int(11) DEFAULT NULL,
  `uqituvchi_id` int(11) DEFAULT NULL,
  KEY `FK1_uquvchi_kurslari` (`uquvchi_id`),
  KEY `FK2_uquvchi_kurslari` (`kurs_id`),
  KEY `FK_uquvchi_kurslari_uqituvchilar` (`uqituvchi_id`),
  CONSTRAINT `FK1_uquvchi_kurslari` FOREIGN KEY (`kurs_id`) REFERENCES `kurslar` (`id`),
  CONSTRAINT `FK2_uquvchi_kurslari` FOREIGN KEY (`uquvchi_id`) REFERENCES `uquvchilar` (`id`),
  CONSTRAINT `FK_uquvchi_kurslari_uqituvchilar` FOREIGN KEY (`uqituvchi_id`) REFERENCES `uqituvchilar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы uquv_markaz.uquvchi_kurslari: ~14 rows (приблизительно)
INSERT IGNORE INTO `uquvchi_kurslari` (`uquvchi_id`, `kurs_id`, `uqituvchi_id`) VALUES
	(4, 3, 14),
	(6, 7, 6),
	(16, 4, 12),
	(2, 2, 3),
	(4, 9, 7),
	(5, 9, 7),
	(5, 3, 6),
	(1, 8, 8),
	(10, 1, 2),
	(11, 9, 7),
	(4, 2, 3),
	(1, 7, 6),
	(14, 4, 9),
	(3, 6, 13);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
