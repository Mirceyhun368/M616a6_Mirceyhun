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




