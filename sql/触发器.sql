--高德数据插入触发器
CREATE OR REPLACE FUNCTION BeforeInsertGaodePOI() RETURNS TRIGGER AS $example_table$ 
BEGIN
--自动进行坐标计算，并赋值
NEW.geom=ST_PointFromText('POINT('||replace(New.location,',',' ')||')',4326);
return new;
End	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertGaodePOI_trigger Before INSERT  ON gaode_poi FOR EACH ROW EXECUTE PROCEDURE BeforeInsertGaodePOI ();