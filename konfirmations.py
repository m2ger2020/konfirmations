#!/bin/python
from tkinter import messagebox
import random
from time import sleep
import argparse 
import sys
import configparser

###m6ned vaikev22rtused ;)
path_to_config="konfirmations.ini"
faili_asukoht=""

###argumentide sisselugemine k2surealt O_o
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

### s2tete sisselugemine konf-failist ;]
config=configparser.ConfigParser()
config.read(path_to_config)
if faili_asukoht=="":
    faili_asukoht=config['USER']['MessageFile']
P=float(config['USER']['MessageProbability'])
intervall=float(config['USER']['MessageInterval'])

###kinnituste sisselugemine vastavast failist >_o
fail=open(faili_asukoht,'r')
kinnitused=fail.readlines()

###vahva s6num! ;O
print("The Konfirmation is Coming.")

###t88tsykkel ^_^
while True:
    p=random.random()
    if p<=P:
        s6num=kinnitused[random.randint(0,len(kinnitused)-1)]
        aken=messagebox.showwarning("Konfirmation",s6num)
    sleep(intervall)
    #yay! :D:D:D
