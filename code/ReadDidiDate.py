import requests
import json
import time
from pandas import DataFrame
import psycopg2
import math
import random

file_object = open('G:/滴滴数据/dongweixu@zjut.edu.cn_20161101/gps_20161101')
try:
  for line in file_object:
    print(line, end = '')
    data=line.split(',');
    sql = "INSERT INTO didi_track_data (track_id, order_id, time, x, y) VALUES ('"+data[0]+"', '"+data[1]+"', '"+data[2]+"', "+data[3]+", "+data[4]+");"
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
finally:
  file_object.close()