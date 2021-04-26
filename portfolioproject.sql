-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2021 at 04:57 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `portfolioproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `about_data`
--

CREATE TABLE `about_data` (
  `sno` int(11) NOT NULL,
  `user_id` varchar(30) NOT NULL,
  `text` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `acadmic_data`
--

CREATE TABLE `acadmic_data` (
  `sno` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `course` varchar(50) NOT NULL,
  `duration` varchar(25) NOT NULL,
  `institute` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `achievement_data`
--

CREATE TABLE `achievement_data` (
  `sno` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `image` text NOT NULL,
  `tag` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `certificate_data`
--

CREATE TABLE `certificate_data` (
  `sno` int(11) NOT NULL,
  `user_id` text NOT NULL,
  `tag_name` varchar(25) NOT NULL,
  `image` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `experience_data`
--

CREATE TABLE `experience_data` (
  `sno` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `duration` varchar(25) NOT NULL,
  `organisation` text NOT NULL,
  `discription` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `link_data`
--

CREATE TABLE `link_data` (
  `sno` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `profile_data`
--

CREATE TABLE `profile_data` (
  `sno` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `image` text NOT NULL,
  `name` varchar(30) NOT NULL,
  `mobile` varchar(12) NOT NULL,
  `email` varchar(100) NOT NULL,
  `location` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `project_data`
--

CREATE TABLE `project_data` (
  `sno` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `image` text NOT NULL,
  `description` text NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `skill_data`
--

CREATE TABLE `skill_data` (
  `sno` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `skill_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `totals`
--

CREATE TABLE `totals` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `totals`
--

INSERT INTO `totals` (`sno`, `name`, `total`) VALUES
(1, 'about_data', 0),
(2, 'acadmic_data', 0),
(3, 'achievement_data', 0),
(4, 'experience_data', 0),
(5, 'link_data', 0),
(6, 'profile_data', 0),
(7, 'project_data', 0),
(8, 'skill_data', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `about_data`
--
ALTER TABLE `about_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `acadmic_data`
--
ALTER TABLE `acadmic_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `achievement_data`
--
ALTER TABLE `achievement_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `certificate_data`
--
ALTER TABLE `certificate_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `experience_data`
--
ALTER TABLE `experience_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `link_data`
--
ALTER TABLE `link_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `profile_data`
--
ALTER TABLE `profile_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `project_data`
--
ALTER TABLE `project_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `skill_data`
--
ALTER TABLE `skill_data`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `totals`
--
ALTER TABLE `totals`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `about_data`
--
ALTER TABLE `about_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `acadmic_data`
--
ALTER TABLE `acadmic_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `achievement_data`
--
ALTER TABLE `achievement_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `certificate_data`
--
ALTER TABLE `certificate_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `experience_data`
--
ALTER TABLE `experience_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `link_data`
--
ALTER TABLE `link_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile_data`
--
ALTER TABLE `profile_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `project_data`
--
ALTER TABLE `project_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `skill_data`
--
ALTER TABLE `skill_data`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `totals`
--
ALTER TABLE `totals`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
