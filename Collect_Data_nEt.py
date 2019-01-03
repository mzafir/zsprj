
import csv
import re
from urllib.request import urlopen
import json
import time

def network_getter():

    file = open("net_data.json", "w")
    fdqn = 'http://34.239.233.186:61208/api/3/'
    plugins = ["network"]
    s = len(plugins)
    result =[]
    for j in range(1000000000000):
        for i in range(s):
            u = urlopen(fdqn + plugins[i])
           # print(type(u))
            data=json.load(u)#.read().decode('utf-8'))
            result.append(data[1])
            data=json.dumps(data)
    file.write(json.dumps(result))
    file.close()

network_getter()


