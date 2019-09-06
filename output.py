#! /usr/bin/env python3
# _*_ coding: utf-8 _*_


import sqlite3
import datetime
from bokeh.plotting import figure, output_file, show

class Output:
        y1 = []
        y2 = []
        x = []

        def sqlite_out(self):
                dbname = '/home/pi/code/temp.db'
                con = sqlite3.connect(dbname)
                cur = con.cursor()

                cur.execute('SELECT tmp FROM temp order by date desc limit 61')
                self.y1 = ([(y1[0]) for y1 in cur.fetchall()])
                cur.execute('SELECT hum FROM temp order by date desc limit 61')
                self.y2 = ([(y2[0]) for y2 in cur.fetchall()])
                cur.execute('SELECT date FROM temp order by date desc limit 61')
                self.x = ([(x[0]) for x in cur.fetchall()])
                self.tmp = self.y1[0] - self.y1[60]
                self.hum = self.y2[0] - self.y2[60]
                self.date = self.x[60]

                con.close()
        """
        def sqlite_out_hour(self):
                dbname = '/home/pi/code/temp.db'
                con = sqlite3.connect(dbname)
                cur = con.cursor()

                for row1 in cur.execute('SELECT tmp FROM hourtemp order by date desc limit 1'):
                        self.tmp = row1[0]
                for row2 in cur.execute('SELECT hum FROM hourtemp order by date desc limit 1'):
                        self.hum = row2[0]
                for row3 in cur.execute('SELECT date FROM hourtemp order by date desc limit 1'):
                        self.date = row3[0]

                con.close()
        """
        def get_tmp(self):
                te = self.tmp
                return te

        def get_hum(self):
                hu = self.hum
                return hu

        def get_date(self):
                da = self.date
                return da

        def graph_draw(self):
                x = self.x[::-1]
                y1 = self.y1[::-1]
                y2 = self.y2[::-1]

                #output_file("/home/pi/code/templates/lines.html")

                p = figure(title="temp data", plot_width=1200, plot_height=500, x_axis_label='日時', y_axis_label='温度,湿度', x_range=x)
                p.y_range.start = 0
                p.xaxis.major_label_orientation = 1

                p.line(x, y1, line_width=5, legend="temp", color="limegreen")
                p.line(x, y2, line_width=5, legend="hum", color="blue")
                return p
