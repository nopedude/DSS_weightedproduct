import math

print("===SISTEM PENDUKUNG KEPUTUSAN UNTUK TRANSAKSI PEMBELIAN MOBIL===")
# INPUTSPEK
print(" ")
print("Masukkan spesifikasi mobil ke-1 :")
M1 = {
    'M1id': input('Masukkan merk mobil '),
    'M1C1': int(input('Berapa harga mobil yang ditawarkan? ')),
    'M1C2': int(input('Berapa jumlah penumpang maksimum? ')),
    'M1C3': int(input('Berapa jumlah konsumsi bahan bakar? ')),
    'M1C4': int(input('Berapa tenaga yang dihasilkan oleh mesin? '))
}

print('')
print("Masukkan spesifikasi mobil ke-2 :")
M2 = {
    'M2id': input('Masukkan merk mobil '),
    'M2C1': int(input('Berapa harga mobil yang ditawarkan? ')),
    'M2C2': int(input('Berapa jumlah penumpang maksimum? ')),
    'M2C3': int(input('Berapa jumlah konsumsi bahan bakar? ')),
    'M2C4': int(input('Berapa tenaga yang dihasilkan oleh mesin? '))
}
print('')

print("Masukkan spesifikasi mobil ke-3 :")
M3 = {
    'M3id': input('Masukkan merk mobil '),
    'M3C1': int(input('Berapa harga mobil yang ditawarkan? ')),
    'M3C2': int(input('Berapa jumlah penumpang maksimum? ')),
    'M3C3': int(input('Berapa jumlah konsumsi bahan bakar? ')),
    'M3C4': int(input('Berapa tenaga yang dihasilkan oleh mesin? '))
}
print('')
print("Masukkan spesifikasi mobil ke-4 :")
M4 = {
    'M4id': input('Masukkan merk mobil '),
    'M4C1': int(input('Berapa harga mobil yang ditawarkan? ')),
    'M4C2': int(input('Berapa jumlah penumpang maksimum? ')),
    'M4C3': int(input('Berapa jumlah konsumsi bahan bakar? ')),
    'M4C4': int(input('Berapa tenaga yang dihasilkan oleh mesin? '))
}
print('')
print("Masukkan spesifikasi mobil ke-5 :")
M5 = {
    'M5id': input('Masukkan merk mobil '),
    'M5C1': int(input('Berapa harga mobil yang ditawarkan? ')),
    'M5C2': int(input('Berapa jumlah penumpang maksimum? ')),
    'M5C3': int(input('Berapa jumlah konsumsi bahan bakar? ')),
    'M5C4': int(input('Berapa tenaga yang dihasilkan oleh mesin? '))
}

# PEMBOBOTAN
print(" ")
print("===BOBOT PERTIMBANGAN===")
W1 = 0
while not int(W1) in range(1, 5):
    W1 = input('Dari angka 1-5, seberapa pentingkah harga mobil? ')
    if W1.isdigit() and 1 <= int(W1) <= 5:
        break
    print("Input tidak diterima")

W2 = 0
while not int(W2) in range(1, 5):
    W2 = input('Dari angka 1-5, seberapa pentingkah kapasitas penumpang? ')
    if W2.isdigit() and 1 <= int(W2) <= 5:
        break
    print("Input tidak diterima")

W3 = 0
while not int(W3) in range(1, 5):
    W3 = input('Dari angka 1-5, seberapa pentingkah konsumsi BBM? ')
    if W3.isdigit() and 1 <= int(W3) <= 5:
        break
    print("Input tidak diterima")

W4 = 0
while not int(W4) in range(1, 5):
    W4 = input('Dari angka 1-5, seberapa pentingkah tenaga mesin? ')
    if W4.isdigit() and 1 <= int(W4) <= 5:
        break
    print("Input tidak diterima")

W1 = float(W1)
W2 = float(W2)
W3 = float(W3)
W4 = float(W4)

a = [W1, W2, W3, W4]
b = math.fsum(a)
#print(b)

w1 = W1 / b
w1 = w1 * -1
#print("W1 :", w1)
w2 = W2 / b
#print("W2 :", w2)
w3 = W3 / b
#print("W3 :", w3)
w4 = W4 / b
#print("W4 :", w4)

# RANKING
S1 = pow(M1['M1C1'], w1) * pow(M1['M1C2'], w2) * pow(M1['M1C3'], w3) * pow(M1['M1C4'], w4)
#print("Nilai S1 adalah :", S1)
S2 = pow(M2['M2C1'], w1) * pow(M2['M2C2'], w2) * pow(M2['M2C3'], w3) * pow(M2['M2C4'], w4)
#print("Nilai S2 adalah :", S2)
S3 = pow(M3['M3C1'], w1) * pow(M3['M3C2'], w2) * pow(M3['M3C3'], w3) * pow(M3['M3C4'], w4)
#print("Nilai S3 adalah :", S3)
S4 = pow(M4['M4C1'], w1) * pow(M4['M4C2'], w2) * pow(M4['M4C3'], w3) * pow(M4['M4C4'], w4)
#print("Nilai S4 adalah :", S4)
S5 = pow(M5['M5C1'], w1) * pow(M5['M5C2'], w2) * pow(M5['M5C3'], w3) * pow(M5['M5C4'], w4)
#print("Nilai S5 adalah :", S5)

c = [S1, S2, S3, S4, S5]
d = math.fsum(c)
#print(d)

V1 = S1 / d
V2 = S2 / d
V3 = S3 / d
V4 = S4 / d
V5 = S5 / d

e = {
    'V1':V1,
    'V2':V2,
    'V3':V3,
    'V4':V4,
    'V5':V5
    }
f = max(e, key=e.get)

if f == "V1":
    print("Mobil",M1['M1id'],"dapat dipertimbangkan untuk dipilih")
elif f == "V2":
    print("Mobil",M2['M2id'],"dapat dipertimbangkan untuk dipilih")
elif f == "V3":
    print("Mobil",M3['M3id'],"dapat dipertimbangkan untuk dipilih")
elif f== "V4":
    print("Mobil",M4['M4id'],"dapat dipertimbangkan untuk dipilih")
elif f == "V5":
    print("Mobil",M5['M5id'],"dapat dipertimbangkan untuk dipilih")
