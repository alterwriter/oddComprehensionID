#Original by Ananda Fikri - clone writer
#don't copy it without permission if you are not buying me a starbucks or nasi padang

numIn = []
ganjil = []
try:
    while 999 not in numIn:
        numIn.append(int(input('Masukkan angka : ')))
    numIn.pop(len(numIn)-1)

except ValueError:
    print("invalid value")
    numIn


for x in numIn:
    if x % 2 == 1:
        ganjil.append(x)

print("="*20)
print('anda memasukkan sebanyak ' + str(len(numIn)) + " angka")
print("jumlah bilangan ganjil adalah: %s" % str(sum(ganjil)))