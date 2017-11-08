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



def getOneResidentialDate(id):
    roadUrl ="http://ditu.amap.com/detail/get/detail?id="+id;
    print(roadUrl);
    try:
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
            spec = data.get('spec');

            name = base.get("name");
            region_id = base.get("poiid");
            city_code = base.get("city_adcode");
            city_name = base.get("city_name");
            tag = base.get("tag");
            print(city_name);
            address = base.get("address");
            mining_shape = spec.get("mining_shape");
            residential = data.get("residential");
            service_parking = "";
            green_rate = "";
            opening_data = "";
            price = "";
            volume_rate = "";
            intro = "";
            property_fee = "";
            area_total = "";
            if residential!=None:
                service_parking = residential.get("service_parking");
                green_rate = residential.get("green_rate");
                opening_data = residential.get("opening_data");
                price = residential.get("price");
                volume_rate = str(residential.get("volume_rate"));
                intro = residential.get("intro");
                property_fee = residential.get("property_fee");
                area_total = residential.get("area_total");
            if mining_shape != None:
                shape = mining_shape.get("shape");
                center = mining_shape.get("center");
                area = mining_shape.get("area");
                if service_parking==None:
                    service_parking="";
                if green_rate == None:
                    green_rate = "";
                if opening_data == None:
                    opening_data = "";
                if price == None:
                    price = "";
                if volume_rate == None:
                    volume_rate = "";
                if intro == None:
                    intro = "";
                if property_fee == None:
                    property_fee = "";
                if area_total == None:
                    area_total = "";
                sql = "INSERT INTO gaode_residential_region(region_id, city_code, shape, name, address, city_name, area, center, tag, service_parking, volume_rate, area_total, price, intro, opening_data, property_fee) VALUES ('" + region_id + "', '" + city_code + "', '" + shape + "', '" + name + "', '" + address + "', '" + city_name + "', " + area + ", '" + center + "', '" + tag + "', '" + service_parking + "', '" + volume_rate + "', '" + area_total + "', '" + price + "', '" + intro + "', '" + opening_data + "', '" + property_fee + "');"
                print(sql);
                conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                        port="5432");
                cur = conn.cursor();
                try:
                    cur.execute(sql);
                    conn.commit();
                except Exception as e:
                    cur.close();
                    conn.close();
                    print(e);
            else:

                reason="没有空间数据";
                print(reason);
                conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                        port="5432");
                cur = conn.cursor();
                sql = "INSERT INTO gaode_residential_disable (region_id,reason) VALUES ('" + id + "','" + reason + "');"
                cur.execute(sql);
                conn.commit();
        else:
            reason = "返回错误状态";
            print(reason);
            conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                    port="5432");
            cur = conn.cursor();
            sql = "INSERT INTO gaode_residential_disable (region_id,reason) VALUES ('" + id + "','" + reason + "');"
            cur.execute(sql);
            conn.commit();
    except Exception as e:
        print(e);
        reason="请求失败";
        conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        sql = "INSERT INTO gaode_residential_disable (region_id,reason) VALUES ('" + id + "','" + reason + "');"
        cur.execute(sql);
        conn.commit();





def batchGetResidential():
    a = 1;
    while a == 1:
        sql = "SELECT id from gaode_poi_residentialarea t where t.id not in (select region_id from gaode_residential_region ) and t.id not in (select region_id from gaode_residential_disable ) limit 1;";
        conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        cur.execute(sql);
        keyData = cur.fetchall();
        uid = keyData[0][0];
        if uid!=None:
            getOneResidentialDate(uid);
            sleepTime=random.randint(75, 85);
            print(sleepTime);
            time.sleep(sleepTime);
        else:
            break;


batchGetResidential();
# getOneRoadDate('BZA5QP005U');

# getOneResidentialDate('B023B00273');