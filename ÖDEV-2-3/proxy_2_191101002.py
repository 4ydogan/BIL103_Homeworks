import socket

proxyIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxyOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
portClient = 6666
Buffer_Boyutu = 4096
proxyIn.bind((host, portClient))
proxyIn.listen()

host = "localhost"
portServer = 19110
proxyOut.connect((host, portServer))



while True:
    print("Bağlantı bekleniyor....")
    baglanti, istemciIPAdresi = proxyIn.accept()  # server ile bağlantı olusturuldu
    print("Istemciden gelen baglanti kabul edildi")
    print('Baglanan istemci IP Adresi ve Portu:', istemciIPAdresi)
    istemcidenGelenMesaj = baglanti.recv(Buffer_Boyutu)
    if not istemcidenGelenMesaj:
        break
    print("Istemciden mesaj geldi: ", istemcidenGelenMesaj)
    gonderilecekMesaj = istemcidenGelenMesaj
    print("Veri sunucuya basarili bir sekilde gonderildi.")
    proxyOut.send(gonderilecekMesaj)
    break

