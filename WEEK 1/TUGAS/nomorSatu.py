def cariPrima(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def tampilBilPrima(n):
    print("Bilangan prima dari 1 hingga", n, "adalah:")
    for num in range(2, n + 1):
        if cariPrima(num):
            print(num)

n = int(input("Masukkan nilai n : "))
tampilBilPrima(n)