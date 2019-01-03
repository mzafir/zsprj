
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
    for j in range(1000000000):
        for i in range(s):
            time.sleep(2)
            u = urlopen(fdqn + plugins[i])
            data = json.load(u)
            result.append(data)

    file.write(json.dumps(result))
    file.close()

t_end = time.time() + 21000
while time.time() < t_end:
 cpugetter()

