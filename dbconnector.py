#!/usr/bin/python3
import pymysql

class RemoteDB:
    db = None
    cur = None

    def __init__(self, host, port, user, password, database) -> None:
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        self.cur = self.db.cursor()

    def __del__(self):
        self.db.close()

    def exist(self, ipv4add):
        _1 = ipv4add.split('.')[0]
        _2 = ipv4add.split('.')[1]
        _3 = ipv4add.split('.')[2]
        sql = "SELECT _1,_2,_3 FROM ipv4 WHERE _1=%s AND _2=%s AND _3=%s"
        self.cur.execute(sql, (_1, _2, _3))
        results = self.cur.fetchall()
        if len(results):
            return True
        else:
            return False

    def new(self, response):
        try:
            for q in response:
                if q["status"] == "success":      
                    _1 = q["query"].split('.')[0]
                    _2 = q["query"].split('.')[1]
                    _3 = q["query"].split('.')[2]
                    countryCode = q["countryCode"]
                    region = q["regionName"]
                    city = q["city"]
                    lat = q["lat"]
                    lon = q["lon"]
                    isp = q["isp"]
                    org = q["org"]
                    _as = q["as"]
                    asname = q["asname"]
                    if q["mobile"] == True:
                        mobile = '1'
                    else:
                        mobile = '0'
                    if q["hosting"] == True:
                        hosting = '1'
                    else:
                        hosting = '0'
                    sql = "INSERT INTO ipv4(`_1`,`_2`,`_3`,`countryCode`,`region`,`city`,`lat`,`lon`,`isp`,`org`,`as`,`asname`,`mobile`,`hosting`) \
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    self.cur.execute(sql, (_1, _2, _3, countryCode, region, city, lat, lon, isp, org, _as, asname, mobile, hosting))
            self.db.commit()
        except:
            self.db.rollback()