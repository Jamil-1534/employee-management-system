CREATE DATABASE  IF NOT EXISTS `employee_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `employee_data`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: employee_data
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data` (
  `Id` varchar(20) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Phone` varchar(15) DEFAULT NULL,
  `Role` varchar(50) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `Salary` decimal(18,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES ('1521','joy','01994032931','Web Developer','Male',50000.00),('1522','joya','1994032931','Web Developer','Male',50000.00),('65','fdcy','51454','Network Engineer','Male',32032.00),('452','iolbg','2412045','Web Developer','Male',50124.00),('4522','iolbgm','2412045','Cloud Architect','Male',501241.00),('52274','fcgxfrd','04512','Web Developer','Male',51012.00),('65165','hjfhjn','4634','Cloud Architect','Male',64564.00),('45324','joy','425020','Web Developer','Female',2.00),('45265','dfgb','024520','Cloud Architect','Male',10021.00),('04124105','g bhk','041532','Web Developer','Male',1240.00),('02415204','fgh','0125345','Cloud Architect','Female',2145.00),('4535','gfesegr','345262634','Web Developer','Female',46645.00),('345345','rvsd','5234','Cloud Architect','Female',245.00),('6745','fgdr','5634','Cloud Architect','Male',654.00),('3453','dgser','5356323','Web Developer','Male',435.00),('54675436','gd fbf','65345','Web Developer','Male',5674.00),('6516555445','hjfhjn','4634','Cloud Architect','Male',64564.00);
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-05  1:33:52
