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

Date: 2017-11-10 16:51:20
*/


-- ----------------------------
-- Table structure for didi_track_data
-- ----------------------------
DROP TABLE IF EXISTS "public"."didi_track_data";
CREATE TABLE "public"."didi_track_data" (
"track_id" varchar(50) COLLATE "default" NOT NULL,
"order_id" varchar(50) COLLATE "default" NOT NULL,
"time" varchar(20) COLLATE "default" NOT NULL,
"x" float8,
"y" float8,
"geom" "public"."geometry",
"format_time" timestamp(6)
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Triggers structure for table didi_track_data
-- ----------------------------
CREATE TRIGGER "beforeinsertinsertdiditrack_trigger" BEFORE INSERT ON "public"."didi_track_data"
FOR EACH ROW
EXECUTE PROCEDURE "beforeinsertdiditrack"();

-- ----------------------------
-- Primary Key structure for table didi_track_data
-- ----------------------------
ALTER TABLE "public"."didi_track_data" ADD PRIMARY KEY ("track_id", "order_id", "time");
