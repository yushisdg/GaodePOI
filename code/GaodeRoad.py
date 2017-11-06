import requests
import json
import time
from pandas import DataFrame
import psycopg2
import math
import random
import sys
import sys
from urllib.request import urlopen



def getOneRoadDate(id):
    roadUrl ="http://ditu.amap.com/detail/get/detail?id="+id;
    print(roadUrl);
    res = requests.get(url=roadUrl, timeout=3);
    content = res.content;
    print(content);
    total_json = json.loads(content);
    print(total_json);
    status = total_json.get("status");
    print(status);
    if status == '1':
        data = total_json.get("data");
        base = data.get('base');
        spec=data.get('spec');
        name=base.get("name");
        road_id=base.get("poiid");
        city_code=base.get("city_adcode");
        city_name=base.get("city_name");
        print(city_name);
        address=base.get("address");
        mining_shape=spec.get("mining_shape");
        shape=mining_shape.get("shape");
        print(shape);
        count=shape.count('|');
        points="";
        polyline="";
        if count==0:
            polyline = shape.replace('|', ';').split(";");
        elif count==1:
            polyline = shape.replace('|', ';').split(";");
        # elif count==2:
        #     print(2);
        #     polyline=shape.split('|');
        #     points=polyline[1]+";"+polyline[0]+";";
        #     pts=polyline[2].split(';');
        #     pts.reverse();
        #     index1=0;
        #     for pt in pts:
        #         points=points+pt;
        #         index1 = index1 + 1;
        #         if index1 <len(pts):
        #             points = points + ";"
        #     print(points);
        #     polyline=points.split(";");
        else:
            polyline = shape.split('|');
            segentCount = len(polyline);
            print(segentCount);
            for segIndex in range(0,segentCount-2):
                print(segIndex);
                points=points+polyline[segIndex]+";";
            print("point: "+points);
            pts = polyline[segentCount-1].split(';');
            pts.reverse();
            index1 = 0;
            for pt in pts:
                points = points + pt;
                index1 = index1 + 1;
                if index1 < len(pts):
                    points = points + ";"
            print(points);
            polyline = points.split(";");
        print(polyline);
        index = 0;
        geo="";
        for item in polyline:
            item=item.replace(',',' ');
            index = index + 1;
            geo=geo+item;
            if index != len(polyline):
                geo = geo + ","
        print(geo);
        roadSql="INSERT INTO gaode_road (road_id, city_code, shape, name, address, city_name) VALUES ('"+road_id+"', '"+city_code+"', '"+geo+"', '"+name+"', '"+address+"', '"+city_name+"');";
        conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        try:
            cur.execute(roadSql);
            conn.commit();
        except Exception as e:
            cur.close();
            conn.close();
            print(e);
    else:
        try:
            conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                    port="5432");
            cur = conn.cursor();
            sql = "INSERT INTO gaode_road_disable (road_id) VALUES ('" + id + "');"
            cur.execute(sql);
            conn.commit();
        except Exception as e:
            print(e);
            cur.close();
            conn.close();

# getOneRoadDate();
def batchGetBaiduBusLine():
    a = 1;
    while a == 1:
        sql = "SELECT id from gaode_road_poi t where t.id not in (select road_id from gaode_road ) limit 1;";
        conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        cur.execute(sql);
        keyData = cur.fetchall();
        uid = keyData[0][0];
        if uid!=None:
            getOneRoadDate(uid);
            sleepTime=random.randint(40, 50);
            print(sleepTime);
            time.sleep(sleepTime);
        else:
            break;


# batchGetBaiduBusLine();
getOneRoadDate('BZA5QP005U');