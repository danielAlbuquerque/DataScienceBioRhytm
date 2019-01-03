import datetime

from math import sin

def getBiorhythm(zd):
    pi = 3.14159
    zd = int(zd)
    physical = int(50 * (1 + sin((zd / 23.0 - (zd / 23)) * 360 * pi / 180)))
    emotion = int(50 * (1 + sin((zd / 28.0 - (zd / 28)) * 360 * pi / 180)))
    intellect = int(50 * (1 + sin((zd / 33.0 - (zd / 33)) * 360 * pi / 180)))
    return physical, emotion, intellect

def saveData():
    pass

bd = raw_input("Dt. Nascimento (formato = mm/dd/yyyy): ")

dL = bd.split("/")

birthday = datetime.date(int(dL[2]), int(dL[0]), int(dL[1]))

today = datetime.date.today()

age = (today - birthday).days
px, ex, ix = getBiorhythm(age)

saveData(px, ex, ix)

print "-"*58
print "BIORITMO:"
print "FISICO            :  %5d" % px
print "EMOCIONAL         :  %5d" % ex
print "INTELECTUAL       :  %5d" % ix
print "-"*58