# -*- coding: utf-8 -*-
# importiert das os modul
# importiert das os shutil
import os
import shutil
import os.path
import glob
import collections
import string
import random
import subprocess
import time
import frogress

#Bildschirm sauber machen
os.system('clear')
program = raw_input("Was wollen Sie machen Dateien (e)rstellen oder (l)öschen : ")
#abfrage nach der Anzahl der zu erstellenden Dateien
if program.lower() == ('e'):
    anzahl = input ("Wieviiel files sollen erstellt werden :")
    #abfrage nach dem preafix der zu erstellenden Dateien
    endungen = raw_input ("Welche Endung soll die Datei haben :")
    #i ist nur eine variable für den itterator
    #for i in range(0, anzahl):
    for i in frogress.bar(range(0, anzahl)):
        ran = random.choice(string.ascii_letters)
        ran1 = random.choice(string.ascii_letters)
        subprocess.call("touch %s%s.%s" % (ran,ran1,endungen), shell=True)
        #open ('%s%s.txt' % (ran,ran1), 'a').close()
        #print ("touch %s%s.txt") % (ran,ran1)
elif program.lower() == ('l'):
    #erstellt eine liste von dateien und ordnern im derzeitigen verzeichnis und entfernt dateien mit .py sowie Ordner
    filelist  = [ f for f in os.listdir(".") if not f.endswith(".py") and not os.path.isdir (f)]
    for f in filelist:
        #print f
        #löscht dateien
        os.remove(f)
    # erstellt eine Liste der aktuell verzeichnisse im aktuellen Ordner
    subdirectories = [d for d in os.listdir(".") if os.path.isdir(d)]
    #d ist der itterator und geht die liste subdirectories ab
    for d in frogress.bar(subdirectories):
        #print d
        #löscht verzeichnisse die leer sind
        #os.rmdir(d)
        #löscht verzeichnisse die nicht leer sind
        shutil.rmtree(d)

time.sleep(1)
exit ()
