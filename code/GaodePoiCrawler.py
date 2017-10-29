import requests
import json
import time
from pandas import DataFrame
import psycopg2
import math


pages=1;

def getGaodePOI(key,rectangle,type,page,offset):
    poiUrl="http://restapi.amap.com/v3/place/polygon?polygon="+rectangle+"&types="+type+"&output=json&key="+key+"&page="+page+"&offset="+offset+"&extensions=all"
    res = requests.get(url=poiUrl).content;
    total_json = json.loads(res);
    print(total_json);
    insert_list = [];
    count=total_json.get('count');
    poisJson=total_json.get('pois');
    totalSql="";
    if any(poisJson):
        i=0;
        for poi in poisJson:
            i=i+1;
            print(poi);
            id=poi.get('id');
            tag=json.dumps(poi.get('tag'));
            name=poi.get('name');
            type=poi.get('type');
            typecode=poi.get('typecode');
            biz_type=json.dumps(poi.get('biz_type'));
            address=poi.get('address');
            location=poi.get('location');
            distance=json.dumps(poi.get('distance'));
            tel=json.dumps(poi.get('tel'));
            postcode=json.dumps(poi.get('postcode'));
            website=json.dumps(poi.get('website'));
            email=json.dumps(poi.get('email'));
            pcode=poi.get('pcode');
            pname=poi.get('pname');
            citycode=poi.get('citycode');
            cityname=poi.get('cityname');
            adcode=poi.get('adcode');
            adname=poi.get('adname');
            entr_location=json.dumps(poi.get('entr_location'));
            exit_location=json.dumps(poi.get('exit_location'));
            navi_poiid=json.dumps(poi.get('navi_poiid'));
            gridcode=poi.get('gridcode');
            alias=json.dumps(poi.get('alias'));
            temp_business_area=poi.get('business_area');
            if isinstance(temp_business_area,str):
                business_area=temp_business_area;
            else:
                business_area=json.dumps(poi.get('business_area'));
            print(business_area);
            parking_type=poi.get('parking_type');  #None
            if parking_type==None:
                parking_type="NULL"
            indoor_map=poi.get('indoor_map');
            indoor_data=poi.get('indoor_data');
            cpid=json.dumps(indoor_data.get('cpid'));
            floor=json.dumps(indoor_data.get('floor'));
            truefloor=json.dumps(indoor_data.get('truefloor'));
            groupbuy_num=poi.get('groupbuy_num');
            discount_num=poi.get('discount_num');
            biz_ext = poi.get('biz_ext');
            rating=json.dumps(biz_ext.get('rating'));
            cost=json.dumps(biz_ext.get('cost'));
            meal_ordering=biz_ext.get('meal_ordering');   #None
            if meal_ordering==None:
                meal_ordering="meal_ordering";
            seat_ordering=biz_ext.get('seat_ordering');    #None
            if seat_ordering==None:
                seat_ordering="seat_ordering";
            ticket_ordering=biz_ext.get('ticket_ordering'); #None
            if ticket_ordering==None:
                ticket_ordering="ticket_ordering";
            hotel_ordering=biz_ext.get('hotel_ordering');  #None
            if hotel_ordering==None:
                hotel_ordering="hotel_ordering";
            photos = json.dumps(poi.get('photos'));
            sql = "INSERT INTO gaode_poi (id, tag, name, type, typecode, biz_type, address, location, distance, tel, postcode, website, email, pcode, pname, citycode, cityname, adcode, adname, entr_location, exit_location, navi_poiid, gridcode, alias, business_area, parking_type, indoor_map, cpid, floor, truefloor, groupbuy_num, discount_num, rating, cost, meal_ordering, seat_ordering, ticket_ordering, hotel_ordering, photos) VALUES ('" + id + "','" + tag + "','" + name + "','" + type + "','" + typecode + "','" + biz_type + "','" + address + "','" + location + "','" + distance + "','" + tel + "','" + postcode + "','" + website + "','" + email + "','" + pcode + "','" + pname + "','" + citycode + "','" + cityname + "','" + adcode + "','" + adname + "','" + entr_location + "','" + exit_location + "','" + navi_poiid + "','" + gridcode + "','" + alias + "','" + business_area + "','" + parking_type + "','" + indoor_map + "','" + cpid + "','" + floor + "','" + truefloor + "','" + groupbuy_num + "','" + discount_num + "','" + rating + "','" + cost + "','" + meal_ordering + "','" + seat_ordering + "','" + ticket_ordering + "','" + hotel_ordering + "','" + photos+"');";
            totalSql=totalSql+sql;

            #print(id+" "+tag+" "+name +" "+type +" "+typecode +" "+biz_type +" "+address +" "+location +" "+distance +" "+tel +" "+postcode+" "+ website +" "+email +" "+pcode +" "+pname +" "+citycode +" "+cityname +" "+adcode +" "+adname +" "+entr_location +" "+exit_location +" "+navi_poiid +" "+gridcode +" "+alias +" "+business_area+" "+ parking_type +" "+indoor_map +" "+cpid +" "+floor +" "+truefloor +" "+groupbuy_num +" "+discount_num +" "+rating +" "+cost +" "+meal_ordering +" "+seat_ordering +" "+ticket_ordering +" "+hotel_ordering +" "+titile +" "+url );
            # print(id+" "+tag+" "+name +" "+type +" "+typecode +" "+biz_type +" "+address +" "+location +" "+distance +" "+tel +" "+postcode+" "
            #       + website + " " + email + " " + pcode + " " + pname + " " + citycode + " " + cityname + " " + adcode + " " + adname + " " + entr_location + " "
            #       + exit_location + " " + navi_poiid + " " + gridcode + " " + alias + " "
            #       + business_area + " "
            #       + indoor_map + " " + cpid + " "
            #       + floor + " " + truefloor + " " + groupbuy_num + " " + discount_num
            #       + " " + rating + " " + cost + " "
            #       +photos
            #       );


        print(page);
        print(totalSql);
        conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        try:
            cur.execute(totalSql);
        except Exception as e:
            print(e);
        conn.commit();
        cur.close();
        conn.close();
        pages = math.ceil(int(count) / int(offset));
        return pages;

key='a5e9cfffb5d9a00c14142cdc17742a8d';
rectangle='120.12924,30.30185;120.16018,30.27150';
type=str(150700);
page=str(1);
offset="50";
pages=getGaodePOI(key,rectangle,type,page,offset);
print(pages);
if pages>1:
    for num in range(2, pages+1):
        getGaodePOI(key, rectangle, type, str(num), offset)