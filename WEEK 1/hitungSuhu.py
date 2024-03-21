def fahrenKeCelci(suhuFahren):
    return (suhuFahren - 32) * 5/9

def celciKeFahren(suhuCelci):
    return (suhuCelci * 9/5) + 32

print("DAFTAR MENU :")
print("1. Fahrenheit ke Celsius")
print("2. Celsius ke Fahrenheit")

menu = int(input("Pilih Menu : "))

if menu == 1:
    suhuFahren = float(input("Masukkan suhu dalam Fahrenheit: "))
    suhuCelci = fahrenKeCelci(suhuFahren)
    print("Suhu dalam Celsius:", round(suhuCelci, 2), "C")
elif menu == 2:
    suhuCelci = float(input("Masukkan suhu dalam Celsius: "))
    suhuFahren = celciKeFahren(suhuCelci)
    print("Suhu dalam Fahrenheit:", round(suhuFahren, 2), "F")
else:
    print("menu tidak valid.")