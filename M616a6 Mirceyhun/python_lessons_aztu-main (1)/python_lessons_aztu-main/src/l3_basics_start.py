# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)
name=input()
print("Mənim adım",name)
age=int(input())
age=age+1
print("Mənim yaşım",age)



print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# TODO: cell, rsrp, drops

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# TODO: type(...) və «mətn ≠ ədəd»

print("=== Kərpic 4 ===")   # Müqayisə → True / False
# TODO: rsrp < -105, ==

print("=== Kərpic 5 ===")   # Siyahı (list)
# TODO: rsrp_list, indeks, len, orta

print("=== Kərpic 6 ===")   # Lüğət (dict)
row = {"cell_id": "BAK-0207", "region": "Yasamal", "rsrp_dbm": -108.1}
print(row["region"])
print(row["rsrp_dbm"])
print(row)
row["band"] = "LTE800"
row["region"]="Nesimi"
print(row)

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
for v in rsrp_list:
    v = v * int(input())
    print(v)


age = int(input())

if  age > 21 :
    print("yaşım 21dən böyükdür") 
else :
    print("yaşım 21dən kiçikdir")

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
