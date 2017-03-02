# -*- coding: utf-8 -*-
# importiert das os modul
# importiert das os shutil
import os
import shutil
import os.path
import glob
import time
import frogress
import collections
from os.path import join, splitext
from glob import glob
from collections import Counter

#Bildschirm sauber machen
os.system('clear')
#In diesem verzeichnis liege und arbeite ich (das script), hier sind alle zu ordnenden Dateien und hier werde
#ich auch die Ordner A - A-Z Anlegen
wd = os.path.dirname(os.path.abspath(__file__))
# nun mache ich mir eine Liste mit Buschtaben auch Buchstaben sind Nummern ;) 65 = A und Z ist 91
ALPHA = list(map(chr, range(65, 91)))
# ich weiss wo ich liege und habe mir das unter der variable "(wd)" gemerkt , wenn ich das in einem text anzeigen
# will muss ich das im text kenntlich machen mit ""%s"(string), am ende des textes gebe ich mir den Hinweiß was
# ich damit meine  % (wd)
print "in diesem Verzeichnis werde ich Aufräumen  %s\n" % (wd)
# Jier werden die Dateien gezählt
c = Counter([splitext(i)[1][1:] for i in glob(join(wd, '*'))])
#endngen wird zum array (Liste)
endungen = []
for ext, count in c.most_common():
     if ext != "":
        # zur Liste der Endungen wird jede ermittelte endung dieser durchläufe hinzugefügt
        endungen.append(ext)
        print "%s\t%s" % (ext,count)
print "\n"
#setzt das Suchverzeichnis gleich dem Ausführunsverzeichnis des Scriptes
hiermachen = os.path.dirname(os.path.abspath(__file__))
# Schleife die sicherstellt das die nutzereingabe richtig gemacht wird , verglichen wird mit den array der ermittelten
# endungen
while True:
    try:
        endung = raw_input("Welche Endung haben die Dateien (\".gewünschte Endung\") zum Abbrechen x : ")
        if endung in endungen:
            print "Weiter geht es"
            endung ="."+endung
            break
        elif endung.lower() == "x" :
             print "Aufwiedersehen\n"
             exit()
        else:
            print "Bitte Eingabe richtig machen "
    except ValueError:
        print "Bitte richtige Eingabe"
#hier  beginntder Prozess der einzelnen Ordner
path = wd+'/%s'
for Buchstabe in ALPHA:
    if not os.path.exists(path % Buchstabe):
        os.makedirs(path % Buchstabe)
# Listet alle Dateien im Suchverzeichnis auf  mit mit der Endung txt
for file in frogress.bar(os.listdir(hiermachen)):
    # wenn der Dateiname (wenn groß dann automatisch klein ".lower()" endet mit *.bin
    # und der erste Buchtabe (Groß zum vergleich mit Alpha) file[0].upper() in ALPHA vorkommt
    if file.lower().endswith(endung.lower()) and file[0].upper() in ALPHA :
        # zum einsparen einer Schleife nehme den 1.Buschtaben der Datei in Groß um das zielverzeichniss zu finden
        #datei = open("datenbank.csv", "a")
        with open("datenbank.csv", "a") as datei:
            logdatei = open("copy.log", "a")
            Buchstabe = file[0].upper()
            sourcefile = os.path.join(hiermachen, file)
            destinationfile = os.path.join(path % Buchstabe, file)
            #Debug Ausgabe print"%s ==> %s" % (file,destinationfile)
            shutil.move (sourcefile,destinationfile)
            datei.write("\t%s,\t%s\n" % (file,destinationfile) )
            logdatei.write("%s nach %s verschoben\n" % (file,destinationfile) )
            logdatei.close()

exit()
