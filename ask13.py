from urllib.request import Request, urlopen
import json

#περνω δεδομενα και τα τοποθετω στην λιστα
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data = data.decode()
json_acceptable_string = data.replace("'", "\"")
d = json.loads(json_acceptable_string)
random = d["randomness"]
list = []
for i in range(0,len(random),2):
    temp = str(random[i])+str(random[i+1])
    list.append(temp)

#μετατρεπω αριθμους στην λιστα στην 10 μορφη
for i in range(len(list)):
    list[i] = int(list[i],16)

#βρισκω modul 80
for i in range(len(list)):
    list[i] = list[i]-80*int(list[i]/80)

#ελεγχω το καθε αντικειμενο να ειναι μονο 1 φορα στην λιστα
listtotal = []
listtotal.append(list[0])
for i in list:
    if i not in listtotal:
        listtotal.append(i)

#περνω λιστα νικητων και ελεγχω ποσα νουμερα νικησαν  
req = Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data = data.decode()
json_acceptable_string = data.replace("'", "\"")
d = json.loads(json_acceptable_string)
winners = d["last"]["winningNumbers"]["list"]
num = 0

for i in winners:
    if i in listtotal:
        num += 1

print ("From numbers: ",winners)
print (num," would win")

