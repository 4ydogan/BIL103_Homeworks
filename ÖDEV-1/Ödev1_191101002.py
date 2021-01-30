import os
import sys

ogrenci_no = input("ANO hesaplaması yapılacak öğrencinin öğrenci numarasını giriniz:")
ogrenci_txt = ogrenci_no + ".txt"
harfKarsilik = {"AA": 4.00, "BA": 3.50, "BB": 3.00, "CB": 2.50, "CC": 2.00, "DC": 1.50, "DD": 1.00, "FD": 0.50, "FF": 0.00, }

krediler = {"BİL103": 2, "BİL113": 4, "MAT101": 4, "FİZ101": 3, "FİZ101L": 1, "TÜR101": 2, "İNG001": 2,
            "BİL211": 4, "BİL132": 3, "MAT102": 4, "FİZ102": 3, "FİZ102L": 1, "TÜR102": 2, "İNG002": 2,
            "BİL133": 3, "BİL212": 4, "BİL264": 3, "BİL264L": 1, "BİL245": 4, "AİT201": 2, "İNG003": 2,
            "BİL214": 4, "BİL334": 3, "BİL361": 3, "İKT105": 3, "OEG101": 1, "AİT202": 2, "İNG004": 2,
            "BİL331": 3, "BİL395": 3, "BİL481": 3, "BİL345": 3, "UGİ315": 2, "İYD1": 3,
            "BİL372": 4, "BİL461": 3, "İYD2": 3,
            "BİL452": 3, "BİL495": 1, "İYD3": 3, "BİL496": 4, "İYD4": 3, }

if os.path.isfile(ogrenci_txt):

    toplamKredi = 0
    result = 0.0

    for satir in open(ogrenci_txt, "r", encoding="utf-8"):
        x = satir.split()

        dersKredi = krediler.get(x[0],None)
        if dersKredi is None:
            print("Müfredat dışı ders bulundu.")
            sys.exit()

        harfNotu = harfKarsilik.get(x[1],None)
        if harfNotu is None:
            print("Geçersiz not bulundu.")
            sys.exit()

        toplamKredi += dersKredi
        result += harfNotu * dersKredi

    if(result == 0.0 and toplamKredi == 0):
        print("Hatalı ders veya not bilgisi girildi veya not bilgisi girilmedi.")
    else:
        result = result / toplamKredi
        result = round(result, 2)
        print(ogrenci_no, "no'lu öğrencinin not ortalaması:", result)
else:
    print("Bu öğrenciye ait not bilgisi bulunamadı.")