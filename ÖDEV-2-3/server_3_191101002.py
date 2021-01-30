import socket
from Crypto.Cipher import AES
import hashlib


g = 7
p = 1237
b = 4

sunucuSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 2222
Buffer_Boyutu = 4096
sunucuSoketi.bind((host, port))
sunucuSoketi.listen(5)
print("\n" + str(port), "portu acildi ve baglantilar dinleniyor")

while True:
    print("Baglanti bekleniyor....")
    baglanti, istemciIPAdresi = sunucuSoketi.accept()  # proxy ile bağlantı olusturuldu
    print("Proxy'den gelen baglanti kabul edildi")
    print('Baglanan istemci IP Adresi ve Portu:', istemciIPAdresi)
    sunucuSifre = (g ** b) % p
    baglanti.send(bytes(str(sunucuSifre), "utf-8"))
    print("Sifre gönderildi")
    print("Proxy'den şifre alinmasi bekleniyor...")
    proxydenGelenSifre = baglanti.recv(Buffer_Boyutu)
    print("Proxy'den şifre geldi:", proxydenGelenSifre)
    anahtar = (int(proxydenGelenSifre.decode("utf-8")) ** b) % p
    print("Ortak anahtar oluşturuldu:", anahtar)

    password = str(anahtar).encode("utf-8")
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = bytes('This is an IV456', "utf-8")
    cipher = AES.new(key, mode, IV)

    proxydenGelenMesaj = baglanti.recv(Buffer_Boyutu)
    print("Proxy'den mesaj alındı.")
    proxydenGelenMesajSifresiz = (cipher.decrypt(proxydenGelenMesaj).rstrip()).decode("utf-8")
    proxydenGelenMesajSifreli = proxydenGelenMesaj.rstrip().decode('latin-1')
    x = proxydenGelenMesajSifresiz.split(" ")
    isimSoyisim = x[0] + " " + x[1] + " - şifreli"
    krediKartNo = x[2]
    gecerlilikSuresi = x[3]
    guvenlikKodu = x[4]
    dosya = open(isimSoyisim, "w", encoding="utf-8")
    dosya.write(proxydenGelenMesajSifreli)
    dosya.close()

    isimSoyisim = x[0] + " " + x[1]

    dosya = open(isimSoyisim, "w", encoding="utf-8")
    dosya.write(krediKartNo + "\n" + gecerlilikSuresi + "\n" + guvenlikKodu)
    dosya.close()
    baglanti.close()
    print("Proxy ile baglanti kesildi.")
    break
