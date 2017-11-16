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

Date: 2017-11-10 16:51:28
*/


-- ----------------------------
-- Table structure for didi_order_data
-- ----------------------------
DROP TABLE IF EXISTS "public"."didi_order_data";
CREATE TABLE "public"."didi_order_data" (
"order_id" varchar(50) COLLATE "default" NOT NULL,
"start_time" varchar(20) COLLATE "default",
"end_time" varchar(20) COLLATE "default",
"from_x" float8,
"from_y" float8,
"to_x" float8,
"to_y" float8
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table didi_order_data
-- ----------------------------
ALTER TABLE "public"."didi_order_data" ADD PRIMARY KEY ("order_id");
