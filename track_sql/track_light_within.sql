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

Date: 2017-10-31 16:55:04
*/


-- ----------------------------
-- Table structure for track_light_within
-- ----------------------------
DROP TABLE IF EXISTS "public"."track_light_within";
CREATE TABLE "public"."track_light_within" (
"gid" int4 DEFAULT nextval('track_inter_gid_seq'::regclass) NOT NULL,
"fint_len" numeric(10),
"geom" "public"."geometry"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Records of track_light_within
-- ----------------------------
INSERT INTO "public"."track_light_within" VALUES ('581', null, '0101000020E6100000391C46ED1A045E40B84FD7E9C64E3E40');
INSERT INTO "public"."track_light_within" VALUES ('598', null, '0101000020E61000002E2AB9CF48045E401DE68DC3E14F3E40');
INSERT INTO "public"."track_light_within" VALUES ('602', null, '0101000020E61000004BF1E07453045E40DE880B631C4F3E40');
INSERT INTO "public"."track_light_within" VALUES ('612', null, '0101000020E6100000A904B5D974045E40D6B4490B10503E40');
INSERT INTO "public"."track_light_within" VALUES ('657', null, '0101000020E6100000F918E31202055E409F6968E1DE503E40');
INSERT INTO "public"."track_light_within" VALUES ('692', null, '0101000020E61000003E353F3F66055E4005F81D5125513E40');
INSERT INTO "public"."track_light_within" VALUES ('703', null, '0101000020E61000009D47229B93055E400059948230513E40');
INSERT INTO "public"."track_light_within" VALUES ('714', null, '0101000020E6100000EA2BEEB7CA055E40E0F22E6341513E40');
INSERT INTO "public"."track_light_within" VALUES ('715', null, '0101000020E61000009023D611CF055E40C2F15DFEC8503E40');
INSERT INTO "public"."track_light_within" VALUES ('716', null, '0101000020E6100000EE00553CD3055E4031C88E052B503E40');
INSERT INTO "public"."track_light_within" VALUES ('718', null, '0101000020E6100000D5089827DD055E40D8CC1E004E4F3E40');
INSERT INTO "public"."track_light_within" VALUES ('733', null, '0101000020E6100000E611B40125065E4084D0C112BF4F3E40');
INSERT INTO "public"."track_light_within" VALUES ('735', null, '0101000020E6100000CEE52EA32B065E4049336518334F3E40');
INSERT INTO "public"."track_light_within" VALUES ('736', null, '0101000020E61000002C4AD29D32065E403245CD8B914E3E40');
INSERT INTO "public"."track_light_within" VALUES ('738', null, '0101000020E61000005251B9C03A065E4076046EAEE64D3E40');
INSERT INTO "public"."track_light_within" VALUES ('741', null, '0101000020E61000005F56F90945065E40BB1D96C9794B3E40');
INSERT INTO "public"."track_light_within" VALUES ('742', null, '0101000020E61000002E71CF7B45065E40EFC16801DB4C3E40');
INSERT INTO "public"."track_light_within" VALUES ('743', null, '0101000020E6100000CBA2537846065E404D597458534A3E40');
INSERT INTO "public"."track_light_within" VALUES ('745', null, '0101000020E610000023CF59B74B065E408FA863D0D4493E40');
INSERT INTO "public"."track_light_within" VALUES ('747', null, '0101000020E61000001EE8498851065E40FFEA304A53493E40');
INSERT INTO "public"."track_light_within" VALUES ('754', null, '0101000020E6100000B86813AA6A065E4093CD77AA56493E40');
INSERT INTO "public"."track_light_within" VALUES ('764', null, '0101000020E6100000B38578A39E065E409AC5EA4160493E40');
INSERT INTO "public"."track_light_within" VALUES ('768', null, '0101000020E610000004E25DA1BE065E409A4120EE65493E40');
INSERT INTO "public"."track_light_within" VALUES ('774', null, '0101000020E61000001FD56896E5065E40278337E26D493E40');
INSERT INTO "public"."track_light_within" VALUES ('783', null, '0101000020E6100000665F40CE48075E4076E8D78880493E40');
INSERT INTO "public"."track_light_within" VALUES ('790', null, '0101000020E6100000FACD6C509E075E402AB8F45893493E40');
INSERT INTO "public"."track_light_within" VALUES ('792', null, '0101000020E6100000912EF8FFCF075E4029E538EFA8493E40');

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Indexes structure for table track_light_within
-- ----------------------------
CREATE INDEX "track_inter_geom_idx_copy_copy" ON "public"."track_light_within" USING gist ("geom");

-- ----------------------------
-- Primary Key structure for table track_light_within
-- ----------------------------
ALTER TABLE "public"."track_light_within" ADD PRIMARY KEY ("gid");
