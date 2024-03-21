def tampilAngka(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 4 == 0:
            print("Index =", i, "Output = OKYES")
        elif i % 3 == 0:
            print("Index =", i, "Output = OK")
        elif i % 4 == 0:
            print("Index =", i, "Output = YES")
        else:
            print("Index =", i, "Output =", i)

n = int(input("Masukkan nilai n : "))
print("----------")
print("Output :")
tampilAngka(n)