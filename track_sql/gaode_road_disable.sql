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

Date: 2017-11-06 19:28:06
*/


-- ----------------------------
-- Table structure for gaode_road_disable
-- ----------------------------
DROP TABLE IF EXISTS "public"."gaode_road_disable";
CREATE TABLE "public"."gaode_road_disable" (
"road_id" varchar(50) COLLATE "default" NOT NULL
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Triggers structure for table gaode_road_disable
-- ----------------------------
CREATE TRIGGER "beforeinsertinsertgaoderoad_trigger" BEFORE INSERT ON "public"."gaode_road_disable"
FOR EACH ROW
EXECUTE PROCEDURE "beforeinsertgaoderoad"();

-- ----------------------------
-- Primary Key structure for table gaode_road_disable
-- ----------------------------
ALTER TABLE "public"."gaode_road_disable" ADD PRIMARY KEY ("road_id");
