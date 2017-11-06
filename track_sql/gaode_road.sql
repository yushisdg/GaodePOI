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

Date: 2017-11-06 19:28:00
*/


-- ----------------------------
-- Table structure for gaode_road
-- ----------------------------
DROP TABLE IF EXISTS "public"."gaode_road";
CREATE TABLE "public"."gaode_road" (
"road_id" varchar(50) COLLATE "default" NOT NULL,
"city_code" varchar(50) COLLATE "default",
"shape" text COLLATE "default",
"name" varchar(50) COLLATE "default",
"address" varchar(255) COLLATE "default",
"city_name" varchar(50) COLLATE "default",
"geom" "public"."geometry"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Triggers structure for table gaode_road
-- ----------------------------
CREATE TRIGGER "beforeinsertinsertgaoderoad_trigger" BEFORE INSERT ON "public"."gaode_road"
FOR EACH ROW
EXECUTE PROCEDURE "beforeinsertgaoderoad"();

-- ----------------------------
-- Primary Key structure for table gaode_road
-- ----------------------------
ALTER TABLE "public"."gaode_road" ADD PRIMARY KEY ("road_id");
