
import csv
import re
from urllib.request import urlopen
import json
import time



def memgetter():

    file=open("workfile_mem_3", "w")
    fdqn='http://34.239.233.186:61208/api/3/'
    plugins=["mem"]
    s=len(plugins)
    result=[]
    for j in range(10):
     for i in range(s):
       time.sleep(2)
       u=urlopen(fdqn+plugins[i])
       data=json.load(u)
       result.append(data)

    file.write(json.dumps(result))
    file.close()


def cpugetter():

    file = open("workfile_cpu_2", "w")
    fdqn = 'http://34.239.233.186:61208/api/3/'
    plugins = ["cpu"]
    s = len(plugins)
    result=[]
    for j in range(5):
        for i in range(s):
            time.sleep(2)
            u = urlopen(fdqn + plugins[i])
            data = json.load(u)
            result.append(data)

    file.write(json.dumps(result))
    file.close()

def network_getter():

    file = open("net_data.json", "w")
    fdqn = 'http://34.239.233.186:61208/api/3/'
    plugins = ["network"]
    s = len(plugins)
    result =[]
    for j in range(10):
        for i in range(s):
            time.sleep(5)
            u = urlopen(fdqn + plugins[i])
           # print(type(u))
            data=json.load(u)#.read().decode('utf-8'))
            result.append(data[1])
            #data = u.read()
           # print(type(data))
            data=json.dumps(data)
           # print(data)
            """pat1=re.compile("^b\'\[")
            show=pat1.match(data)
            print(show)
            pat2=re.compile("\]")
            show2=pat2.match(data)
            print(show2)
"""
           # data=data.replace("\]\'b\'\[","")
           # print(data)
           # data=data.replace("^b\'\[\{","{")
          #  print(data)
            #result.append(data[1])
            #file.write(data)
    file.write(json.dumps(result))
    file.close()
def cleanup():
    file = open("workfile_network", "r")
    file1 = open("w_clean", "w")
    for item in file:
        item1=str(item)
        """item1=str(item)
        item1=item1.replace("\[\]", ",")
        item1 = item1.replace("\'", "")
       """
        pat1=re.compile("\]\[")
        show1=pat1.match(item1)
        print(show1)
#        file1.write(item1)
    file.close()

t_end = time.time() + 21000
while time.time() < t_end:
 network_getter()


