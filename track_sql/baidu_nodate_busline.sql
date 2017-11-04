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

Date: 2017-11-04 16:56:33
*/


-- ----------------------------
-- Table structure for baidu_nodate_busline
-- ----------------------------
DROP TABLE IF EXISTS "public"."baidu_nodate_busline";
CREATE TABLE "public"."baidu_nodate_busline" (
"uid" varchar COLLATE "default" NOT NULL
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table baidu_nodate_busline
-- ----------------------------
ALTER TABLE "public"."baidu_nodate_busline" ADD PRIMARY KEY ("uid");
