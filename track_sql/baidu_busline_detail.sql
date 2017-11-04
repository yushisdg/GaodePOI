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

Date: 2017-11-04 16:55:46
*/


-- ----------------------------
-- Table structure for baidu_busline_detail
-- ----------------------------
DROP TABLE IF EXISTS "public"."baidu_busline_detail";
CREATE TABLE "public"."baidu_busline_detail" (
"uid" varchar(50) COLLATE "default" NOT NULL,
"name" varchar(50) COLLATE "default",
"geo" text COLLATE "default",
"end_time" time(6),
"start_time" time(6),
"line_direction" varchar(50) COLLATE "default",
"company" varchar(50) COLLATE "default",
"pair_lineuid" varchar(50) COLLATE "default",
"geom" "public"."geometry"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Triggers structure for table baidu_busline_detail
-- ----------------------------
CREATE TRIGGER "beforeinsertinsertbaidubusline_trigger" BEFORE INSERT ON "public"."baidu_busline_detail"
FOR EACH ROW
EXECUTE PROCEDURE "beforeinsertbaidubusline"();

-- ----------------------------
-- Primary Key structure for table baidu_busline_detail
-- ----------------------------
ALTER TABLE "public"."baidu_busline_detail" ADD PRIMARY KEY ("uid");
