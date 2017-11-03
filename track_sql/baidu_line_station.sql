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

Date: 2017-11-03 22:53:49
*/


-- ----------------------------
-- Table structure for baidu_line_station
-- ----------------------------
DROP TABLE IF EXISTS "public"."baidu_line_station";
CREATE TABLE "public"."baidu_line_station" (
"line_uid" varchar(50) COLLATE "default" NOT NULL,
"station_uid" varchar(50) COLLATE "default" NOT NULL,
"station_num" int4 NOT NULL
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Records of baidu_line_station
-- ----------------------------
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '07427205be56bbaad618b765', '1');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '09d5ef94d32ba0a96ea3ccb7', '17');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '1495ae857e84c49960180977', '26');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '1579a100798b9033ff0eb078', '5');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '15e76a9d6422f30780a12e10', '16');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '2172a6ac561a2bb540ab9a4c', '21');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '2d144c4ea2d2d21a081cc72c', '15');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '37e9fe24ccf5f639a21de9ed', '23');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '475cbbdd1939d9532e4733db', '12');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '599c180eea669e7d2811d1f8', '14');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '5f7eb76b0f468ec52b06ce60', '13');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '6577c82035116bb07dc8765d', '4');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '87a2fbecf60f3894d6b74ef3', '6');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '915ae9b6cfac417c88f15da4', '10');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', '9b3e27cde40d23d1a2046400', '22');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'a0553262883b29aaab175aee', '24');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'a0c297fcb45343a336b06c40', '25');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'ac8e32edb9a5171cb31e3621', '2');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'b3628036d9ae85ac9122e096', '19');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'c22013d175f3045997f08c45', '9');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'cacf73144684621f52e5c566', '11');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'e7b8a969299a6cae1d580055', '20');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'ed934654d3411dba28b97cde', '7');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'ef44b579bf2d9f4beee4a563', '8');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'f98c352b9dbc3b63128824bf', '3');
INSERT INTO "public"."baidu_line_station" VALUES ('46d863bf5073da5cea56faff', 'fc4fdc8d1cbafb062afc48b4', '18');

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table baidu_line_station
-- ----------------------------
ALTER TABLE "public"."baidu_line_station" ADD PRIMARY KEY ("line_uid", "station_uid");
