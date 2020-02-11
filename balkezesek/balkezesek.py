import codecs
import time

class BalKezes():
    def __init__(self, name, fromdt, todt, weight, height):
        self.name = name
        self.fromdt = time.strptime(fromdt, "%Y-%m-%d")
        self.todt = time.strptime(todt, "%Y-%m-%d")
        self.weightkg = int(weight)/2.2046
        self.weightpnd = int(weight)
        self.heightcm = int(height)*2.54
        self.heightinch = int(height)

balkezesek = []


f = codecs.open("balkezesek.csv", "r", encoding="iso8859_2").read()

f1format = time.strptime("1999-10-01","%Y-%m-%d")
f2format = time.strptime("1999-10-31","%Y-%m-%d")

for i in range(1, len(f.split("\r\n"))):
    x = f.split("\r\n")[i]
    data = []
    for p in x.split(";"):
        data += [p]
    balkezesek += [BalKezes(data[0], data[1], data[2], data[3], data[4])]

print("3. feladat", str(len(balkezesek)), "Rekord az állományban.")
print("4. feladat")

for x in balkezesek:
    if x.todt >= f1format and x.todt <= f2format:
        print("    ", x.name, str(x.heightcm).replace(".",","), "cm")


print("Kérek egy 1990 és 1999 közötti évszámot! : ")
indate = input()
while indate.isnumeric() != True or int(indate) < 1990 or int(indate) >1999:
    print("Hibás adat, kérek egy 1990 és 1999 közötti évszámot!: ")
    indate = input()

fromi = time.strptime(indate+"-01-01", "%Y-%m-%d")
toi = time.strptime(indate+"-12-31", "%Y-%m-%d")
num = 0
avgc = 0
for x in balkezesek:
    if x.fromdt >= fromi and x.fromdt <= toi:
        num += 1
        avgc += x.weightpnd

print("6. feladat: " + str(round(avgc/num, 2)), "font")
        