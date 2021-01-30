import socket

sunucuSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 19110
Buffer_Boyutu = 4096
sunucuSoketi.bind((host, port))
sunucuSoketi.listen(1)
print("\n" + str(port), "portu acildi ve baglantilar dinleniyor" + "\n")

while True:
    print("Baglanti bekleniyor....")
    baglanti, istemciIPAdresi = sunucuSoketi.accept()  # Baglanti talebi olusturuldu
    print("Proxy'den gelen baglanti talebi kabul edildi")
    print('Baglanan istemci IP Adresi ve Portu:', istemciIPAdresi)
    print("Istemciden mesaj alinmasi bekleniyor...")
    while True:
        istemcidenGelenMesaj = baglanti.recv(Buffer_Boyutu)
        if not istemcidenGelenMesaj:
            break
        print("Istemciden mesaj geldi: ", istemcidenGelenMesaj)
        print("Istemciden mesaj alindi ve Buffer bosaldi. Proxy ile baglanti kesiliyor...")
        istemcidenGelenMesaj = istemcidenGelenMesaj.decode("utf-8")
        x = istemcidenGelenMesaj.split(" ")
        isimSoyisim = x[0] + " " + x[1]
        krediKartNo = x[2]
        gecerlilikSuresi = x[3]
        guvenlikKodu = x[4]
        dosya = open(isimSoyisim, "w", encoding="utf-8")
        dosya.write(krediKartNo + "\n" + gecerlilikSuresi + "\n" + guvenlikKodu)
        dosya.close()
    baglanti.close()
    print("Proxy ile baglanti kesildi.")
    break
