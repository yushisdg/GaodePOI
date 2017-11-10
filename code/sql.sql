
CREATE OR REPLACE FUNCTION BeforeInsertDidiTrack() RETURNS TRIGGER AS $example_table$
BEGIN
--自动进行坐标计算，并赋值
NEW.geom=ST_PointFromText('POINT('||New.x::VARCHAR||' '||New.y::VARCHAR||')',4326);
return new;
End	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertDidiTrack_trigger Before INSERT  ON didi_track_data FOR EACH ROW EXECUTE PROCEDURE BeforeInsertDidiTrack ();


UPDATE didi_track_data t set format_time=TIMESTAMP WITH TIME ZONE 'epoch' + t.time::FLOAT * INTERVAL '1 second'


INSERT into didi_track_data_inter SELECT * from didi_track_data k where k.order_id in (select t.order_id from didi_track_data t where  ST_Intersects(st_transform (
							ST_Buffer (
								st_transform (
									ST_PointFromText('POINT('||104.07328::VARCHAR||' '||30.68588::VARCHAR||')',4326),
									3857
								),
								50
							),
							4326
						) ,t.geom) GROUP BY t.order_id) and k.format_time BETWEEN '2016-11-01 00:08:15' and '2016-11-02 09:08:15'



insert into didi_track_line(geom,order_id) select CreateLineByPoints(array(select t.geom from didi_track_data t where t.order_id=k.order_id ORDER BY t.format_time)),k.order_id  from (select order_id from didi_track_data GROUP BY order_id) k
