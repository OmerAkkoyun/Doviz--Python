encoding="utf-8"
import requests
import json
import time
print("""
----------------
DÖVİZ UYGULAMASI
----------------
ABD DOLARI  için :USD
EURO        için :EUR
TÜRK LİRASI için :TRY
----------------
""")

paraadi=input("Para Birinizin Adı :")
miktar=float(input("Miktar :"))
cevir=input("Çevirilecek Para Birimi :")
print("Güncel Değerler Kontrol ediliyor..")
time.sleep(2)
print("Hesaplanıyor...")
time.sleep(1)

url="https://api.fixer.io/latest?base="
getir=requests.get(url+paraadi)
json_et=getir.json()
print("Sonuç =  ",(json_et["rates"][cevir])*miktar,cevir)






