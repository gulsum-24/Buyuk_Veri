def elbise_listele(baglanti,sorgu):
    uygula = baglanti.cursor()
    komut = sorgu
    uygula.execute(komut)
    return uygula



def elbise_ekle(baglanti, ekle):
    uygula2 = baglanti.cursor()
    komut2= ekle
    uygula2.execute(komut2)
    return uygula2



def elbise_silme(baglanti,silme):
    uygula3 =baglanti.cursor()
    komut3 = silme
    uygula3.execute(komut3)
    return uygula3



def elbise_guncelle(baglanti, guncelle):
    uygula4 = baglanti.cursor()
    komut4 = guncelle
    uygula4.execute(komut4)
    return uygula4
