import socket

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
    break

