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

Date: 2017-11-04 16:56:07
*/


-- ----------------------------
-- Table structure for baidu_busline
-- ----------------------------
DROP TABLE IF EXISTS "public"."baidu_busline";
CREATE TABLE "public"."baidu_busline" (
"uid" varchar(50) COLLATE "default" NOT NULL,
"addr" varchar(50) COLLATE "default"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table baidu_busline
-- ----------------------------
ALTER TABLE "public"."baidu_busline" ADD PRIMARY KEY ("uid");
