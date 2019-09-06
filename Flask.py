#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from bokeh.embed import components
from bokeh.plotting import figure
from flask import Flask, render_template
from sense_hat import SenseHat
from output import Output

app = Flask(__name__)
@app.route('/')

def index():
        str = ["寒い", "肌寒い", "何も感じない", "快い", "暑くない", "やや暑い", "暑くて汗が出る", "暑くてたまらない"]
        sense = SenseHat()
        tmp = sense.get_temperature()
        hum = sense.get_humidity()
        thi = 0.81 * tmp + hum * 0.01 * (0.99 * tmp - 14.3) + 46.3
        if thi < 55 :
                mes = str[0]
        elif thi >= 55 and thi < 60 :
                mes = str[1]
        elif thi >= 60 and thi < 65 :
                mes = str[2]
        elif thi >= 65 and thi < 70 :
                mes = str[3]
        elif thi >= 70 and thi < 75 :
                mes = str[4]
        elif thi >= 75 and thi < 80 :
                mes = str[5]
        elif thi >= 80 and thi < 85 :
                mes = str[6]
        elif thi >= 85 :
                mes = str[7]

        out = Output()
        out.sqlite_out()
        subtmp = out.get_tmp()
        subhum = out.get_hum()
        date = out.get_date()
        p = out.graph_draw()
        script, div = components(p)
        thi = format(thi, '.1f')
        tmp = format(tmp, '.1f')
        hum = format(hum, '.1f')
        subtmp = format(subtmp, '.1f')
        subhum = format(subhum, '.1f')
        return render_template('index.html', script=script, div=div, tmp=tmp, hum=hum, thi=thi, mes=mes, date=date, subtmp=subtmp, subhum=subhum)

app.run(host='0.0.0.0', debug=True)
