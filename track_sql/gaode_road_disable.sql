/*
Navicat PGSQL Data Transfer

Source Server         : postgresql-local
Source Server Version : 90411
Source Host           : localhost:5432
Source Database       : mydatabase
Source Schema         : public

Target Server Type    : PGSQL
Target Server Version : 90411
File Encoding         : 65001

Date: 2017-11-07 06:51:51
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
-- Records of gaode_road_disable
-- ----------------------------
INSERT INTO "public"."gaode_road_disable" VALUES ('B023B18HX1');
INSERT INTO "public"."gaode_road_disable" VALUES ('B023B1CS8O');
INSERT INTO "public"."gaode_road_disable" VALUES ('B0FFF5NZCK');
INSERT INTO "public"."gaode_road_disable" VALUES ('B0FFGQ4SDY');

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------
