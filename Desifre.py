"""
İçine girilen kelimeyi deşifre eden fonksiyon
"""


def desifre(kelime):
    harflerin_karsiliklari={"A":"!","B":"'","C":"^","Ç":"+","D":"%","E":"&","F":"/","G":"(","Ğ":")","H":"=","I":"*","I":"?","J":";","K":"-","L":"_","M":"|","N":"}","O":"]","Ö":"[","P":"{","R":"$","S":"é","Ş":"<","T":"@","U":"€","Ü":"æ","V":"¨","Y":"ß","Z":".","Q":",","W":"`","X":"<"}
    for i in kelime:
        if i != i.upper():
            i=i.upper()
        print(harflerin_karsiliklari[i],end="")
desifre("ömER")
