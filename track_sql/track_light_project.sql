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

Date: 2017-10-31 16:54:56
*/


-- ----------------------------
-- Table structure for track_light_project
-- ----------------------------
DROP TABLE IF EXISTS "public"."track_light_project";
CREATE TABLE "public"."track_light_project" (
"gid" int4 DEFAULT nextval('track_inter_gid_seq'::regclass) NOT NULL,
"fint_len" numeric(10),
"geom" "public"."geometry"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Records of track_light_project
-- ----------------------------
INSERT INTO "public"."track_light_project" VALUES ('818', null, '0101000020E6100000103413D767075E40C416BCFC96493E40');
INSERT INTO "public"."track_light_project" VALUES ('819', null, '0101000020E6100000F7AEDDAA1B045E404C7947F8D04E3E40');
INSERT INTO "public"."track_light_project" VALUES ('820', null, '0101000020E610000096676CC649045E4048EB7060E04F3E40');
INSERT INTO "public"."track_light_project" VALUES ('821', null, '0101000020E61000006E7A914C50045E405F6C64171E4F3E40');
INSERT INTO "public"."track_light_project" VALUES ('822', null, '0101000020E6100000D063EA9474045E40D2DB094814503E40');
INSERT INTO "public"."track_light_project" VALUES ('823', null, '0101000020E61000009F55BC9500055E404FE0B356E8503E40');
INSERT INTO "public"."track_light_project" VALUES ('824', null, '0101000020E6100000B6E3943E66055E4083E48F0733513E40');
INSERT INTO "public"."track_light_project" VALUES ('825', null, '0101000020E6100000FBD4D56C93055E402C68F7F53A513E40');
INSERT INTO "public"."track_light_project" VALUES ('826', null, '0101000020E61000004A5ADEA3CA055E401C692B2A41513E40');
INSERT INTO "public"."track_light_project" VALUES ('827', null, '0101000020E610000002123E38CF055E40BDC56A1EC9503E40');
INSERT INTO "public"."track_light_project" VALUES ('828', null, '0101000020E6100000FA15B0C9D3055E40EB373D572B503E40');
INSERT INTO "public"."track_light_project" VALUES ('829', null, '0101000020E61000004FD99BC9DD055E4024D3FF9D584F3E40');
INSERT INTO "public"."track_light_project" VALUES ('830', null, '0101000020E6100000FDA454EB24065E408ED7722EBB4F3E40');
INSERT INTO "public"."track_light_project" VALUES ('831', null, '0101000020E6100000B30B26C92D065E40C99B2ABD354F3E40');
INSERT INTO "public"."track_light_project" VALUES ('832', null, '0101000020E610000078B6BE0A35065E403D284ABA934E3E40');
INSERT INTO "public"."track_light_project" VALUES ('833', null, '0101000020E6100000C79EADE13D065E40C4CAC6E2E84D3E40');
INSERT INTO "public"."track_light_project" VALUES ('834', null, '0101000020E6100000E566344248065E40D4D8B175794B3E40');
INSERT INTO "public"."track_light_project" VALUES ('835', null, '0101000020E61000002B503DA947065E40EEC3E4CCDB4C3E40');
INSERT INTO "public"."track_light_project" VALUES ('836', null, '0101000020E6100000497B106047065E40534AFE37534A3E40');
INSERT INTO "public"."track_light_project" VALUES ('837', null, '0101000020E61000003DDB22DB4D065E401EF71E1FD7493E40');
INSERT INTO "public"."track_light_project" VALUES ('838', null, '0101000020E61000004A193E4F55065E4083BB1BFF65493E40');
INSERT INTO "public"."track_light_project" VALUES ('839', null, '0101000020E61000007704F8956A065E40A920B89664493E40');
INSERT INTO "public"."track_light_project" VALUES ('840', null, '0101000020E6100000D36D54A09E065E40D825B7CF6C493E40');
INSERT INTO "public"."track_light_project" VALUES ('841', null, '0101000020E610000033F66E90BE065E4052DA690370493E40');
INSERT INTO "public"."track_light_project" VALUES ('842', null, '0101000020E6100000088A0197E5065E408903C6F17B493E40');
INSERT INTO "public"."track_light_project" VALUES ('843', null, '0101000020E610000036896E6549075E4028CCCB4F91493E40');
INSERT INTO "public"."track_light_project" VALUES ('844', null, '0101000020E61000006CB1DC249D075E404A2A09E19D493E40');
INSERT INTO "public"."track_light_project" VALUES ('845', null, '0101000020E610000055A7EEFACF075E4060CA082FAA493E40');

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Indexes structure for table track_light_project
-- ----------------------------
CREATE INDEX "track_inter_geom_idx_copy_copy1" ON "public"."track_light_project" USING gist ("geom");

-- ----------------------------
-- Primary Key structure for table track_light_project
-- ----------------------------
ALTER TABLE "public"."track_light_project" ADD PRIMARY KEY ("gid");
