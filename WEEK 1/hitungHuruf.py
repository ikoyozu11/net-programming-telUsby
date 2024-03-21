def hitungKarakter(kata):
    jumlahKarakter = {}
    totalKarakter = 0
    for huruf in kata.lower():
        if huruf in jumlahKarakter:
            jumlahKarakter[huruf] += 1
        else:
            jumlahKarakter[huruf] = 1
        totalKarakter += 1
    return jumlahKarakter, totalKarakter

kata = input("Masukkan sebuah kata : ")
jumlahKarakter, totalKarakter = hitungKarakter(kata)
print("----------")
print("Jumlah huruf dalam kata '{}' adalah :".format(kata))
for huruf, jumlah in jumlahKarakter.items():
    print("{} = {}".format(huruf, jumlah))
print("----------")
print("Total huruf :", totalKarakter)