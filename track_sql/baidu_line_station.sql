/*
Navicat PGSQL Data Transfer

Source Server         : localhost
Source Server Version : 90411
Source Host           : localhost:5432
Source Database       : superpower
Source Schema         : public

Target Server Type    : PGSQL
Target Server Version : 90411
File Encoding         : 65001

Date: 2017-11-04 16:56:17
*/


-- ----------------------------
-- Table structure for baidu_line_station
-- ----------------------------
DROP TABLE IF EXISTS "public"."baidu_line_station";
CREATE TABLE "public"."baidu_line_station" (
"line_uid" varchar(50) COLLATE "default" NOT NULL,
"station_uid" varchar(50) COLLATE "default" NOT NULL,
"station_num" int4 NOT NULL
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table baidu_line_station
-- ----------------------------
ALTER TABLE "public"."baidu_line_station" ADD PRIMARY KEY ("line_uid", "station_uid");