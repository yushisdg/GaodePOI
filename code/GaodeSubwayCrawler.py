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



def getOneBusLineDate(lineName):
    busLineUrl = "http://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=10&city=330100&geoobj=119.384533|30.109422|121.362072|30.488845&keywords="+lineName;
    print(busLineUrl);
    res = requests.get(url=busLineUrl,timeout=3);
    content=res.content;
    total_json = json.loads(content);
    print(total_json);
    status=total_json.get("status");
    print(status);
    if status=='1':
        print("--------------------------------------------");
        data = total_json.get("data");
        busline_list = data.get('busline_list');
        if busline_list!=None:
            print("线路信息");
            print(busline_list);
            if any(busline_list):
                i = 0;
                for line in busline_list:
                    totalSql = "";
                    bus_lineid = line.get("id");
                    areacode = line.get("areacode");
                    xs = line.get("xs");
                    front_name = line.get("front_name");
                    terminal_name = line.get("terminal_name");
                    terminal_spell = line.get("terminal_spell");
                    basic_price = line.get("basic_price");
                    type = line.get("type");
                    company = line.get("company");
                    status = line.get("status");
                    ic_card = line.get("ic_card");
                    description = line.get("description");
                    key_name = line.get("key_name");
                    start_time = line.get("start_time");
                    front_spell = line.get("front_spell");
                    ys = line.get("ys");
                    total_price = line.get("total_price");
                    name = line.get("name");
                    auto = line.get("auto");
                    interval = line.get("interval");
                    bounds = line.get("bounds");
                    air = line.get("air");
                    length = line.get("length");
                    end_time = line.get("end_time");
                    is_realtime = line.get("is_realtime");
                    stations = line.get("stations");
                    # print(bus_lineid+" ,"+areacode+" ,"+xs+" ,"+front_name+" ,"+terminal_name+" ,"+terminal_spell+" ,"+basic_price+" ,"+type+" ,"+company+" ,"+status+" ,"+ic_card+" ,"+description+" ,"+key_name+" ,"+start_time+" ,"+front_spell+" ,"+ys+" ,"+total_price+" ,"+name+" ,"+auto+" ,"+interval+" ,"+bounds+" ,"+air+" ,"+length+" ,"+end_time+" ,"+is_realtime);
                    linesql = "INSERT INTO gaode_subway (bus_lineid, areacode, xs, front_name,terminal_name, terminal_spell, basic_price, type, company,status, ic_card, description, key_name, start_time, front_spell, ys, total_price, name, auto, interval, bounds, air, length, end_time, is_realtime) VALUES" + "('" + bus_lineid + " ','" + areacode + " ','" + xs + " ','" + front_name + " ','" + terminal_name + " ','" + terminal_spell + " ','" + basic_price + " ','" + type + " ','" + company + " ','" + status + " ','" + ic_card + " ','" + description + " ','" + key_name + " ','" + start_time + " ','" + front_spell + " ','" + ys + " ','" + total_price + " ','" + name + " ','" + auto + " ','" + interval + " ','" + bounds + " ','" + air + " ','" + length + " ','" + end_time + " ','" + is_realtime + "');";

                    conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                            port="5432");
                    cur = conn.cursor();
                    try:
                        cur.execute(linesql);
                        conn.commit();
                    except Exception as e:
                        cur.close();
                        conn.close();
                        print(e);
                    for station in stations:
                        poiid2 = station.get("poiid2");
                        status = station.get("status");
                        trans_flag = station.get("trans_flag");
                        code = station.get("code");
                        name = station.get("name");
                        station_num = station.get("station_num");
                        poiid1 = station.get("poiid1");
                        start_time = station.get("start_time");
                        spell = station.get("spell");
                        station_id = station.get("station_id");
                        end_time = station.get("end_time");
                        xy_coords = station.get("xy_coords");
                        # print(poiid2+" ,"+status+" ,"+trans_flag+" ,"+code+" ,"+name+" ,"+station_num+" ,"+poiid1+" ,"+start_time+" ,"+spell+" ,"+station_id+" ,"+end_time+" ,"+xy_coords);
                        station_sql = "INSERT INTO gaode_stations(poiid2,status,trans_flag,code,name,poiid1,start_time,spell,station_id,end_time,xy_coords) VALUES('" + poiid2 + "' ,'" + status + "' ,'" + trans_flag + "' ,'" + code + "' ,'" + name + "' ,'" + poiid1 + "' ,'" + start_time + "' ,'" + spell + "' ,'" + station_id + "' ,'" + end_time + "' ,'" + xy_coords + "');"
                        try:
                            conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                                    port="5432");
                            cur = conn.cursor();
                            cur.execute(station_sql);
                            conn.commit();
                        except Exception as e:
                            print(e);
                            cur.close();
                            conn.close();
                        line_station_rel_sql = "INSERT INTO gaode_line_station (busline_id, station_id, station_num) VALUES ('" + bus_lineid + "','" + station_id + "', " + station_num + ");"
                        try:
                            conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                                    port="5432");
                            cur = conn.cursor();
                            cur.execute(line_station_rel_sql);
                            conn.commit();
                        except Exception as e:
                            print(e);
                            cur.close();
                            conn.close();
                cur.close();
                conn.close();

def getBuslineNanes():
    conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost", port="5432");
    cur = conn.cursor();
    sql = "SELECT array_to_string(ARRAY(SELECT DISTINCT UNNEST(string_to_array(array_to_string(array(SELECT replace(t.address,'(在建)', '') from gaode_poi t where t.typecode like '15050%'),';'),';',''))),';');";
    cur.execute(sql);
    busLineStr=cur.fetchall();
    lines = busLineStr[0][0].split(';');
    length = len(lines);
    print(length);
    print("--------------------------------------------------------------------------");
    cur.close();
    conn.close();
    length = len(lines);
    lineList=[];
    print(len(lines));
    for line in lines:
        if line in lineList:
            continue
        else:
            line="地铁"+line;
            lineList.append(line);
    return lineList;


def batchGetBusLineDate():
    lineList=getBuslineNanes();
    # lineList.reverse();
    # length=len(lineList);
    # print(length);
    # newLineList=[];
    # for num in range( round(length/8)*6, length):
    #     newLineList.append(lineList[num]);
    # # newLineList.reverse();
    NeedCount=0;
    lineList.reverse();
    for lineName in lineList:
        print(lineName);
        conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        sql = "select count(*) from gaode_subway t where t.key_name like '%"+lineName+"%'";
        cur.execute(sql);
        keyData = cur.fetchall();
        count = keyData[0][0];
        cur.close();
        conn.close();
        sleepTime = random.randint(20, 35);
        if count==0:
            getOneBusLineDate(lineName);
        else:
            sleepTime=0
        print(sleepTime);
        time.sleep(sleepTime);
        
        
    print(NeedCount);
batchGetBusLineDate();
# getOneBusLineDate("173路(内环)");

