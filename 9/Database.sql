-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: otakulife
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrator`
--

DROP TABLE IF EXISTS `administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrator` (
  `adminid` int(11) NOT NULL AUTO_INCREMENT,
  `brukernavn` varchar(255) NOT NULL,
  `adgang` tinyint(3) DEFAULT NULL,
  `opprettsdato` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`adminid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator`
--

LOCK TABLES `administrator` WRITE;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` VALUES (3,'aribo',3,'2017-03-28 11:51:31'),(4,'pojo',1,'2017-03-28 11:51:31');
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bestilling`
--

DROP TABLE IF EXISTS `bestilling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bestilling` (
  `bestillingid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `brukernavn` varchar(255) NOT NULL,
  `dato` timestamp NULL DEFAULT NULL,
  `leveringstid` int(10) unsigned DEFAULT '5',
  `bestillingsstatus` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`bestillingid`),
  KEY `brukernavn_idx` (`brukernavn`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bestilling`
--

LOCK TABLES `bestilling` WRITE;
/*!40000 ALTER TABLE `bestilling` DISABLE KEYS */;
INSERT INTO `bestilling` VALUES (1,'outlandmoro','2017-04-19 20:36:05',5,1),(2,'topdoog1','2017-04-19 20:36:05',3,1),(3,'pojo','2017-04-19 20:36:05',2,1),(4,'cycloneD11','2017-04-19 20:36:05',9,1),(5,'outlandmoro','2017-04-20 00:24:03',5,1),(6,'aribo','2017-04-20 14:24:53',7,1),(7,'pojo','2017-04-20 12:00:00',1,1),(8,'test','2017-04-20 00:22:03',1,1),(9,'aribo','2017-04-20 12:55:55',3,1),(10,'random','2017-04-20 13:10:42',1,1),(11,'seef11','2017-04-26 14:10:23',7,1),(12,'pojo','2017-04-21 00:24:03',7,1),(13,'test','2017-04-21 00:24:03',7,1),(14,'aribo','2017-04-22 00:24:03',7,1),(15,'pojo','2017-04-23 00:24:03',7,1),(16,'topdoog1','2017-04-24 00:24:03',7,1),(17,'seef11','2017-04-25 00:24:03',7,1),(18,'random','2017-04-26 00:24:03',7,1),(19,'outlandmoro','2017-04-26 00:24:03',7,1),(20,'topdoog1','2017-04-26 00:24:03',7,1);
/*!40000 ALTER TABLE `bestilling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bestillingskurv`
--

DROP TABLE IF EXISTS `bestillingskurv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bestillingskurv` (
  `bestillingid` int(11) NOT NULL,
  `produktid` int(11) NOT NULL,
  `kvantitet` int(11) NOT NULL,
  PRIMARY KEY (`bestillingid`,`produktid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bestillingskurv`
--

LOCK TABLES `bestillingskurv` WRITE;
/*!40000 ALTER TABLE `bestillingskurv` DISABLE KEYS */;
INSERT INTO `bestillingskurv` VALUES (1,2,1),(1,3,2),(2,1,2),(3,3,1),(4,7,1),(4,9,2),(5,1,1),(5,2,3),(6,1,1),(6,3,3),(7,1,1),(8,4,2),(9,3,4),(10,3,1),(11,4,2),(12,3,2),(12,10,1),(13,7,4),(14,9,1),(15,2,10),(15,3,1),(15,6,1),(15,9,1),(16,1,1),(17,7,1),(18,1,1),(18,9,1),(18,11,1),(19,5,1),(20,3,8);
/*!40000 ALTER TABLE `bestillingskurv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bruker`
--

DROP TABLE IF EXISTS `bruker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bruker` (
  `brukernavn` varchar(255) NOT NULL,
  `passord` varchar(255) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `fornavn` varchar(100) DEFAULT NULL,
  `etternavn` varchar(100) DEFAULT NULL,
  `addresse` varchar(45) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`brukernavn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bruker`
--

LOCK TABLES `bruker` WRITE;
/*!40000 ALTER TABLE `bruker` DISABLE KEYS */;
INSERT INTO `bruker` VALUES ('aribo','$5$rounds=535000$oJk1OZ4sONusGvDX$EPYjVeqx8WLLo954zorfql5SUrgvcF5KOcf71z1fkUD','aoaa@mail.com','Ahmed','Abdi','Terje vigens vei 3',1),('cycloneD11','$5$rounds=535000$M7uXtHnu8wIYUovv$YVzvQCMmEEXnffd39eFBGKxmIbHN.riBde3ghjzQ110','cycle@mail.com','Mohamed','Maalin',' Skauen vei 2',0),('olav','$5$rounds=535000$tU85F6nODqvUsdwC$X5U4tQG5t3ROIkQhBw.OOw7WoDq5yPZWAe8nUC2pQj8','olav@msn.no','Olav','Olsen','Gøkka stien 7',0),('outlandmoro','$5$rounds=535000$8QVifhVeB.j4crjI$5$rounds=535000$wY6HyuCs2VJZg8Ju$qItXTDo7cFGDbN6iY0SPI4pdnkPW3zkSxINk0J8nlGA','outland@mail.com','Osman','Chaudry','Ukjent vei 2',0),('pojo','$5$rounds=535000$0Bs46yGQ6QGQsnzV$JmYWUXiJnavE8aW6AFRmd6.w/iUPfLYbZ9WWFgc1FaB','pojo@mail.com','Bendik','Gjøvik','Buran vei 3',0),('random','$5$rounds=535000$tmYDCJ4MXJ3qOYvC$5$rounds=535000$onFNCQJKT0QOXzh8$4UrS3TcYW815KPk8ZVH61DCltrtTTcER1CwmBkfwJa2','random@random.no','Random','Random','Random veien 1',0),('seef11','$5$rounds=535000$GDMBrr9q/q74YjAa$5$rounds=535000$yih7UdOHCfcO3HOO$5$rounds=535000$yih7UdOHCfcO3HOO$Cv4Sw1TX34wc9OLPd0SbAMOi.2jAPPWx4OUNEwm1xy3','seef@mail.com','Ahmed','Yusuf','Overalt vei 1',0),('test','$5$rounds=535000$EEbigRlIwSXBiATd$ep0DWkUnTtWdLPSRsNdo/AvJGSFaXIMkjH5BIf0kac8','test@test.no','test','test','test veien 4',1),('tom','$5$rounds=535000$alaPHnzSiqaIW.64$cu.fHxeLEkA7kHREFbFJaSrELDOgHEfoOXgBUzcfpW0','tom@tom','Tom','Tom','Atom veien 16',0),('topdoog1','$5$rounds=535000$T.xw27vxeBwaTHSj$5$rounds=535000$TByKN4UAQQRxhbBi$X4tV0HEnJx5ZhcZWAX.ehha2Zyj.ALudgRmEoTxjtR0','freia@mail.com','Zakaria','Mohamod','Buran vei 2',0);
/*!40000 ALTER TABLE `bruker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `digital`
--

DROP TABLE IF EXISTS `digital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `digital` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kode` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `digital`
--

LOCK TABLES `digital` WRITE;
/*!40000 ALTER TABLE `digital` DISABLE KEYS */;
/*!40000 ALTER TABLE `digital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `levering`
--

DROP TABLE IF EXISTS `levering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `levering` (
  `leveringsid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `brukernavn` varchar(255) NOT NULL,
  `bestillingsaddresse` varchar(45) DEFAULT NULL,
  `leveringstatus` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`leveringsid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `levering`
--

LOCK TABLES `levering` WRITE;
/*!40000 ALTER TABLE `levering` DISABLE KEYS */;
INSERT INTO `levering` VALUES (3,'topdoog1','Buran vei 2','1'),(4,'pojo','Bruan vei 3','1');
/*!40000 ALTER TABLE `levering` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leverings_addresse`
--

DROP TABLE IF EXISTS `leverings_addresse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leverings_addresse` (
  `leveringsid` int(10) unsigned NOT NULL,
  `leverings_addresse` varchar(45) NOT NULL,
  `fornavn` varchar(100) NOT NULL,
  `etternavn` varchar(100) NOT NULL,
  PRIMARY KEY (`leveringsid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leverings_addresse`
--

LOCK TABLES `leverings_addresse` WRITE;
/*!40000 ALTER TABLE `leverings_addresse` DISABLE KEYS */;
INSERT INTO `leverings_addresse` VALUES (1,'Buran vei 2','Zakaria','Mohamod'),(2,'random gate 1','Thomas','Tog');
/*!40000 ALTER TABLE `leverings_addresse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produkt`
--

DROP TABLE IF EXISTS `produkt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produkt` (
  `produktid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `produktnavn` varchar(255) DEFAULT NULL,
  `beskrivelse` varchar(1024) DEFAULT NULL,
  `standardpris` float NOT NULL DEFAULT '0',
  `avslag` int(100) NOT NULL DEFAULT '0',
  `tilbudpris` float GENERATED ALWAYS AS ((`standardpris` - ((`standardpris` * `avslag`) / 100))) VIRTUAL NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `produktbilde` varchar(255) DEFAULT NULL,
  `type_produkt` varchar(450) DEFAULT NULL,
  PRIMARY KEY (`produktid`),
  FULLTEXT KEY `produktnavn` (`produktnavn`,`beskrivelse`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produkt`
--

LOCK TABLES `produkt` WRITE;
/*!40000 ALTER TABLE `produkt` DISABLE KEYS */;
INSERT INTO `produkt` (`produktid`, `produktnavn`, `beskrivelse`, `standardpris`, `avslag`, `deleted`, `produktbilde`, `type_produkt`) VALUES (1,'Final Fantasy 15','Final Fantasy XV, originally called Final Fantasy Versus XIII, is the fifteenth installment in the main Final Fantasy series and a former entry in the Fabula Nova Crystallis: Final Fantasy sub-series. The extent to which it connects to Final Fantasy XIII and Final Fantasy Type-0 has been reduced, and it now features an original lore. The game was released worldwide on November 29, 2016 for the PlayStation 4 and Xbox One. It supports the PlayStation 4 Pro, but is optimized for the consoles standard version.',60,20,0,'final-fantasy-xv-312641.22.jpg','PS4'),(2,'Fire Emblem Echoes','Et eller annet',60,50,0,'fire-emblem-echoes-mou-hitori-no-eiyuu-ou-507791.1.jpg','3DS'),(3,'Monster Hunter XX','Et eller annet',60,50,0,'monster-hunter-xx-497033.17.jpg','3DS'),(4,'Aoki Kakumei no Valkyria (Valkyria Chronicles 4)','Et eller annet',60,25,0,'aoki-kakumei-no-valkyria-442221.7.jpg','PS4'),(5,'Berserker Musou (Berserker Warrior)','Et eller annet',60,20,0,'berserk-musou-475801.13.jpg','PS4'),(6,'Persona 5','Et eller annet',60,25,0,'persona-5-379517.5.jpg','PS4'),(7,'Ryu ga Gotoku 6 (Yakuza 6)','Et eller annet',60,20,0,'ryu-ga-gotoku-6-inochi-no-uta-429361.6.jpg','PS4'),(8,'Eiyu Densetsu Zero no Kiseki Evolution (Legend of Heroes Trail of the Zero Evolution)','Et eller annet',60,70,0,'pa.211939.7.jpg','PSVita'),(9,'Eiyu Densetsu Ao no Kiseki Evolution (Legend of Heroes Trail of the Blue Evolution)','Et eller annet',60,70,0,'eiyuu-densetsu-ao-no-kiseki-evolution-317423.11.jpg','PSVita'),(10,'Eiyuu Densetsu Sen no Kiseki (Legend of Heroes Trails of the Cold Steel)','Et eller annet',60,50,0,'eiyuudensetsusennokiseki-279187.8.jpg','PSVita'),(11,'Eiyuu Densetsu Sen no Kiseki II (Legend of Heroes Trails of the Cold Steel II)','Et eller annet',60,50,0,'eiyuu-densetsu-sen-no-kiseki-ii-347829.13.jpg','PSVita'),(12,'Eiyuu Densetsu Sora no Kiseki FC Evolution (Legend of Heroes Trails in the Sky FC)','Et eller annet',60,70,0,'eiyuu-densetsu-sora-no-kiseki-fc-evolution-394099.9.jpg','PSVita'),(13,'Eiyuu Densetsu Sora no Kiseki SC Evolution (Legend of Heroes Trails in the Sky SC)','Et eller annet',60,70,0,'eiyuu-densetsu-sora-no-kiseki-sc-evolution-423671.9.jpg','PSVita'),(14,'Eiyuu Densetsu Sora no Kiseki the 3rd Evolution (Legend of Heroes Trails in the Sky the 3rd)','Et eller annet',60,70,0,'eiyuu-densetsu-sora-no-kiseki-the-3rd-evolution-465611.2.jpg','PSVita'),(15,'Kingdom Hearts III','Et eller annet',60,20,0,'kingdom-hearts-iii-312629.15.jpg','PS4'),(16,'Final Fantasy 14','Best MMORPG',100,10,1,'ff14.jpg','PC'),(17,'Dota2','Meh',100,10,1,'header.jpg','PC'),(18,'af','sff',100,1,1,'chain_chronicle_org.jpg','afaf'),(19,'Final Fantasy 14','Yoshi-P is a genious',40,10,1,'ff14.jpg','PC/PS4');
/*!40000 ALTER TABLE `produkt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relatert_produkt`
--

DROP TABLE IF EXISTS `relatert_produkt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `relatert_produkt` (
  `produktid` int(10) unsigned NOT NULL,
  `relatert_produkt` varchar(45) NOT NULL,
  `popularitet` int(1) DEFAULT NULL,
  PRIMARY KEY (`produktid`,`relatert_produkt`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relatert_produkt`
--

LOCK TABLES `relatert_produkt` WRITE;
/*!40000 ALTER TABLE `relatert_produkt` DISABLE KEYS */;
INSERT INTO `relatert_produkt` VALUES (1,'Berserker Musou (Berserker Warrior)',10),(5,'Final Fantasy XV',5);
/*!40000 ALTER TABLE `relatert_produkt` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-28 21:38:18
