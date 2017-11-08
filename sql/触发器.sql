--高德数据插入触发器
CREATE OR REPLACE FUNCTION BeforeInsertGaodePOI() RETURNS TRIGGER AS $example_table$ 
BEGIN
--自动进行坐标计算，并赋值
NEW.geom=ST_PointFromText('POINT('||replace(New.location,',',' ')||')',4326);
return new;
End	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertGaodePOI_trigger Before INSERT  ON gaode_poi FOR EACH ROW EXECUTE PROCEDURE BeforeInsertGaodePOI ();


--高德数据插入触发器  生成线路
CREATE OR REPLACE FUNCTION BeforeInsertGaodeBusline() RETURNS TRIGGER AS $example_table$
declare rec  record;
declare pointCount  INTEGER;
declare i  INTEGER;
declare num INTEGER;
declare pointLntLngs VARCHAR;
declare xsArray VARCHAR[];
declare ysArray VARCHAR[];
BEGIN
	--自动进行坐标计算，并赋值
pointLntLngs:='';
i:=1;
num:=1;
xsArray=string_to_array(New.xs,',','');
ysArray=string_to_array(New.ys,',','');
pointCount=array_length(string_to_array(New.xs,',',''),1);
FOR i IN 1..pointCount loop
 pointLntLngs=pointLntLngs||xsArray[num]||' '||ysArray[num];
	if (num!=pointCount) then
	pointLntLngs=pointLntLngs||',';
	end if;
	num=num+1;
end loop;
NEW.geom=ST_LineFromText('LINESTRING('||pointLntLngs||')',4326);
return new;
end	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertGaodeBusLine_trigger Before INSERT  ON gaode_busline FOR EACH ROW EXECUTE PROCEDURE BeforeInsertGaodeBusline ();


--百度站点表触发器
CREATE OR REPLACE FUNCTION BeforeInsertBaiduStation() RETURNS TRIGGER AS $example_table$
BEGIN
--自动进行坐标计算，并赋值
NEW.geom=ST_PointFromText('POINT('||New.geo||')',4326);
return new;
End	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertBaiduStation_trigger Before INSERT  ON baidu_station FOR EACH ROW EXECUTE PROCEDURE BeforeInsertBaiduStation ();


CREATE OR REPLACE FUNCTION BeforeInsertBaiduBusLine() RETURNS TRIGGER AS $example_table$
BEGIN
--自动进行坐标计算，并赋值
NEW.geom=ST_LineFromText('LINESTRING('||New.geo||')',4326);
return new;
End	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertBaiduBusLine_trigger Before INSERT  ON baidu_busline_detail FOR EACH ROW EXECUTE PROCEDURE BeforeInsertBaiduBusLine ();



select LayerTransform('gaode_station_copy','GCJ2BD');
inputlayer：输入的表名称，是个要加/纠偏的table名称，table是个空间表。
transformtype：加/纠偏方式，支持以下6种'BD2GCJ', 'GCJ2BD', 'WGS2GCJ','GCJ2WGS','BD2WGS','WGS2BD'，分别代表 百度转谷歌高德，谷歌高德转百度，84转火星，火星转84，百度转84,84转百度。


--高德道路插入触发器
CREATE OR REPLACE FUNCTION BeforeInsertGaodeRoad() RETURNS TRIGGER AS $example_table$
BEGIN
--自动进行坐标计算，并赋值
NEW.geom=ST_LineFromText('LINESTRING('||NEW.shape||')',4326);
return new;
End	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertGaodeRoad_trigger Before INSERT  ON gaode_road FOR EACH ROW EXECUTE PROCEDURE BeforeInsertGaodeRoad ();


update gaode_residential_region t set geom=ST_PolygonFromText('POLYGON(('||replace(replace(t.shape,',', ' '),';',',')||'))',4326) ;


--高德Residential插入触发器
CREATE OR REPLACE FUNCTION BeforeInsertGaodeResidential() RETURNS TRIGGER AS $example_table$
BEGIN
--自动进行坐标计算，并赋值
NEW.geom=ST_PolygonFromText('POLYGON(('||replace(replace(New.shape,',', ' '),';',',')||'))',4326);
return new;
End	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertGaodeResidential_trigger Before INSERT  ON gaode_residential_region FOR EACH ROW EXECUTE PROCEDURE BeforeInsertGaodeResidential ();



 --insert into gaode_poi_gaojia_inter select * from gaode_poi t where t.typecode like '%190308%' or  t.typecode like '%190309%'   --高架出入口
 --insert into gaode_poi_subwaystation select * from gaode_poi t where t.typecode like '%15050%'   --地铁站
 --insert into gaode_poi_building select * from gaode_poi t where t.typecode like '%12020%'   --写字楼
--insert into gaode_poi_company select * from gaode_poi t where t.typecode like '%170%'   --公司
--insert into gaode_poi_governmental select * from gaode_poi t where t.typecode like '%130%'   --政府部门
--insert into gaode_poi_industrialpark select * from gaode_poi t where t.typecode like '%120100%'   --工业园区
--insert into gaode_poi_inter select * from gaode_poi t where t.typecode like '%190302%'   --路口
--insert into gaode_poi_museum select * from gaode_poi t where t.typecode like '%140%'   --博物馆
--insert into gaode_poi_parking select * from gaode_poi t where t.typecode like '%15090%'   --博物馆
--insert into gaode_poi_residentialarea select * from gaode_poi t where t.typecode like '%12030%'   --小区
--insert into gaode_poi_school select * from gaode_poi t where t.typecode like '%14120%'   --学校
--insert into gaode_poi_subwaystation select * from gaode_poi t where t.typecode like '%15050%'   --地铁
--insert into gaode_poi_residentialarea select * from gaode_poi t where t.typecode like '%12030%'   --地铁