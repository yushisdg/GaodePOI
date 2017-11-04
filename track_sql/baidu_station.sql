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

Date: 2017-11-04 16:56:45
*/


-- ----------------------------
-- Table structure for baidu_station
-- ----------------------------
DROP TABLE IF EXISTS "public"."baidu_station";
CREATE TABLE "public"."baidu_station" (
"uid" varchar(50) COLLATE "default" NOT NULL,
"name" varchar(50) COLLATE "default",
"geo" varchar(255) COLLATE "default",
"geom" "public"."geometry"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Triggers structure for table baidu_station
-- ----------------------------
CREATE TRIGGER "beforeinsertinsertbaidustation_trigger" BEFORE INSERT ON "public"."baidu_station"
FOR EACH ROW
EXECUTE PROCEDURE "beforeinsertbaidustation"();

-- ----------------------------
-- Primary Key structure for table baidu_station
-- ----------------------------
ALTER TABLE "public"."baidu_station" ADD PRIMARY KEY ("uid");
