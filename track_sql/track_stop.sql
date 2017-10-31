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

Date: 2017-10-31 16:55:55
*/


-- ----------------------------
-- Table structure for track_stop
-- ----------------------------
DROP TABLE IF EXISTS "public"."track_stop";
CREATE TABLE "public"."track_stop" (
"gid" int4 DEFAULT nextval('track_points_gid_seq'::regclass) NOT NULL,
"__gid" numeric(10),
"____gid" numeric(10),
"track_fid" numeric(10),
"track_seg_" numeric(10),
"track_se_1" numeric(10),
"ele" numeric(32),
"time" varchar(24) COLLATE "default",
"course" numeric,
"speed" numeric,
"magvar" numeric,
"geoidheigh" numeric,
"name" varchar(254) COLLATE "default",
"cmt" varchar(254) COLLATE "default",
"desc" varchar(254) COLLATE "default",
"src" varchar(254) COLLATE "default",
"url" varchar(254) COLLATE "default",
"urlname" varchar(254) COLLATE "default",
"sym" varchar(254) COLLATE "default",
"type" varchar(254) COLLATE "default",
"fix" varchar(254) COLLATE "default",
"sat" numeric(10),
"hdop" numeric,
"vdop" numeric,
"pdop" numeric,
"ageofdgpsd" numeric,
"dgpsid" numeric(10),
"geom" "public"."geometry"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Records of track_stop
-- ----------------------------
INSERT INTO "public"."track_stop" VALUES ('370', null, null, null, null, null, null, '2017/10/30 23:33:33.000', null, '1.938921451568604', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E61000009A9F8E536A075E405C8DA3BA95493E40');
INSERT INTO "public"."track_stop" VALUES ('371', null, null, null, null, null, null, '2017/10/30 23:40:01.000', null, '1.214240431785584', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E61000007830E0D96F065E402DD1C0C564493E40');
INSERT INTO "public"."track_stop" VALUES ('372', null, null, null, null, null, null, '2017/10/30 23:41:20.000', null, '1.501512765884399', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E610000042E4A53148065E40C5FBB456444A3E40');
INSERT INTO "public"."track_stop" VALUES ('373', null, null, null, null, null, null, '2017/10/30 23:45:41.000', null, '1.911740660667419', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E6100000162ADBED48065E4045968435054C3E40');
INSERT INTO "public"."track_stop" VALUES ('374', null, null, null, null, null, null, '2017/10/30 23:50:14.000', null, '1.117431521415710', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E6100000F9E5098127065E407C60576FA54F3E40');
INSERT INTO "public"."track_stop" VALUES ('375', null, null, null, null, null, null, '2017/10/30 23:51:38.000', null, '1.294616222381592', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E6100000F694273CD7055E4012D97A30D34F3E40');
INSERT INTO "public"."track_stop" VALUES ('376', null, null, null, null, null, null, '2017/10/30 23:54:04.000', null, '1.435609698295593', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E6100000DC77DDECD0055E40312F505FA6503E40');
INSERT INTO "public"."track_stop" VALUES ('377', null, null, null, null, null, null, '2017/10/30 23:54:32.000', null, '1.603954672813416', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E6100000CB02B3FBCB055E40D48F1E7B19513E40');
INSERT INTO "public"."track_stop" VALUES ('378', null, null, null, null, null, null, '2017/10/30 23:57:29.000', null, '0.844519436359406', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E6100000159B951327055E408AE2234217513E40');
INSERT INTO "public"."track_stop" VALUES ('379', null, null, null, null, null, null, '2017/10/31 00:01:39.000', null, '1.632839918136597', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E61000003C1B7D5DDF045E40A364099FA6503E40');
INSERT INTO "public"."track_stop" VALUES ('380', null, null, null, null, null, null, '2017/10/31 00:02:15.000', null, '1.420155048370361', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E61000007A7CAF32C7045E40DB55FABC7F503E40');
INSERT INTO "public"."track_stop" VALUES ('381', null, null, null, null, null, null, '2017/10/31 00:02:57.000', null, '1.841191172599793', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E610000091BC8880A0045E40536EB6DD43503E40');
INSERT INTO "public"."track_stop" VALUES ('382', null, null, null, null, null, null, '2017/10/31 00:05:39.000', null, '1.384140491485596', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E6100000423FBAE54D045E405099B6F2444F3E40');
INSERT INTO "public"."track_stop" VALUES ('383', null, null, null, null, null, null, '2017/10/31 00:06:23.000', null, '1.555835962295532', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E61000009B2995B24E045E407E75CD84144F3E40');
INSERT INTO "public"."track_stop" VALUES ('384', null, null, null, null, null, null, '2017/10/31 00:06:38.000', null, '1.468617320060730', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E6100000FA72F4C149045E407E6E31A60E4F3E40');
INSERT INTO "public"."track_stop" VALUES ('385', null, null, null, null, null, null, '2017/10/31 00:07:35.000', null, '1.538100838661194', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '0101000020E61000009021F0CA12045E4082EFABC8264F3E40');

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Indexes structure for table track_stop
-- ----------------------------
CREATE INDEX "track_points_geom_idx_copy" ON "public"."track_stop" USING gist ("geom");

-- ----------------------------
-- Primary Key structure for table track_stop
-- ----------------------------
ALTER TABLE "public"."track_stop" ADD PRIMARY KEY ("gid");
