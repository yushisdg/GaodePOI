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

Date: 2017-11-08 06:43:49
*/


-- ----------------------------
-- Table structure for gaode_residential_disable
-- ----------------------------
DROP TABLE IF EXISTS "public"."gaode_residential_disable";
CREATE TABLE "public"."gaode_residential_disable" (
"region_id" varchar(50) COLLATE "default" NOT NULL,
"reason" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Records of gaode_residential_disable
-- ----------------------------
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B008C8', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B0129F', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B0274D', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B05MYU', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B05S33', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B05SJQ', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B05T2E', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B05UWB', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B05V44', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B05VIU', '没有空间数据');
INSERT INTO "public"."gaode_residential_disable" VALUES ('B023B0644H', '没有空间数据');

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------
