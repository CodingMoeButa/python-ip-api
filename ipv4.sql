/*
 Navicat Premium Data Transfer

 Source Server         : hk
 Source Server Type    : MariaDB
 Source Server Version : 100332
 Source Host           : hk.zimoe.com:3306
 Source Schema         : ipapi

 Target Server Type    : MariaDB
 Target Server Version : 100332
 File Encoding         : 65001

 Date: 02/02/2022 20:11:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ipv4
-- ----------------------------
DROP TABLE IF EXISTS `ipv4`;
CREATE TABLE `ipv4`  (
  `_1` tinyint(3) UNSIGNED NOT NULL,
  `_2` tinyint(3) UNSIGNED NOT NULL,
  `_3` tinyint(3) UNSIGNED NOT NULL,
  `countryCode` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `region` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `city` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `lat` float NULL DEFAULT NULL,
  `lon` float NULL DEFAULT NULL,
  `isp` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `org` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `as` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `asname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `mobile` tinyint(4) NOT NULL DEFAULT 0,
  `hosting` tinyint(4) NOT NULL DEFAULT 0
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
