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
    try:
        # 使用收费代理
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = "HN5861W41O905A0D"
        proxyPass = "044A1683F60BB0C2"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        res = requests.get(roadUrl, proxies=proxies)
        # res = requests.get(url=roadUrl, timeout=5);
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
            road_id = base.get("poiid");
            city_code = base.get("city_adcode");
            city_name = base.get("city_name");
            print(city_name);
            address = base.get("address");
            mining_shape = spec.get("mining_shape");
            if mining_shape != None:
                shape = mining_shape.get("shape");
                if shape != None:
                    print(shape);
                    count = shape.count('|');
                    points = "";
                    polyline = "";
                    polyline = shape.split('|');
                    index = 0;
                    for line in polyline:
                        geo = line.replace(',', ' ').replace(';', ',');
                        roadSql = "INSERT INTO gaode_road (road_id, city_code, shape, name, address, city_name,order_num) VALUES ('" + road_id + "', '" + city_code + "', '" + geo + "', '" + name + "', '" + address + "', '" + city_name + "'," + str(
                            index) + ");";
                        index = index + 1;
                        conn = psycopg2.connect(database="superpower", user="postgres", password="123456",
                                                host="localhost",
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
                        reason = "无空间数据";
                        conn = psycopg2.connect(database="superpower", user="postgres", password="123456",
                                                host="localhost",
                                                port="5432");
                        cur = conn.cursor();
                        sql = "INSERT INTO gaode_road_disable (road_id,reason) VALUES ('" + id + "','" + reason + "');"
                        cur.execute(sql);
                        conn.commit();
                    except Exception as e:
                        print(e);
                        cur.close();
                        conn.close();
            else:
                try:
                    reason = "无空间数据";
                    conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                            port="5432");
                    cur = conn.cursor();
                    sql = "INSERT INTO gaode_road_disable (road_id,reason) VALUES ('" + id + "','" + reason + "');"
                    cur.execute(sql);
                    conn.commit();
                except Exception as e:
                    print(e);
                    cur.close();
                    conn.close();
        else:
            try:
                print(status);
                if status != 6:
                    reason = "返回错误状态";
                    conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                            port="5432");
                    cur = conn.cursor();
                    sql = "INSERT INTO gaode_road_disable (road_id,reason) VALUES ('" + id + "','" + reason + "');"
                    cur.execute(sql);
                    conn.commit();
            except Exception as e:
                print(e);
                cur.close();
                conn.close();
    except Exception as e:
        print(e);
        reason = "返回错误状态";
        print(reason);


# getOneRoadDate();
def batchGetBaiduBusLine():
    a = 1;
    while a == 1:
        sql = "SELECT id from gaode_road_poi t where t.id not in (select road_id from gaode_road ) and t.id not in (select road_id from gaode_road_disable ) limit 1;";
        conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        cur.execute(sql);
        keyData = cur.fetchall();
        uid = keyData[0][0];
        if uid!=None:
            getOneRoadDate(uid);
            sleepTime=random.randint(5, 6);
            print(sleepTime);
            time.sleep(sleepTime);7
        else:
            break;


batchGetBaiduBusLine();
# getOneRoadDate('BZA5QP005U');