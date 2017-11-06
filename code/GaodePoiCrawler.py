import requests
import json
import time
from pandas import DataFrame
import psycopg2
import math


pages=1;

def getGaodePOI(key,rectangle,type,page,offset):
    poiUrl="http://restapi.amap.com/v3/place/polygon?polygon="+rectangle+"&types="+type+"&output=json&key="+key+"&page="+page+"&offset="+offset+"&extensions=all"
    print(poiUrl);
    res = requests.get(url=poiUrl).content;
    afterRequest(key);
    total_json = json.loads(res);
    print(total_json);
    insert_list = [];
    count=total_json.get('count');
    poisJson=total_json.get('pois');
    totalSql="";
    print(poisJson);
    poiCount=len(poisJson);
    if poiCount>0:
        if any(poisJson):
            i=0;
            for poi in poisJson:
                i=i+1;
                print(poi);
                id=poi.get('id');
                tag=json.dumps(poi.get('tag'));
                name=poi.get('name');
                type=poi.get('type');
                typecode=json.dumps(poi.get('typecode'));
                biz_type=json.dumps(poi.get('biz_type'));
                address=poi.get('address');
                if isinstance(address,str):
                    print(1);
                else:
                    address=json.dumps(address);
                location=poi.get('location');
                distance=json.dumps(poi.get('distance'));
                tel=json.dumps(poi.get('tel'));
                postcode=json.dumps(poi.get('postcode'));
                website=json.dumps(poi.get('website'));
                email=json.dumps(poi.get('email'));
                pcode=json.dumps(poi.get('pcode'));
                pname=json.dumps(poi.get('pname'));
                citycode=json.dumps(poi.get('citycode'));
                cityname=json.dumps(poi.get('cityname'));
                adcode=json.dumps(poi.get('adcode'));
                adname=json.dumps(poi.get('adname'));
                entr_location=json.dumps(poi.get('entr_location'));
                exit_location=json.dumps(poi.get('exit_location'));
                navi_poiid=json.dumps(poi.get('navi_poiid'));
                gridcode=json.dumps(poi.get('gridcode'));
                alias=json.dumps(poi.get('alias'));
                temp_business_area=json.dumps(poi.get('business_area'));
                if isinstance(temp_business_area,str):
                    business_area=temp_business_area;
                else:
                    business_area=json.dumps(poi.get('business_area'));
                print(business_area);
                parking_type=poi.get('parking_type');  #None
                if parking_type==None:
                    parking_type="NULL"
                indoor_map=json.dumps(poi.get('indoor_map'));
                indoor_data=poi.get('indoor_data');
                cpid=json.dumps(indoor_data.get('cpid'));
                floor=json.dumps(indoor_data.get('floor'));
                truefloor=json.dumps(indoor_data.get('truefloor'));
                groupbuy_num=json.dumps(poi.get('groupbuy_num'));
                discount_num=json.dumps(poi.get('discount_num'));
                biz_ext = poi.get('biz_ext');
                rating=json.dumps(biz_ext.get('rating'));
                cost=json.dumps(biz_ext.get('cost'));
                meal_ordering=biz_ext.get('meal_ordering');   #None
                meal_ordering="meal_ordering";
                seat_ordering=biz_ext.get('seat_ordering');    #None
                seat_ordering="seat_ordering";
                ticket_ordering=biz_ext.get('ticket_ordering'); #None
                ticket_ordering="ticket_ordering";
                hotel_ordering=biz_ext.get('hotel_ordering');  #None
                hotel_ordering="hotel_ordering";
                photos = json.dumps(poi.get('photos'));
                sql = "INSERT INTO gaode_poi (id, tag, name, type, typecode, biz_type, address, location, distance, tel, postcode, website, email, pcode, pname, citycode, cityname, adcode, adname, entr_location, exit_location, navi_poiid, gridcode, alias, business_area, parking_type, indoor_map, cpid, floor, truefloor, groupbuy_num, discount_num, rating, cost, meal_ordering, seat_ordering, ticket_ordering, hotel_ordering, photos) VALUES ('" + id + "','" + tag + "','" + name + "','" + type + "','" + typecode + "','" + biz_type + "','" + address + "','" + location + "','" + distance + "','" + tel + "','" + postcode + "','" + website + "','" + email + "','" + pcode + "','" + pname + "','" + citycode + "','" + cityname + "','" + adcode + "','" + adname + "','" + entr_location + "','" + exit_location + "','" + navi_poiid + "','" + gridcode + "','" + alias + "','" + business_area + "','" + parking_type + "','" + indoor_map + "','" + cpid + "','" + floor + "','" + truefloor + "','" + groupbuy_num + "','" + discount_num + "','" + rating + "','" + cost + "','" + meal_ordering + "','" + seat_ordering + "','" + ticket_ordering + "','" + hotel_ordering + "','" + photos+"');";
                print(sql);
                conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost",
                                        port="5432");
                cur = conn.cursor();
                try:
                    cur.execute(sql);
                except Exception as e:
                    print(e);
                conn.commit();
                cur.close();
                conn.close();
            pages = math.ceil(int(count) / int(offset));
            return pages;
    else:
        return 0;


type=str(150700);
page=str(1);
offset="50";
def getOneRectangleAllPoi(key,rectangle,type,page,offset):
    pages = getGaodePOI(key, rectangle, type, page, offset);
    if pages > 1:
        for num in range(2, pages + 1):
            getGaodePOI(key, rectangle, type, str(num), offset)
    return None;


# 获取研究区域网格
def getRegionRectangles():
    conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost", port="5432");
    cur = conn.cursor();
    cur.execute("select t.__xmin||','||t.ymin||';'||t.__xmax||','||t.ymax rectangle from hangzhou_grid t");
    rectangleData = cur.fetchall();
    cur.close();
    conn.close();
    return rectangleData;


def getUseableKey():
    currentDate = time.strftime("%Y-%m-%d", time.localtime());
    conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost", port="5432");
    cur = conn.cursor();
    cur.execute("select KJ.key from (SELECT k.key, COALESCE((select j.poi_reqcount from gaode_keys j where j.date='" + currentDate + "' and j.key=k.key),0) poi_reqcount from (SELECT t.key from gaode_keys t GROUP BY t.key)  K) KJ  where KJ.poi_reqcount<1000");
    keyData = cur.fetchall();
    key=keyData[0][0];
    cur.close;
    conn.close();
    if key==None:
        print("没有可用key了，需要申请更多的账户");
    return key;

#批量请求研究区域内的一类POI
def batchGetGaodePoi(type):
    page = str(1);
    offset = "50";
    rectangleData=getRegionRectangles();
    for rec in rectangleData:
        print(rec[0]);
        key=getUseableKey();
        if key==None:
            print("没有可用key了，需要申请更多的账户");
        else:
            getOneRectangleAllPoi(key, rec[0], type,page,offset);
        print("一个区域的数据已获取完成");


#请求完成后 key计数+1
def afterRequest(key):
    currentDate = time.strftime("%Y-%m-%d", time.localtime());
    conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost", port="5432");
    cur = conn.cursor();
    cur.execute("SELECT count(*) from gaode_keys t where t.key='"+key+"' and t.date='"+currentDate+"'");
    keyData = cur.fetchall();
    if keyData[0][0]==0:
        cur.execute(" INSERT INTO gaode_keys (key, date, poi_reqcount) VALUES('"+key+"','"+currentDate+"'"+",1)");
    else:
        cur.execute("UPDATE gaode_keys t set poi_reqcount=t.poi_reqcount+1 where t.key='"+key+"' and t.date='"+currentDate+"'");
    conn.commit();
    cur.close;
    conn.close();
    print("key :"+key+" +1");


# key='a5e9cfffb5d9a00c14142cdc17742a8d';
# rectangle='120.12924,30.30185;120.16018,30.27150';
# type=str(150700);
# page=str(1);
# offset="50";
# pages=getGaodePOI(key,rectangle,type,page,offset);
# print(pages);
# if pages>1:
#     for num in range(2, pages+1):
#         getGaodePOI(key, rectangle, type, str(num), offset)

type=str(190301);
batchGetGaodePoi(type);