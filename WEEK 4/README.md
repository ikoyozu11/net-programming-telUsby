<h1 align="left">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&color=F7AA00&center=false&vCenter=true&width=800&height=70&duration=4000&pause=500&lines=⚡+Welcome+to+My+Repository+⚡;+Network+Programming+Socket+😁;"/>
</h1>
<p><strong>Nama : Okky Rangga Pratama</strong></p>
<p><strong>NIM : 1203220011</strong></p>
<p><strong>Kelas : IF-02-01</strong></p>

<hr>

<p>Hello everyone👋, This is a repository for Networking Programming course code Socket Programming topic in semester 4 at the Telkomuniversity National Campus Surabaya🧑‍💻.</p>
<p>Don't forget to leave a mark by giving a star⚡on this repository.</p>

<hr>

<h2>Penjelasan Modul</h2>

## Soal 1 & Jawaban
1.	Membuat laporan percobaan praktikum dan beri Analisa Hasil Percobaan tadi yang sudah dibuat Pembuatan Aplikasi Client-Server Sederhana (Single Thread)

**A. Code Server**
```python
import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

HOST = 'localhost' 
PORT = 12345 

server_socket.bind((HOST, PORT)) 

server_socket.listen(1) 
print("Waiting...") 
client_socket, client_address = server_socket.accept() 

data = client_socket.recv(1024) 

angka = int(data.decode()) 
print("Request dari client :", angka, ", dengan IP client :", client_address) 

if angka % 2 == 0: 
    response = "angka " + str(angka) + " merupakan genap" 
else: 
    response = "angka " + str(angka) + " merupakan ganjil"

client_socket.sendall(response.encode()) 

client_socket.close() 
server_socket.close()
```
Berikut penjelasan kode program diatas :

- Membuat objek socket untuk server.
```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
``` 
- Mendefinisikan alamat host (localhost) dan nomor port (12345) yang digunakan oleh server. Localhost mengacu pada komputer server dan Port dipilih secara acak tetapi harus cocok dengan port yang digunakan klien.
```python
HOST = 'localhost' 
PORT = 12345
``` 
- Mengikat (bind) socket server ke alamat dan port yang telah dibuat.
```python
server_socket.bind((HOST, PORT)) 
```
- Mengaktifkan mode listen pada socket server dengan parameter 1 yang menentukan jumlah maksimum antrian koneksi yang diterima oleh server.
```python
server_socket.listen(1) 
```
- Mencetak pesan sebagai penanda server menunggu koneksi dari klien.
```python
print("Waiting...") 
```
- Membuat metode untuk menerima koneksi dari klien. Metode accept() akan memblokir program sampai klien terhubung. Setelah koneksi diterima, server akan mengembalikan socket klien dan alamat klien.
```python
client_socket, client_address = server_socket.accept() 
```
- Membuat metode untuk menerima pesan dari klien dengan parameter 1024 yang menunjukkan ukuran buffer yang akan digunakan untuk menerima data.
```python
data = client_socket.recv(1024) 
```
- Mendekode data yang diterima dari klien menjadi string kemudian mongonversi data tersebut menjadi integer. Data yang dikonversi akan disimpan didalam variabel angka.
```python
angka = int(data.decode())
```
- Mencetak informasi permintaan yang diterima dari klien, termasuk angka yang dikirim dan Alamat IP klien.
```python
print("Request dari client :", angka, ", dengan IP client :", client_address) 
```
- Membuat kondisi untuk mengecek apakah data yang diterima dari klien itu ganjil atau genap.
```python
if angka % 2 == 0: 
    response = "angka " + str(angka) + " merupakan genap" 
else: 
    response = "angka " + str(angka) + " merupakan ganjil"
```
- Mengirim respon Kembali kepada klien.
```python
client_socket.sendall(response.encode())
```
- Menutup koneksi socket klien dan socket server.
```python
client_socket.close() 
server_socket.close()
```

**B. Code Klien**
```python
import socket 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

HOST = 'localhost' 
PORT = 12345 
client_socket.connect((HOST, PORT)) 

pesan = input("Masukkan angka :") 
client_socket.sendall(pesan.encode()) 

data = client_socket.recv(1024) 
print(data.decode()) 

client_socket.close()
```
Berikut penjelasan kode program diatas :

- Membuat objek socket untuk klien.
```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
``` 
- Mendefinisikan alamat host (localhost) dan nomor port (12345). Localhost mengacu pada komputer klien dan Port dipilih secara acak tetapi harus cocok dengan port yang digunakan server.
```python
HOST = 'localhost' 
PORT = 12345
``` 
- Membuat metode untuk mengoneksikan klien ke server.
```python
client_socket.connect((HOST, PORT)) 
```
- Meminta klien memasukkan pesan yang akan dikirim ke server.
```python
pesan = input("Masukkan angka :")
``` 
- Membuat metode untuk mengirimkan pesan ke server.
```python
client_socket.sendall(pesan.encode())
``` 
- Membuat metode untuk menerima pesan dari server. Parameter 1024 menunjukkan ukuran buffer yang digunakan untuk menerima data.
```python
data = client_socket.recv(1024)
``` 
- Membuat metode untuk mencetak pesan yang diterima dari server.
```python
print(data.decode())
``` 
- Menutup koneksi dengan server.
```python
client_socket.close()
```

## Soal 2, 3 & Jawaban
2.	Membuat sebuah program server yang dapat menerima koneksi dari klien menggunakan protokol TCP. Server ini akan menerima pesan dari klien dan mengirimkan pesan balasan berisi jumlah karakter pada pesan tersebut. Gunakan port 12345 untuk server. Membuat analisa dari hasil program tersebut.
3.	Membuat sebuah program klien yang dapat terhubung ke server yang telah dibuat pada soal nomor 1. Klien ini akan mengirimkan pesan ke server berupa inputan dari pengguna dan menampilkan pesan balasan jumlah karakter yang diterima dari server. 


<hr>

<h3 align="left">Thank you and have a great day ❤</h3>
