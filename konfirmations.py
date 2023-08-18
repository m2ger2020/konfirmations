#!/bin/python
from tkinter import messagebox
import random
from time import sleep
import argparse 
import sys

path_to_config="konfirmations.ini"
faili_asukoht=""
argparser=argparse.ArgumentParser()
argparser.add_argument("-v","--version",help="kuvab versiooniinfo",action="store_true")
argparser.add_argument("-c","--config_file",help="kasutaja isiklik konfiguratsioonifail")
argparser.add_argument("-f","--file",help="kasutaja isiklik kinnituste fail")
args=argparser.parse_args()
if args.version:
    print("""konfirmations.py 0.02\nauthor: minu peakene\nReleased under the GNU General Public License""")
    sys.exit()

if args.config_file:
    print("Kasutan konfiguratsioonifaili % s" % (prguneV22rtus))
    path_to_config=prguneV22rtus.strip()
if args.file:
    print("Kasutan tekstifaili % s" % (prguneV22rtus))
    faili_asukoht=prguneV22rtus



### s2tete sisselugemine
config=configparser.ConfigParser()
config.read(path_to_config)
if faili_asukoht=="":
    faili_asukoht=config['USER']['MessageFile']
P=float(config['USER']['MessageProbability'])
intervall=float(config['USER']['MessageInterval'])

fail=open(faili_asukoht,'r')
kinnitused=fail.readlines()

print("The Konfirmation is Coming.")
while True:
    p=random.random()
    if p<=P:
        s6num=kinnitused[random.randint(0,len(kinnitused)-1)]
        aken=messagebox.showwarning("Konfirmation",s6num)
    sleep(intervall)
