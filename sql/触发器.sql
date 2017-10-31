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