#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pymsteams
from sense_hat import SenseHat
sense = SenseHat()

message_teams = pymsteams.connectorcard("")
tmp = sense.get_temperature()
hum = sense.get_humidity()
thi = 0.81 * tmp  + 0.01 * hum * (0.99 * tmp - 14.3) + 46.3

if thi <= 55 :
        message = "とても寒いです  温度:" + format(tmp, '.1f') + "℃  湿度:"+ format(hum, '.1f') + "%"
        message_teams.title("raspberry-pi message")
        message_teams.text(message)
        message_teams.send()

elif thi > 55 and thi <= 60:
        message = "肌寒いです  温度:" + format(tmp, '.1f') + "℃  湿度:" + format(hum, '.1f') + "%"
        message_teams.title("raspberry-pi message")
        message_teams.text(message)
        message_teams.send()

elif thi >= 75.0 and thi < 80.0:
        message = "すこし暑いです  温度:" + format(tmp, '.1f') + "℃  湿度:" + format(hum, '.1f') + "%"
        message_teams.title("raspberry-pi message")
        message_teams.text(message)
        message_teams.send()

elif thi >= 80 and thi < 85:
        message = "とても暑いです  温度:" + format(tmp, '.1f') + "℃  湿度:" + format(hum, '.1f') +  "%"
        message_teams.title("raspberry-pi message")
        message_teams.text(message)
        message_teams.send()

elif thi >= 85 :
        message = "ものすごく暑いです  温度:" + format(tmp, '.1f') + "℃  湿度:" + format(hum, '.1f') +  "%"
        message_teams.title("raspberry-pi message")
        message_teams.text(message)
        message_teams.send()
