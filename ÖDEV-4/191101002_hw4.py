import sqlite3

vt = sqlite3.connect('AydoganInsanKaynakları.db')

imlec = vt.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS calisanBilgisi (SicilNo, IsimSoyisim, Adres, TCKimlikNo)")

imlec.execute("INSERT INTO calisanBilgisi VALUES ('11111', 'Ahmet Bulut', 'Aydınlıkevler Mah.', '45646464654')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('22222', 'Funda Doğan', 'Bahçelievler Mah.', '23424242422')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('33333', 'Ayşe Güneş', 'Beşevler Mah.', '95847305739')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('44444', 'Mustafa Toprak', 'Çiçekevler Mah.', '23058380395')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('55555', 'Kerem Yağmur', 'Uzunvler Mah.', '46383069744')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('66666', 'Furkan Taş', 'Kısaevler Mah.', '23409824366')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('77777', 'Murat Gezgin', 'Yatayevler Mah.', '87639046399')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('88888', 'Mehmet Koç', 'Karanlıkevler Mah.', '88347643292')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('99999', 'Halil Gönül', 'Soğukevler Mah.', '75354869876')")
imlec.execute("INSERT INTO calisanBilgisi VALUES ('10101', 'Mert Erkin', 'Sıcakevler Mah.', '12653874248')")


imlec.execute("CREATE TABLE IF NOT EXISTS gorevBilgisi (GörevKodu, GörevÜnvanı, GörevBölümü)")

imlec.execute("INSERT INTO gorevBilgisi VALUES ('12345', 'Bilgisayar Mühendisi', 'Uygulama')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('23456', 'Makine Mühendisi', 'Bakım')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('34567', 'Endüstri Mühendisi', 'Pazarlama')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('98765', 'Elektrik Mühendisi', 'Test')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('87654', 'Yapay Zeka Mühendisi', 'İstatistik')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('76543', 'Bilgisayar Mühendisi', 'Çözüm')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('65432', 'Bilgisayar Mühendisi', 'Yönetim')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('54321', 'Bilgisayar Mühendisi', 'Proje Döngüsü')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('67890', 'Bilgisayar Mühendisi', 'Kodlama')")
imlec.execute("INSERT INTO gorevBilgisi VALUES ('34677', 'Bilgisayar Mühendisi', 'Uygulama')")


imlec.execute("CREATE TABLE IF NOT EXISTS gorevlendirmeBilgisi (SicilNo, GörevKodu, BaşlamaTarihi, BitişTarihi)")

imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('11111', '12345', '15.11.2019', '*')")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('22222', '23456', '24.09.2017', '15.11.2019')")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('33333', '34567', '13.12.2020', '*')")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('44444', '98765', '23.12.2018', '*')")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('55555', '87654', '23.01.2016', '07.04.2017')")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('66666', '76543', '11.05.2019', '*')")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('77777', '65432', '11.07.2019', '07.12.2020')")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('88888', '54321', '07.04.2017', '*')")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('99999', '67890', '09.02.2020', '23.12.2018' )")
imlec.execute("INSERT INTO gorevlendirmeBilgisi VALUES ('10101', '34677', '22.06.2020', '*')")

goreviBilgisayar = list()
sicilIcin = list()

print("Bilgisayar Mühendisi GörevÜnvanı ile herhangi bir zamanda görevlendirilmiş olan çalışanlar sorgulanıyor...")
imlec.execute('SELECT * FROM gorevBilgisi WHERE GörevÜnvanı = "Bilgisayar Mühendisi"')
for row in imlec.fetchall():
    gecici = list(row)
    goreviBilgisayar += gecici

for i in range(len(goreviBilgisayar)//3):
    a = str(goreviBilgisayar[i*3])
    imlec.execute('SELECT * FROM gorevlendirmeBilgisi WHERE GörevKodu = ?', (a,))
    for row in imlec.fetchall():
        gecici = list(row)
        sicilIcin += gecici

print("Bilgisayar Mühendisi GörevÜnvanı ile herhangi bir zamanda görevlendirilmiş olan çalışanlar:\n")

for i in range(len(sicilIcin)//4):
    a = str(sicilIcin[i*4])
    imlec.execute('SELECT * FROM calisanBilgisi WHERE SicilNo = ?', (a,))
    for row in imlec.fetchall():
        gecici = list(row)
        print("TcNo: " + gecici[3] + " ******* Adres: " +gecici[2])

print("\nBilgisayar Mühendisi GörevÜnvanı ile halen görevde olan çalışanlar sorgulanıyor...")

goreviBilgisayar = list()
sicilIcin = list()

imlec.execute('SELECT * FROM gorevBilgisi WHERE GörevÜnvanı = "Bilgisayar Mühendisi"')
for row in imlec.fetchall():
    gecici = list(row)
    goreviBilgisayar += gecici

for i in range(len(goreviBilgisayar)//3):
    a = str(goreviBilgisayar[i*3])
    imlec.execute('SELECT * FROM gorevlendirmeBilgisi WHERE GörevKodu = ?', (a,))
    for row in imlec.fetchall():
        gecici = list(row)
        if gecici[3] == "*":
            sicilIcin += gecici

print("Bilgisayar Mühendisi GörevÜnvanı ile halen görevde olan çalışanlar:\n")

for i in range(len(sicilIcin)//4):
    a = str(sicilIcin[i*4])
    imlec.execute('SELECT * FROM calisanBilgisi WHERE SicilNo = ?', (a,))
    for row in imlec.fetchall():
        gecici = list(row)
        print("TcNo: " + gecici[3] + " ******* Adres: " +gecici[2])

vt.commit()
vt.close()