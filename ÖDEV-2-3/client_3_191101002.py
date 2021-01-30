import socket
from Crypto.Cipher import AES
import hashlib

def pad_message(message):
    while len(message) % 16 != 0:
        message = message + b" "
    return message

g = 7
p = 1237
a = 6

Buffer_Boyutu = 4096
sunucuAdi = 'localhost'
sunucuPortu = 1111

istemciSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
istemciSoketi.connect((sunucuAdi, sunucuPortu)) # proxy ile baglanti kuruldu
sifre = (g ** a) % p #sifre olusturuldu
istemciSoketi.send(bytes(str(sifre), "utf-8"))
print("Şifre gönderildi.")
sunucudanGelenSifre = istemciSoketi.recv(Buffer_Boyutu)
print("Proxy'den şifre geldi.", sunucudanGelenSifre)
anahtar = (int(sunucudanGelenSifre.decode("utf-8")) ** a) % p
print("Ortak anahtar oluşturuldu:", anahtar)
isimSoyisim = input("İsim ve soyisminiz:") + " "
krediKartNo = input("Kredi kartı numaranız:") + " "
gecerlilikSuresi = input("Geçerlilik süresi:") + " "
guvenlikKodu = input("Güvenlik Kodu:") + " "
gonderilecekMesaj = isimSoyisim + krediKartNo + gecerlilikSuresi + guvenlikKodu

password = str(anahtar).encode("utf-8")
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = bytes('This is an IV456', "utf-8")
cipher = AES.new(key, mode, IV)
padded_message = pad_message(bytes(gonderilecekMesaj,"utf-8"))
sifrelenmisMesaj = cipher.encrypt(padded_message)

istemciSoketi.send(sifrelenmisMesaj)
print("Veri sunucuya basarili bir sekilde gonderildi.")