import urllib.request

def extrahieren(txt,von,bis):
    teile = txt.split(von)
    teile.pop(0)
    ergebnis = []
    for teil in teile:
        teil = teil.split(bis)[0]
        ergebnis.append(teil)
    return ergebnis

def sauber(txt):
    repls = ".,;:_!?\"'/()[]{}+<>*"
    for r in repls:
        txt=txt.replace(r," ")
    txt.replace("- "," ")

    while txt.count("  ") >0:
        txt = txt.replace("  "," ")
    return txt

def geturl(url):
    ws = urllib.request.urlopen(url)
    txt = ws.read().decode("utf-8")
    ws.close()
    return txt

def speichern(datei,txt):
    aus = open(datei, "w", encoding="utf-8")
    aus.write(txt)
    aus.close()

def sauberleer(txt):
    txt=txt.replace("\t"," ").replace("\n"," ")
    while txt.count("  "):
        txt = txt.replace("  "," ")
    return txt


api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""
