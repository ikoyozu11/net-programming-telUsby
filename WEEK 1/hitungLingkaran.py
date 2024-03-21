def hitungLuas(jariJari):
    return 3.14 * (jariJari ** 2)

def hitungKeliling(jariJari):
    return 2 * 3.14 * jariJari

jariJari = float(input("Masukkan panjang jari-jari lingkaran : "))

luas = hitungLuas(jariJari)
keliling = hitungKeliling(jariJari)

print("----------")
print("Luas lingkaran adalah :", round(luas, 2))
print("Keliling lingkaran adalah :", round(keliling, 2))