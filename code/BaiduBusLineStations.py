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

uid="46d863bf5073da5cea56faff";
busLineUrl = "http://map.baidu.com/?qt=bsl&tps=&newmap=1&uid="+uid+"&c=179";
print(busLineUrl);
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
};
res = requests.get(url=busLineUrl, headers=headers, timeout=3);
text = res.content;
print(text);
total_json = json.loads(text);
content=total_json.get("content");
print(content);
for item in content:
    print(item);
    company=item.get("company");
    endTime=item.get("endTime");
    geo=item.get("geo");
    line_direction=item.get("line_direction");
    pair_line=item.get("pair_line");
    print(pair_line);
    pairlineUid="";
    if pair_line != None:
        pairlineUid=pair_line.get("uid");
    name=item.get("name");
    startTime=item.get("startTime");

    stations=item.get("stations");
    line_sql="INSERT INTO baidu_busline_detail (uid, name, geo, end_time, start_time, line_direction, company, pair_lineuid) VALUES ('"+uid+"', '"+name+"', '"+geo+"', '"+endTime+"','"+startTime+"','"+line_direction+"','"+company+"','"+pairlineUid+"');"
    print(line_sql);
    conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost",
                            port="5432");
    cur = conn.cursor();
    try:
        cur.execute(line_sql);
        conn.commit();
    except Exception as e:
        cur.close();
        conn.close();
        print(e);
    order=0;
    if stations!=None:
        for station in stations:
            order=order+1;
            print(station);
            stationUid=station.get("uid");
            stationGeo=station.get("geo");
            stationName=station.get("name");
            print(order);
            stationSql="INSERT INTO baidu_station (uid, name, geo) VALUES ('"+stationUid+"','"+stationName+"','"+stationGeo+"');"
            try:
                conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost",
                                        port="5432");
                cur = conn.cursor();
                cur.execute(stationSql);
                conn.commit();
            except Exception as e:
                print(e);
                cur.close();
                conn.close();
            # station_num=order;
            station_num = str(order);
            line_station_rel_sql = "INSERT INTO baidu_line_station (line_uid, station_uid, station_num) VALUES ('" + uid + "','" + stationUid + "', " + station_num + ");"
            print(line_station_rel_sql);
            try:
                conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost",
                                        port="5432");
                cur = conn.cursor();
                cur.execute(line_station_rel_sql);
                conn.commit();
            except Exception as e:
                print(e);
                cur.close();
                conn.close();

