#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import sqlite3
import datetime
from sense_hat import SenseHat
sense = SenseHat()

def sqlite_in(tmp, hum):
        dbname = '/home/pi/code/temp.db'
        con = sqlite3.connect(dbname)
        cur = con.cursor()
        output_time = datetime.datetime.now()
        output_time = output_time.strftime('%Y-%m-%d %H:%M:%S')
        data = (tmp, hum, output_time)
        cur.execute('insert into temp (tmp, hum, date) values (?,?,?)', (data))
        con.commit()
        con.close()

tmp = sense.get_temperature()
hum = sense.get_humidity()
sqlite_in(tmp, hum)
