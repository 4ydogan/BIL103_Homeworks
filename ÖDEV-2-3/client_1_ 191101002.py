import socket

Buffer_Boyutu = 4096
sunucuAdi = 'localhost'
sunucuPortu = 19110
istemciSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
istemciSoketi.connect((sunucuAdi,sunucuPortu))
isimSoyisim = input("İsim ve soyisminiz:") + " "
krediKartNo = input("Kredi kartı numaranız:") + " "
gecerlilikSuresi = input("Geçerlilik süresi:") + " "
guvenlikKodu = input("Güvenlik Kodu:") + " "
gonderilecekMesaj = bytes(isimSoyisim + krediKartNo + gecerlilikSuresi + guvenlikKodu,"utf-8")
istemciSoketi.send(gonderilecekMesaj)
print("Veri sunucuya basarili bir sekilde gonderildi.")
sunucudanGelenMesaj = istemciSoketi.recv(Buffer_Boyutu)
