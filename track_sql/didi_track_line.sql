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

Date: 2017-11-10 16:51:39
*/


-- ----------------------------
-- Table structure for didi_track_line
-- ----------------------------
DROP TABLE IF EXISTS "public"."didi_track_line";
CREATE TABLE "public"."didi_track_line" (
"user_id" varchar(50) COLLATE "default",
"order_id" varchar(50) COLLATE "default" NOT NULL,
"geom" "public"."geometry"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table didi_track_line
-- ----------------------------
ALTER TABLE "public"."didi_track_line" ADD PRIMARY KEY ("order_id");
