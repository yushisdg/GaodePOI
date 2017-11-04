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

MCBAND = [12890594.86, 8362377.87, 5591021, 3481989.83, 1678043.12, 0];
LLBAND = [75, 60, 45, 30, 15, 0];
MC2LL = [[1.410526172116255e-8, 898305509648872e-20, -1.9939833816331, 200.9824383106796, -187.2403703815547,
          91.6087516669843, -23.38765649603339, 2.57121317296198, -.03801003308653, 17337981.2],
         [-7.435856389565537e-9, 8983055097726239e-21, -.78625201886289, 96.32687599759846, -1.85204757529826,
          -59.36935905485877, 47.40033549296737, -16.50741931063887, 2.28786674699375, 10260144.86],
         [-3.030883460898826e-8, 898305509983578e-20, .30071316287616, 59.74293618442277, 7.357984074871,
          -25.38371002664745, 13.45380521110908, -3.29883767235584, .32710905363475, 6856817.37],
         [-1.981981304930552e-8, 8983055099779535e-21, .03278182852591, 40.31678527705744, .65659298677277,
          -4.44255534477492, .85341911805263, .12923347998204, -.04625736007561, 4482777.06],
         [3.09191371068437e-9, 8983055096812155e-21, 6995724062e-14, 23.10934304144901, -.00023663490511,
          -.6321817810242, -.00663494467273, .03430082397953, -.00466043876332, 2555164.4],
         [2.890871144776878e-9, 8983055095805407e-21, -3.068298e-8, 7.47137025468032, -353937994e-14, -.02145144861037,
          -1234426596e-14, .00010322952773, -323890364e-14, 826088.5]];
LL2MC = [[-.0015702102444, 111320.7020616939, 0x60e374c3105a3, -0x24bb4115e2e164, 0x5cc55543bb0ae8, -0x7ce070193f3784,
          0x5e7ca61ddf8150, -0x261a578d8b24d0, 0x665d60f3742ca, 82.5],
         [.0008277824516172526, 111320.7020463578, 647795574.6671607, -4082003173.641316, 10774905663.51142,
          -15171875531.51559, 12053065338.62167, -5124939663.577472, 913311935.9512032, 67.5],
         [.00337398766765, 111320.7020202162, 4481351.045890365, -23393751.19931662, 79682215.47186455,
          -115964993.2797253, 97236711.15602145, -43661946.33752821, 8477230.501135234, 52.5],
         [.00220636496208, 111320.7020209128, 51751.86112841131, 3796837.749470245, 992013.7397791013,
          -1221952.21711287,
          1340652.697009075, -620943.6990984312, 144416.9293806241, 37.5],
         [-.0003441963504368392, 111320.7020576856, 278.2353980772752, 2485758.690035394, 6070.750963243378,
          54821.18345352118, 9540.606633304236, -2710.55326746645, 1405.483844121726, 22.5],
         [-.0003218135878613132, 111320.7020701615, .00369383431289, 823725.6402795718, .46104986909093,
          2351.343141331292, 1.58060784298199, 8.77738589078284, .37238884252424, 7.45]]


def convertor(t, e):
    if t != None and e != None:
        lag = e[0] + e[1] * abs(t[0]);  # lng
        n = abs(t[1]) / e[9];  # lat
        lat = e[2] + e[3] * n + e[4] * n * n + e[5] * n * n * n + e[6] * n * n * n * n + e[7] * n * n * n * n * n + e[8] * n * n * n * n * n * n;
        k = 1;

        if (t[0] > 0):
            k = 1;
        else:
            k = -1;
        lag = lag * k;
        if (t[1] > 0):
            k = 1;
        else:
            k = -1;
        lat = lat * k;
        return [lag, lat]


def getBauduPoint(t):
    e = [abs(t[0]), abs(t[1])];
    order = 0;
    kt = [];
    for item in MCBAND:
        if e[1] > item:
            kt = MC2LL[order];
            break;
        order = order + 1;
    point = convertor(t, kt);
    return point;

def getBaidubusLine(uid):
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
    if content!=None:
        for item in content:
            print(item);
            company=item.get("company");
            endTime=item.get("endTime");
            geo=item.get("geo");
            polyline=geo[2:].replace('|', ';').split(";")[2].split(",");
            index=1;
            points=[];
            point = [0,0];
            for it in polyline:
                if index%2!=0:
                    point=[0,0];
                    point[0]=float(it);
                else:
                    point[1] = float(it);
                    points.append(point);
                index=index+1;
            geo1="";
            index=0;
            for point in points:
               point1=getBauduPoint(point);
               geo1=geo1+str(point1[0])+" "+str(point1[1]);
               index=index+1;
               if index!=len(points):
                   geo1=geo1+","
            geo=geo1
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
            conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
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
                    print(stationGeo[2:].replace('|',';').split(";")[0].split(','))
                    point=[float(stationGeo[2:].replace('|',';').split(";")[0].split(',')[0]),float(stationGeo[2:].replace('|',';').split(";")[0].split(',')[1])];
                    # print(point);
                    point1=getBauduPoint(point);
                    # print(point1);
                    stationGeo=str(point1[0])+" "+str(point1[1]);
                    # print(stationGeo);
                    stationName=station.get("name");
                    print(order);
                    stationSql="INSERT INTO baidu_station (uid, name, geo) VALUES ('"+stationUid+"','"+stationName+"','"+stationGeo+"');"
                    print(stationSql);
                    try:
                        conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                                port="5432");
                        cur = conn.cursor();
                        cur.execute(stationSql);
                        conn.commit();
                    except Exception as e:
                        print(e);
                        cur.close();
                        conn.close();
                    station_num=order;
                    station_num = str(order);
                    line_station_rel_sql = "INSERT INTO baidu_line_station (line_uid, station_uid, station_num) VALUES ('" + uid + "','" + stationUid + "', " + station_num + ");"
                    print(line_station_rel_sql);
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
    else:
        try:
            conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                    port="5432");
            cur = conn.cursor();
            sql="INSERT INTO baidu_nodate_busline (uid) VALUES ('"+uid+"');"
            cur.execute(sql);
            conn.commit();
        except Exception as e:
            print(e);
            cur.close();
            conn.close();



def batchGetBaiduBusLine():
    a = 1;
    while a == 1:
        sql = "select uid from baidu_busline where uid not in (select uid from baidu_busline_detail) and uid not in (select uid from baidu_nodate_busline) limit 1;";
        conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        cur.execute(sql);
        keyData = cur.fetchall();
        uid = keyData[0][0];
        getBaidubusLine(uid);
        sleepTime=random.randint(20, 30);
        print(sleepTime);
        time.sleep(sleepTime);

batchGetBaiduBusLine();


