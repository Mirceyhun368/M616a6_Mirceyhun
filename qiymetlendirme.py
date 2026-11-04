parts = input().split()
values = []
missing = 0
for p in parts :
    if p =="NA":
        missing += 1
    else :
        values.append(float(p))

print("Ölçmə:",len(values))
print("Boş",missing)

if len(values) > 0:
    print("Min:", min(values))
    print("Max:", max(values))
    orta = sum(values)/len(values)
    print("Orta qiymət:",round(orta,1))

counts = {"zəif":0,"orta":0,"yaxşı":0}

for v in values :
    if v >= - 93 :
     status = "yaxşı"
    elif v>= -100 :
     status = "orta"
    else :
     status = "zəif" 

    print(f"{v}-> {status}")
    counts[status] += 1

    
print(counts)

Zəif_payı = (counts["zəif"]/len(values))*100
print(f"Zəif payı:{round(Zəif_payı,1)}%")



print("Qərar: müşahidədə saxla")

max_zəif_seriya = 0
current_seriya = 0
for v in values :
   if v < -105:
      current_seriya +=1
   if current_seriya > max_zəif_seriya:
      max_zəif_seriya = current_seriya
   else :
      current_seriya = 0

print("Ən uzun zəif seriya:",max_zəif_seriya)
