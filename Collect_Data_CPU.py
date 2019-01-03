#Author Asim Zafir
#Zscaler Project

import csv
import re
from urllib.request import urlopen
import json
import time



def cpugetter():

    file = open("cpu_data.json", "w")
    fdqn = 'http://34.239.233.186:61208/api/3/'
    plugins = ["cpu"]
    s = len(plugins)
    result=[]
    for j in range(100000):
        for i in range(s):
            u = urlopen(fdqn + plugins[i])
            data = json.load(u)
            result.append(data)
    file.write(json.dumps(result))
    file.close()


cpugetter()

