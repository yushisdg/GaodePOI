import requests
import json
import time
from pandas import DataFrame
import psycopg2
import math
import random




def getBuiduLine(lineName):
    # hangzhou 179  xiamen194
    busLineUrl = "http://map.baidu.com/?qt=s&wd="+lineName+"&c=194";
    res = requests.get(url=busLineUrl).content;
    print(busLineUrl);
    total_json = json.loads(res);
    print(total_json);
    content = total_json.get("content");
    if content!=None:
        print("!None");
        length = int(len(content));
        for item in content:
            if item.get("blinfo")==None:
                uid = item.get("uid");
                addr = lineName;
                if uid != None and addr != None:
                    conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost",
                                            port="5432");
                    cur = conn.cursor();
                    sql = "INSERT INTO baidu_busline_xiamen(uid, addr) VALUES ('" + uid + "', '" + addr + "');"
                    try:
                        cur.execute(sql);
                        conn.commit();
                        cur.close();
                        conn.close();
                    except Exception as e:
                        print(e);
                        cur.close();
                        conn.close();
            else:
                busLineList = item.get("blinfo");
                if busLineList!=None:
                    for line in busLineList:
                        print(line);
                        if line!=None:
                            uid = line.get("uid");
                            addr = line.get("addr");
                            print(uid + "  " + addr);
                            if uid!=None and  addr!=None:
                                conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost",
                                                        port="5432");
                                cur = conn.cursor();
                                sql = "INSERT INTO baidu_busline_xiamen(uid, addr) VALUES ('" + uid + "', '" + addr + "');"
                                try:
                                    cur.execute(sql);
                                    conn.commit();
                                    cur.close();
                                    conn.close();
                                    conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456",
                                                            host="localhost", port="5432");
                                    cur = conn.cursor();
                                    sql = "INSERT INTO baidu_busline_disable_xiamen(name) VALUES ('" + lineName + "');"
                                    cur.execute(sql);
                                    conn.commit();
                                    cur.close();
                                    conn.close();
                                except Exception as e:
                                    print(e);
                                    cur.close();
                                    conn.close();
    else:
        print("--------------------");
        conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost",port="5432");
        cur = conn.cursor();
        sql="INSERT INTO baidu_busline_disable_xiamen(name) VALUES ('"+lineName+"');"
        cur.execute(sql);
        conn.commit();
        cur.close();
        conn.close();



def batchGetBaiduBusLine():
    lineList=getBuslineNanes();
    for lineName in lineList:
        conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost",
                                port="5432");
        cur = conn.cursor();
        cur.execute("select count(*) from baidu_busline_xiamen t where t.addr='"+lineName+"'");
        keyData = cur.fetchall();
        if keyData[0][0] == 0:
            cur.execute("SELECT count(*) from baidu_busline_disable_xiamen t where  t.name='" + lineName + "'");
            keyData1 = cur.fetchall();
            cur.close();
            conn.close();
            if keyData1[0][0] == 0:
                getBuiduLine(lineName);
                sleepTime = random.randint(20, 30);
                print(sleepTime);
                time.sleep(sleepTime);



def getBuslineNanes():
    conn = psycopg2.connect(database="mydatabase", user="postgres", password="123456", host="localhost", port="5432");
    cur = conn.cursor();
    sql = "SELECT array_to_string(ARRAY(SELECT DISTINCT UNNEST(array(SELECT t.address from gaode_poi_xiamen t)) ORDER BY 1),';');";
    cur.execute(sql);
    busLineStr=cur.fetchall();
    cur.close();
    conn.close();
    print(busLineStr[0][0]);
    lines=busLineStr[0][0].split(';');
    lineList=[];
    print(len(lines));
    for line in lines:
        if line in lineList:
            continue
        else:
            lineList.append(line);
    return lineList;

def check_json_format(raw_msg):
    """
    用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    """
    if isinstance(raw_msg, str):       # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False



batchGetBaiduBusLine();