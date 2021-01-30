import socket
from Crypto.Cipher import AES
import hashlib

g = 7
p = 1237

proxyIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxyOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
portClient = 1111
Buffer_Boyutu = 4096
proxyIn.bind((host, portClient))
proxyIn.listen()

host = "localhost"
portServer = 2222
proxyOut.connect((host, portServer))



while True:
    print("Bağlantı bekleniyor....")
    baglanti, istemciIPAdresi = proxyIn.accept()  # server ile bağlantı olusturuldu
    print("Istemciden gelen baglanti kabul edildi")
    print('Baglanan istemci IP Adresi ve Portu:', istemciIPAdresi)

    print("Istemciden şifre alinmasi bekleniyor...")
    istemcidenGelenSifre = baglanti.recv(Buffer_Boyutu)
    print("Istemciden şifre geldi: ", istemcidenGelenSifre)
    proxyOut.send(istemcidenGelenSifre)
    print("Istemciden gelen şifre sunucuya gönderildi.")

    print("Sunucudan şifre gelmesi bekleniyor...")
    sunucudanGelenSifre = proxyOut.recv(Buffer_Boyutu)
    print("Sunucudan şifre geldi: ", sunucudanGelenSifre)
    baglanti.send(sunucudanGelenSifre)
    print("Sunucudan gelen şifre istemciye gönderildi.")

    print("Istemciden mesaj alinmasi bekleniyor...")
    istemcidenGelenMesaj = baglanti.recv(Buffer_Boyutu)
    print("Istemciden mesaj geldi: ", istemcidenGelenMesaj)
    gonderilecekMesaj = istemcidenGelenMesaj
    proxyOut.send(gonderilecekMesaj)
    print("Istemciden gelen mesaj sunucuya gonderildi.")

    istemcidenGelenSifreStr = istemcidenGelenSifre.decode("utf-8")
    sunucudanGelenSifreStr = sunucudanGelenSifre.decode("utf-8")
    anahtarSunucu = 0
    anahtarIstemci = -1
    anahtar = 0

    b = 0
    a = 0
    sifreA = 0
    sifreB = 0

    for k in range(p):
        sifreA = (g ** k) % p
        if sifreA == int(istemcidenGelenSifreStr):
            for i in range(1, p):
                sifreB = (g ** i) % p
                if sifreB == int(sunucudanGelenSifreStr):
                    anahtarIstemci = (sifreB ** k) % p
                    anahtarSunucu = (sifreA ** i) % p
                if anahtarIstemci == anahtarSunucu:
                    anahtar = anahtarIstemci
                    a = i
                    b = k
                    break
    print("anahtar:", anahtar)
    password = str(anahtar).encode("utf-8")
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = bytes('This is an IV456', "utf-8")
    cipher = AES.new(key, mode, IV)
    sifresizMesaj = (cipher.decrypt(istemcidenGelenMesaj).rstrip()).decode("utf-8")
    print("sifresizMesaj:", sifresizMesaj)
    break
